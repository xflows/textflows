from workflows.textflows import BowDataset,BowModel


def construct_bow_model(input_dict): #TODO
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

    adc = input_dict['adc']

    token_annotation = input_dict['token_annotation']
    stem_feature_name = input_dict['stem_feature_name']

    if stem_feature_name:
        token_annotation+='/'+stem_feature_name

    stop_word_feature_name = input_dict['stop_word_feature_name']
    label_doc_feature_name=input_dict['label_doc_feature_name']

    #docs= [document.raw_text(token_annotation,stop_word_feature_name) for document in adc.documents]

    bow_model=BowModel(adc,token_annotation,stem_feature_name,stop_word_feature_name,label_doc_feature_name)
    bow_dataset=BowDataset.from_adc(adc,bow_model)

    return {'bow_model': bow_model,'bow_dataset': bow_dataset}

def create_dataset_with_bow_model(input_dict):
    bow_model = input_dict['bow_model']
    adc = input_dict['adc']

    return {'bow_dataset': BowDataset.from_adc(adc,bow_model)}
