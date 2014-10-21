def stopword_tagger_hub(inputDict): #TODO
    _adc = ToNetObj(inputDict['adc'])
    _tagger = ToNetObj(inputDict['tagger'])
    _elementAnnotation = ToString(inputDict['elementAnnotation'])
    _outputFeature = ToString(inputDict['outputFeature'])
    execResult = LatinoCF.TagADCStopwords(_adc, _tagger, _elementAnnotation, _outputFeature)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict