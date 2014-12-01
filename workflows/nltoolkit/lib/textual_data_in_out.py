from workflows.textflows import *
import os.path
import time
import re


def load_adc_from_file(input_dict):
    """
    This widges processes raw text file and loads the texts into ADC (Annotated Document Corpus) structure.
    The input file contains one document per line - the whole line represents text from the body of a document.
    In case lines contain more document properties (i.e.: ids, titles, labels,...) than other widgets should be used to load ADC structure.

    :param file: file path
    :return adc: Annotated Document Corpus (workflows.textflows.DocumentCorpus)
    """
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
    """
    This widges processes input text and loads it into ADC (Annotated Document Corpus) structure.
    The input text contains one document per line - the whole line represents text from the body of a document.
    In case lines contain more document properties (i.e.: ids, titles, labels,...) than other widgets should be used to load ADC structure.

    :param plain_string: documents text
    :return adc: Annotated Document Corpus (workflows.textflows.DocumentCorpus)
    """
    source_date = unicode("unknown")
    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
    texts = re.split("[\r\n]", input_dict['plain_string'])

    documents = load_adc(texts, input_dict['tab_separated_title'] == "true", input_dict['leading_labels'] == "true")
    features = {u"Source": "string", u"SourceDate": source_date, u"CorpusCreateDate": corpus_date}

    output_dict = {"adc": DocumentCorpus(documents=documents, features=features)}
    return output_dict


def load_adc(texts,  tab_separated_title, leading_labels):
    """
    function parses title and labels for documents from text and it sets annnotation for each document.

    :param texts: list of documents
    :param tab_separated_title: document title is separated from the text with \t. Example: title \t start of text
    :param leading_labels: documents has labels infront of the text. Example: !LB1 !Lb2 !LBL \t start of text
    :return: list of documents
    """
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


def get_plain_texts(input_dict):
    """
    Widget transforms Annotated Document Corpus to string.

    :param adc: Annotated Document Corpus.
    :param element_annotation: Token Annotation.
    :param element_feature_conditions: Which tokens to include based on their features.
    :param delimiter: Delimiter for token concatenation.
    :param include_doc_id: Include Document Identifier.
    :return: String with all documents in Annotated Document Corpus.

    """

    adc = input_dict['adc']
    element_annotation = input_dict['element_annotation']
    element_feature_conditions = input_dict['element_feature_conditions']
    delimiter = input_dict['delimiter']
    includeDocId = input_dict['include_doc_id'] == "true"

    output_dict = {}
    if includeDocId:
        output_dict["strings"] = {}
        for document in adc.documents:
            output_dict["strings"][document.name] = document.text
    else:
        output_dict["strings"] = []
        for document in adc.documents:
            output_dict["strings"].append(document.text)

    return output_dict


def statistics(input_dict):
    """
    Statistics of Annotated Document Corpus.

    :param adc: Annotated Document Corpus.
    :return doc_count (int): Number of Documents.
    :return feature_count (int): Number of Features.
    :return description (string): Statistics.
    """

    output_dict = {}
    output_dict["doc_count"] = len(input_dict["adc"].documents)
    output_dict["feature_count"] = len(input_dict["adc"].features)
    output_dict["description"] = "Number of documents is " + str(output_dict["doc_count"]) + \
                                 ", number of corpus features is " + str(output_dict["feature_count"]) + "."
    return output_dict


def display_document_corpus(input_dict):
    #implemented in visualization_views.py
    return {}
