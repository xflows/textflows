from workflows.textflows import BowDataset,BowModelConstructor


def construct_bow_model_constructor(input_dict):
    adc=input_dict['adc']
    token_annotation = input_dict['token_annotation']
    stem_feature_name = input_dict['stem_feature_name']

    if stem_feature_name:
        token_annotation+='/'+stem_feature_name

    args={  'adc': adc,
            'token_annotation': token_annotation,
            'stem_feature_name':stem_feature_name,
            'stop_word_feature_name': input_dict['stop_word_feature_name'],
            'label_doc_feature_name': input_dict['label_doc_feature_name'],
            'weighting_type':input_dict['word_weight_type'], #tf_idf
            'normalize_vectors': input_dict['normalize_vectors']=='true', #true
            'max_ngram': int(input_dict['max_ngram_len']), #2
            'min_tf': int(input_dict['min_word_freq']),#5
            'predefined_vocabulary': input_dict.get('vocabulary',None)}

    bow_model=BowModelConstructor(**args)

    return {'bow_model_constructor': bow_model}

def construct_dataset_and_bow_model_constructor(input_dict):
    """
    In TextFlows the Construct BoW Dataset and BoW Model Constructor widget takes as an input an ADC data object
    and generates a sparse BoW model dataset (which can be then handed to i.e. a classifier). The widget takes as an
    input also several user defined parameters, which are taken into account when building the feature dataset:

    :param Token Annotation: This is the type of Annotation instances, which mark parts of the document (e.g., words, sentences or a terms), which will be used for generating the vocabulary and the dataset.
    :param Feature Name: If present, the model will be constructed out of annotations' feature values instead of document text. For example, this is useful when we wish build the BoW model using stems instead of the original word forms.
    :param Stop Word Feature Name: This is an annotation feature name which was used to tag tokens as stop words. These tokens will be excluded from the BoW representational model. If blank, no stop words will be used.
    :param Label Document Feature Name: This is the name of the document feature which will be used for class labeling examples in the dataset. If blank, the generated sparse dataset will be unlabeled.
    :param Maximum n-gram Length: The upper boundary of the range of n-values for different n-grams to be extracted. All values of $n$ such that $1 \leq n \leq \mbox{max\_ngram$ will be used.
    :param Minimum Word Frequency: When building the vocabulary ignore terms that have a term frequency strictly lower than the given threshold. This value is also called cut-off in the literature.
    :param Word Weighting Type: The user can select among various weighting models for assigning weights to features:

        Binary. A feature weight is 1 if the corresponding term is present in the document, or zero otherwise.
        Term occurrence. A feature weight is equal to the number of occurrences of the corresponding term. This weight might be sometimes better than a simple binary value since frequently occurring term are likely to be more relevant to the given text.
        Term frequency. A weight is derived from the term occurrence by dividing the vector by the sum of all vector's weights. The reasoning is similar to term occurrence, with normalization with respect to document size.
        TF-IDF. Term Frequency-Inverse Document Frequency~\citep{salton1988term is the most common scheme for weighting features. For a given term $w$ in document $d$ from corpus $D$, the TF-IDF measure is defined as follows:
        Safe TF-IDF. For a given term $w$ in document $d$ from corpus $D$, the Safe TF-IDF measure is defined as follows:
        TF-IDF with sublinear TF scaling. It often seems unlikely that twenty occurrences of a term in a document truly carry twenty times the significance of a single occurrence. Accordingly, there has been considerable research into variants of term frequency that go beyond counting the number of occurrences of a term~\citep{paltoglou2010study. A common modification is to use the logarithm of the term frequency instead of tf, defined as:

    :param Normalize Vectors: The weighting methods can be further modified by vector normalization. If the user opts to use it in TextFlows the $L2$ regularization~\citep{ng2004feature is performed.

    :return:  Besides the sparse BoW model dataset the Construct BoW Dataset and BoW Model Constructor also outputs
     a BowModelConstructor instance. This additional object contains settings which allow repetition of the feature
     construction steps on another document corpus. These settings include the inputted parameters, as well as the
     learned term weights and vocabulary.

    """

    adc=input_dict['adc']

    bow_model=construct_bow_model_constructor(input_dict)['bow_model_constructor']
    bow_dataset=BowDataset.from_adc(adc,bow_model)

    return {'bow_model_constructor': bow_model,'bow_dataset': bow_dataset}

def create_dataset_using_bow_model_constructor(input_dict):
    bow_model = input_dict['bow_model_constructor']
    adc = input_dict['adc']

    return {'bow_dataset': BowDataset.from_adc(adc,bow_model)}