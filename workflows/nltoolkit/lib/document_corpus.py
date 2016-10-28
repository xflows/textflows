import copy
from workflows.textflows import NltkCorpus
import time
import re


def nltk_corpus(input_dict):
    """Returns the nltk.corpus for the selected corpus name"""
    return {'corpus': {'corpus': NltkCorpus(input_dict['corpus_name']), 'chunk': input_dict['chunk']}}


def extract_nltk_corpus_name(input_dict):
    chunk = input_dict['training_corpus']['chunk']
    corpus = input_dict['training_corpus']['corpus']
    name = "NLTK corpus " + str(chunk)
    match = re.search(r"(\\\\|/)(\w+)'", str(corpus))
    if match:
        name = match.group(2) + " " + str(chunk)
    return {'name': name}


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


def add_computed_document_features(input_dict):
    """
    TODO: Add a feature to Annotated Document Corpus.

    :param adc: Annotated Document Corpus
    :param feature_name: the name of new feature
    :param feature_computation: "New Feature Computatation
    :param feature_spec: Comma separated list of names of old features used in the 'New Feature Computataion'.

    :return: new adc
    """

    adc=input_dict["adc"]
    compute_new_features(adc.documents,input_dict["feature_name"],input_dict["feature_computation"])

    return {"adc":adc}

def add_computed_token_features(input_dict):
    """
    TODO

    :param adc: Annotated Document Corpus
    :param feature_name: the name of new feature
    :param feature_computation: "New Feature Computatation
    :param feature_spec: Comma separated list of names of old features used in the 'New Feature Computataion'.

    :return: new adc
    """

    adc=input_dict["adc"]
    for document in adc.documents:
        compute_new_features(document.get_annotations(input_dict["annotation_name"]),input_dict["feature_name"],input_dict["feature_computation"])

    return {"adc":adc}

def compute_new_features(objs,new_feature_name,feature_computation):
    features = re.findall(r"\{([\w\s]+)\}", feature_computation) #[mm.split(':')[0] for mm in m.groups()]
    for obj in objs:
        new_feature_value=copy.copy(feature_computation)
        for feature in features:
            new_feature_value=new_feature_value.replace("{"+feature+"}",obj.features.get(feature, "NULL"))
        obj.features[new_feature_name]=new_feature_value


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
    adc_filtered, adc_rest = None, input_dict["adc"]

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

        adc_filtered, adc_rest = input_dict["adc"].split(included, None if discard_filtered_out else discarded)

    if discard_filtered_out:
        return {"adc_filtered":adc_filtered, "adc_rest": None}
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
    adc_filtered, adc_rest = input_dict["adc"].split(included, None if discard_filtered_out else discarded)

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


def extract_adc_name(input_dict):
    return {'y_name' : input_dict['adc'].features['Source']}

