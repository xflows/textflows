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
    :param feature_annotation: Select a feature annotation.
    :param delimiter: Delimiter for token concatenation.
    :param include_doc_id: Include Document Identifier.
    :return: String with all documents in Annotated Document Corpus.

    """

    adc = input_dict['adc']
    feature_annotation = input_dict['feature_annotation']
    delimiter = input_dict['delimiter']
    includeDocId = input_dict['include_doc_id'] == "true"

    output_dict = {}
    if includeDocId:
        output_dict["strings"] = {}
        for document in adc.documents:
            output_dict["strings"][document.name] = delimiter.join([t[1] for t in document.get_annotations_with_text(feature_annotation)])
    else:
        output_dict["strings"] = []
        for document in adc.documents:
            output_dict["strings"].append(delimiter.join([t[1] for t in document.get_annotations_with_text(feature_annotation)]))

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


def extract_feature(input_dict):
    """
    Extract documents features.

    :param adc
    :param feature_name
    :return extracted features (list)
    """

    extracted_features = []
    for document in input_dict["adc"].documents:
        extracted_features.append(document.features.get(input_dict["feature_name"], None))

    return {"strings": extracted_features}


def add_feature(input_dict):
    """
    Add a feature to Annotated Document Corpus.

    :param adc: Annotated Document Corpus
    :param feature_name: the name of new feature
    :param feature_values: list of features values
    :param feature_value_prefix:  prefix to feature value

    :return: new adc
    """

    for i, document in enumerate(input_dict["adc"].documents):
        document.features[input_dict[u"feature_name"]] = input_dict[u"feature_value_prefix"] + str(input_dict[u"feature_values"][i])
    return {"adc":input_dict["adc"]}


def split_documents_by_feature_value(input_dict):
    """

    Split Annotated Document Corpus by conditions with features and values.

    :param adc: Annotated Document Corpus
    :param feature_condition: split condition.
    :param discard_filtered_out default-false: discard documents that do not fulfil given condition

    :return adc_filtered: adc with documents that fulfil the condition
    :return adc_rest: adc with documents that do not fulfil the condtion
    """
    discard_filtered_out = input_dict["discard_filtered_out"] == u"true"
    adc_filtered, adc_rest = DocumentCorpus("", ""), input_dict["adc"]

    if input_dict["feature_condition"] != u'':
        feature_conditions = [el.strip().split("=") for el in re.split("[;|,]",input_dict["feature_condition"])]
        for i in range(len(feature_conditions)):
            if len(feature_conditions[i]) != 2:
                raise Exception("Feature condition should be specified like: feature1 = value1, feature2 = value2 etc.")
            feature, value = feature_conditions[i]
            feature_conditions[i] = [feature.strip(), value.strip()]

        included = []
        discarded = []
        for i, document in enumerate(input_dict["adc"].documents):
            if all([document.features.get(feature, "") == value for feature, value in feature_conditions]):
                included.append(i)
            else:
                discarded.append(i)

        adc_filtered, adc_rest = input_dict["adc"].split(included, discarded)

    if discard_filtered_out:
        return {"adc_filtered":adc_filtered, "adc_rest": DocumentCorpus("", "")}
    else:
        return {"adc_filtered": adc_filtered, "adc_rest": adc_rest}


def extract_documents(input_dict):
    """
    Extract documents, given document indices, from Annotated Document Corpus.

    :param adc: Annotated Document Corpus
    :param index_list: list of document ids to include
    :param discard_filtered_out default-false: discard documents that are not included in index_list

    :return adc_filtered: adc with documents that fulfil the condition
    :return adc_rest: adc with documents that do not fulfil the condtion
    """

    discard_filtered_out = input_dict["discard_filtered_out"] == u"true"
    included = input_dict["index_list"]

    for i in included:
        if i < 0 or i >= len(input_dict["adc"].documents) or type(i) != int:
            raise Exception("Document indices are set incorrectly.")
    discarded = [i for i in range(len(input_dict["adc"].documents)) if i not in input_dict["index_list"]]
    adc_filtered, adc_rest = input_dict["adc"].split(included, discarded)

    if discard_filtered_out:
        return {"adc_filtered":adc_filtered, "adc_rest": DocumentCorpus("", "")}
    else:
        return {"adc_filtered": adc_filtered, "adc_rest": adc_rest}


def merge_corpora(input_dict):
    """

    Merge multiple Annotated Document Corpuses into one.

    :param adc: list of Annotated Document Corpuses
    :return: Annotated Document Corpus
    """

    adc = input_dict["adc"][0]
    adc.features["SourceDate"] = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
    adc.features["CorpusCreateDate"] = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))

    for i in range(1, len(input_dict["adc"])):
        for document in input_dict["adc"][i].documents:
            adc.documents.append(document)

    return {"adc": adc}

def display_document_corpus(input_dict):
    #implemented in visualization_views.py
    return {}
