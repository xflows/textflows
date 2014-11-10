from workflows.textflows import *
import os.path
import time
import re


def load_adc_from_file(inputDict):
    file_path = inputDict['file']
    file_name = unicode(os.path.basename(file_path))
    texts = re.split("[\r\n]", open(file_path, "r").read())

    seconds = os.path.getctime(file_path)
    source_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(seconds)))
    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))

    documents = load_adc(texts, inputDict['tabSeparatedTitle'], inputDict['leadingLabels'])
    features = {u"Source": file_name, u"SourceDate": source_date, u"CorpusCreateDate": corpus_date}

    output_dict = {"adc": DocumentCorpus(documents=documents, features=features)}
    return output_dict


def load_adc_from_string(inputDict):
    source_date = unicode("unknown")
    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
    texts = re.split("[\r\n]", inputDict['plainString'])

    documents = load_adc(texts, inputDict['tabSeparatedTitle'], inputDict['leadingLabels'])
    features = {u"Source": "string", u"SourceDate": source_date, u"CorpusCreateDate": corpus_date}

    output_dict = {"adc": DocumentCorpus(documents=documents, features=features)}
    return output_dict

def load_adc(texts,  _tabSeparatedTitle, _leadingLabels):
    documents = []
    for i, text in enumerate(texts):
        title = u"Document" + unicode(i + 1)
        features = {u"contentType": u"Text", u"sourceFileLine": unicode(i)}
        if _tabSeparatedTitle == "true":
            text = text.split("\t")
            title = unicode(text[0])
            text = "\t".join(text[1:])

        if _leadingLabels == "true":
            text = text.split("\t")
            for feature in [f.strip() for f in text[0].split("!") if f != u""]:
                features[feature] = "true"
            text = "".join(text[1:])

        documents.append(Document(name=title,
                                  features=features,
                                  text=unicode(text),
                                  annotations=[Annotation(spanStart=0,
                                                          spanEnd=max(0, len(unicode(text)) - 1),
                                                          type1=u"TextBlock",
                                                          features={})]))
    return documents

def nltk_show_adc(input_dict):
    if input_dict["adc"] is None:
        raise Exception("Input ADC is required for displaying Anotated Document Corpus!")
    return {}
