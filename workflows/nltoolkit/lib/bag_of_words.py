from workflows.textflows import BowDataset,BowModel


def construct_bow_model(inputDict): #TODO
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

    adc = inputDict['adc']

    token_annotation = inputDict['token_annotation']
    stem_feature_name = inputDict['stem_feature_name']

    if stem_feature_name:
        token_annotation+='/'+stem_feature_name

    stop_word_feature_name = inputDict['stop_word_feature_name']
    label_doc_feature_name=inputDict['label_doc_feature_name']

    docs= [document.raw_text(token_annotation,stop_word_feature_name) for document in adc.documents]
    labels=[doc.features.get(label_doc_feature_name,'') for doc in adc.documents] if label_doc_feature_name else None
    bow_model=BowModel(docs)
    bow_dataset=BowDataset.from_raw_documents(docs,bow_model.vectorizer,labels)


    return {'bow_model': bow_model,'bow_dataset': bow_dataset}