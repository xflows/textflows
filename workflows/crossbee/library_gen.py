# -----------------------------------------------------------------------------------------------------
# WARNING: THIS IS AUTOMATICALLY GENERATED FILE, DO NOT EDIT IT MANUALLY AS YOU MAY LOOSE YOUR CHANGES!
# -----------------------------------------------------------------------------------------------------

from workflows.textflows_dot_net.import_dotnet import *
from workflows.textflows_dot_net.serialization_utils import *

def crossbee_construct_standard_heurisitc(inputDict):
    _name = ToString(inputDict['name'])
    _heurisitc_spec = ToEnum(CrossBeeInterfaces.Heurisitcs.StandardHeurisitc.Specification, inputDict['heurisitc_spec'], CrossBeeInterfaces.Heurisitcs.StandardHeurisitc.Specification.random)
    execResult = CrossBeeIntf.ConstructStandardHeurisitc(_name, _heurisitc_spec)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['heurisitc'] = execResultPy
    return outputDict

def crossbee_construct_all_standard_heurisitc(inputDict):
    execResult = CrossBeeIntf.ConstructAllStandardHeurisitc()
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['heurisitcs'] = execResultPy
    return outputDict

def crossbee_construct_outlier_heuristics(inputDict):
    _name = ToString(inputDict['name'])
    _relative = ToBool(inputDict['relative'])
    _outlier_document_indexes = ToNetObj(inputDict['outlier_document_indexes'])
    execResult = CrossBeeIntf.ConstructOutlierHeuristics(_name, _relative, _outlier_document_indexes)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['new_heurisitcs'] = execResultPy
    return outputDict

def crossbee_construct_calculated_heuristics(inputDict):
    _name = ToString(inputDict['name'])
    _calc = ToEnum(CrossBeeInterfaces.Heurisitcs.CalculatedHeustistic.Calculation, inputDict['calc'], CrossBeeInterfaces.Heurisitcs.CalculatedHeustistic.Calculation.Sum)
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.ConstructCalculatedHeuristics(_name, _calc, _heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['new_heurisitcs'] = execResultPy
    return outputDict

def crossbee_construct_ensemble_heuristics(inputDict):
    _name = ToString(inputDict['name'])
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.ConstructEnsembleHeuristics(_name, _heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['new_heurisitcs'] = execResultPy
    return outputDict

def crossbee_combine_heuristics(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.CombineHeuristics(_heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['new_heurisitcs'] = execResultPy
    return outputDict

def crossbee_get_heuristic_names(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.GetHeuristicNames(_heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['names'] = execResultPy
    return outputDict

def crossbee_get_heuristic_structure(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.GetHeuristicStructure(_heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['structure'] = execResultPy
    return outputDict

def crossbee_load_outlier_heuristics(inputDict):
    _name_prefix = ToString(inputDict['name_prefix'])
    _specification = ToString(inputDict['specification'])
    _relative = ToBool(inputDict['relative'])
    execResult = CrossBeeIntf.LoadOutlierHeuristics(_name_prefix, _specification, _relative)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['new_heurisitcs'] = execResultPy
    return outputDict

def crossbee_outlier_heuristics_spec(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.OutlierHeuristicsSpec(_heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['specification'] = execResultPy
    return outputDict

def crossbee_outlier_detection_via_cross_validation(inputDict):
    _csf = ToNetObj(inputDict['csf'])
    _ds = ToNetObj(inputDict['ds'])
    _repetition_count = ToInt(inputDict['repetition_count'])
    _outlier_threshold = ToInt(inputDict['outlier_threshold'])
    _num_of_sets = ToInt(inputDict['num_of_sets'])
    _random = ToBool(inputDict['random'])
    _use_seed = ToBool(inputDict['use_seed'])
    _random_seed = ToInt(inputDict['random_seed'])
    _outlier_weighting = ToEnum(CrossBeeInterfaces.CrossBeeIntf.OutlierWeighting, inputDict['outlier_weighting'], CrossBeeInterfaces.CrossBeeIntf.OutlierWeighting.RelativePercentage)
    execResult = CrossBeeIntf.OutlierDetectionViaCrossValidation(_csf, _ds, _repetition_count, _outlier_threshold, _num_of_sets, _random, _use_seed, _random_seed, _outlier_weighting)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['out'] = execResultPy
    return outputDict

def crossbee_apply_heurisitcs(inputDict):
    _term_dataset = ToNetObj(inputDict['term_dataset'])
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.ApplyHeurisitcs(_term_dataset, _heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['heur'] = execResultPy
    return outputDict

def crossbee_select_heuristics(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.SelectHeuristics(_heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['heuristics'] = execResultPy
    return outputDict

def crossbee_rank_terms(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    execResult = CrossBeeIntf.RankTerms(_heuristics)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['table'] = execResultPy
    return outputDict

def crossbee_explore_in_crossbee(inputDict):
    _parsed_doc = ToNetObj(inputDict['parsed_doc'])
    _heuristics = ToNetObj(inputDict['heuristics'])
    _bterms = ToNetObj(inputDict['bterms'])
    execResult = CrossBeeIntf.ExploreInCrossbee(_parsed_doc, _heuristics, _bterms)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    return outputDict

def crossbee_get_roc_curves(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    _bterms = ToNetObj(inputDict['bterms'])
    execResult = CrossBeeIntf.GetRocCurves(_heuristics, _bterms)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['roc'] = execResultPy
    return outputDict

def crossbee_display_roc_curves(inputDict):
    _roc = ToNetObj(inputDict['roc'])
    execResult = CrossBeeIntf.DisplayRocCurves(_roc)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    return outputDict

def crossbee_get_performance_measures(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    _bterms = ToNetObj(inputDict['bterms'])
    execResult = CrossBeeIntf.GetPerformanceMeasures(_heuristics, _bterms)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['perf'] = execResultPy
    return outputDict

def crossbee_get_viper_measures(inputDict):
    _heuristics = ToNetObj(inputDict['heuristics'])
    _bterms = ToNetObj(inputDict['bterms'])
    execResult = CrossBeeIntf.GetViperMeasures(_heuristics, _bterms)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['perf'] = execResultPy
    return outputDict

