from workflows.textflows import BowDataset,BowModel


def construct_dataset_and_bow_model_constructor(input_dict): #TODO
    # _wordWeightType = ToEnum(Latino.TextMining.WordWeightType, inputDict['wordWeightType'], Latino.TextMining.WordWeightType.TfIdf)
    # _cutLowWeightsPerc = ToFloat(inputDict['cutLowWeightsPerc'])
    # _normalizeVectors = ToBool(inputDict['normalizeVectors'])
    # _tokenId = ToString(inputDict['tokenId'])

    # _labelId = ToString(inputDict['labelId'])
    # _maxNGramLen = ToInt(inputDict['maxNGramLen'])
    # _minWordFreq = ToInt(inputDict['minWordFreq'])
    # _wordWeightType = ToEnum(Latino.TextMining.WordWeightType, inputDict['wordWeightType'], Latino.TextMining.WordWeightType.TfIdf)
    # _cutLowWeightsPerc = ToFloat(inputDict['cutLowWeightsPerc'])
    # _normalizeVectors = ToBool(inputDict['normalizeVectors'])
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
            'vocabulary': input_dict.get('vocabulary',None)}

    bow_model=BowModel(**args)
    bow_dataset=BowDataset.from_adc(adc,bow_model)

    return {'bow_model_constructor': bow_model,'bow_dataset': bow_dataset}

def create_dataset_using_bow_model_constructor(input_dict):
    bow_model = input_dict['bow_model_constructor']
    adc = input_dict['adc']

    return {'bow_dataset': BowDataset.from_adc(adc,bow_model)}