def construct_bow_space(inputDict): #TODO
    _adc = ToNetObj(inputDict['adc'])
    _tokenId = ToString(inputDict['tokenId'])
    _stemId = ToString(inputDict['stemId'])
    _stopwordId = ToString(inputDict['stopwordId'])
    _labelId = ToString(inputDict['labelId'])
    _maxNGramLen = ToInt(inputDict['maxNGramLen'])
    _minWordFreq = ToInt(inputDict['minWordFreq'])
    _wordWeightType = ToEnum(Latino.TextMining.WordWeightType, inputDict['wordWeightType'], Latino.TextMining.WordWeightType.TfIdf)
    _cutLowWeightsPerc = ToFloat(inputDict['cutLowWeightsPerc'])
    _normalizeVectors = ToBool(inputDict['normalizeVectors'])
    execResult = LatinoCF.ConstructBowSpace(_adc, _tokenId, _stemId, _stopwordId, _labelId, _maxNGramLen, _minWordFreq, _wordWeightType, _cutLowWeightsPerc, _normalizeVectors)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['bow'] = execResultPy['bow']
    outputDict['ds'] = execResultPy['ds']
    return outputDict