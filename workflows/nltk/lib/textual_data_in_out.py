from workflows.textflows import *
import os.path
import time
import re


def load_adc(inputDict):
    file_path = inputDict['file']
    file_name = unicode(os.path.basename(file_path))

    seconds = os.path.getctime(file_path)
    source_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(seconds)))
    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))

    texts = re.split("[\r\n]", open(file_path, "r").read())

    _tabSeparatedTitle = inputDict['tabSeparatedTitle'] == "true"
    _leadingLabels = inputDict['leadingLabels'] == "true"
    documents = []
    for i, text in enumerate(texts):
        title = u"Document" + unicode(i + 1)
        features = {u"contentType": u"Text", u"sourceFileLine": unicode(i)}
        if _tabSeparatedTitle:
            text = text.split("\t")
            title = unicode(text[0])
            text = u"\t".join(text[1:])

        if _leadingLabels:
            text = text.split("\t")
            for feature in [f.strip() for f in text[0].split("!") if f != u""]:
                features[feature] = "true"
            text = u"".join(text[1:])

        documents.append(Document(name=title,
                                  features=features,
                                  text=text,
                                  annotations=[Annotation(spanStart=0,
                                                          spanEnd=max(0, len(unicode(text)) - 1),
                                                          type1=u"TextBlock",
                                                          features={})]))

    features = {u"Source": file_name, u"SourceDate": source_date, u"CorpusCreateDate": corpus_date}

    output_dict = {"adc": DocumentCorpus(documents=documents, features=features)}
    return output_dict


def load_adcfrom_string(inputDict):

    source_date = unicode("unknown")
    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))

    texts = re.split("[\r\n]", inputDict['plainString'])

    _tabSeparatedTitle = inputDict['tabSeparatedTitle'] == "true"
    _leadingLabels = inputDict['leadingLabels'] == "true"
    documents = []
    for i, text in enumerate(texts):
        title = u"Document" + unicode(i + 1)
        features = {u"contentType": u"Text", u"sourceFileLine": unicode(i)}
        if _tabSeparatedTitle:
            text = text.split("\t")
            title = unicode(text[0])
            text = u"\t".join(text[1:])

        if _leadingLabels:
            text = text.split("\t")
            for feature in [f.strip() for f in text[0].split("!") if f != u""]:
                features[feature] = "true"
            text = u"".join(text[1:])

        documents.append(Document(name=title,
                                  features=features,
                                  text=text,
                                  annotations=[Annotation(spanStart=0,
                                                          spanEnd=max(0, len(unicode(text)) - 1),
                                                          type1=u"TextBlock",
                                                          features={})]))

    features = {u"Source": "string", u"SourceDate": source_date, u"CorpusCreateDate": corpus_date}

    output_dict = {"adc": DocumentCorpus(documents=documents, features=features)}
    return output_dict


def nltk_show_adc(input_dict):
    if input_dict["adc"] is None:
        raise Exception("Input ADC is required for displaying Anotated Document Corpus!")
    return {}
