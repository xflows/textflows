from workflows.textflows import *
import os.path
import time
import re


def load_adc_from_file(input_dict):
    file_path = input_dict['file']
    file_name = unicode(os.path.basename(file_path))
    texts = re.split("[\r\n]", open(file_path, "r").read())

    seconds = os.path.getctime(file_path)
    source_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(seconds)))
    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))

    documents = load_adc(texts, input_dict['tab_separated_title'] == "true", input_dict['leading_labels'] == "true")
    features = {u"Source": file_name, u"SourceDate": source_date, u"CorpusCreateDate": corpus_date}

    output_dict = {"adc": DocumentCorpus(documents=documents, features=features)}
    return output_dict


def load_adc_from_string(input_dict):
    source_date = unicode("unknown")
    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
    texts = re.split("[\r\n]", input_dict['plain_string'])

    documents = load_adc(texts, input_dict['tab_separated_title'] == "true", input_dict['leading_labels'] == "true")
    features = {u"Source": "string", u"SourceDate": source_date, u"CorpusCreateDate": corpus_date}

    output_dict = {"adc": DocumentCorpus(documents=documents, features=features)}
    return output_dict


def load_adc(texts,  tab_separated_title, leading_labels):
    documents = []
    for i, text in enumerate(texts):
        title = u"Document" + unicode(i + 1)
        features = {u"contentType": u"Text", u"sourceFileLine": unicode(i)}

        if tab_separated_title:
            #example: title \t start of text
            text = text.split("\t")
            title = unicode(text[0])
            text = "\t".join(text[1:])

        if leading_labels:
            #example: !LB1 !Lb2 !LBL \t start of text
            text = text.split("\t")
            for feature in [f.strip() for f in text[0].split("!") if f != u""]:
                features[feature] = "true"
            text = "".join(text[1:])

        documents.append(Document(name=title,
                                  features=features,
                                  text=unicode(text),
                                  annotations=[Annotation(span_start=0,
                                                          span_end=max(0, len(unicode(text)) - 1),
                                                          type=u"TextBlock",
                                                          features={})]))
    return documents


def display_document_corpus(input_dict):
    return {}
