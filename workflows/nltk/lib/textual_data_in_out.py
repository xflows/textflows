def load_adc(inputDict): #TODO
    _file = ToString(inputDict['file'])
    _tabSeparatedTitle = ToBool(inputDict['tabSeparatedTitle'])
    _leadingLabels = ToBool(inputDict['leadingLabels'])
    execResult = LatinoCF.LoadADC(_file, _tabSeparatedTitle, _leadingLabels)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict