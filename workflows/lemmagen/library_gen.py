# -----------------------------------------------------------------------------------------------------
# WARNING: THIS IS AUTOMATICALLY GENERATED FILE, DO NOT EDIT IT MANUALLY AS YOU MAY LOOSE YOUR CHANGES!
# -----------------------------------------------------------------------------------------------------

from workflows.textflows_dot_net.import_dotnet import *
from workflows.textflows_dot_net.serialization_utils import *

def lemmagen_load_example_list_from_string(inputDict):
    _tab_delim = ToString(inputDict['tab_delim'])
    _format = ToString(inputDict['format'])
    execResult = LemmaSharpIntf.LoadExampleListFromString(_tab_delim, _format)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['example_list'] = execResultPy
    return outputDict

def lemmagen_load_example_list_from_table(inputDict):
    _table = ToNetObj(inputDict['table'])
    _format = ToString(inputDict['format'])
    execResult = LemmaSharpIntf.LoadExampleListFromTable(_table, _format)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['example_list'] = execResultPy
    return outputDict

def lemmagen_example_list_to_table(inputDict):
    _example_list = ToNetObj(inputDict['example_list'])
    execResult = LemmaSharpIntf.ExampleListToTable(_example_list)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['table'] = execResultPy
    return outputDict

def lemmagen_save_lemmatizer(inputDict):
    _lmtz = ToNetObj(inputDict['lmtz'])
    execResult = LemmaSharpIntf.SaveLemmatizer(_lmtz)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['obj_string'] = execResultPy
    return outputDict

def lemmagen_load_net_lemmatizer(inputDict):
    _lmtz_str = ToString(inputDict['lmtz_str'])
    execResult = LemmaSharpIntf.LoadNetLemmatizer(_lmtz_str)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['obj'] = execResultPy
    return outputDict

def lemmagen_group_examples(inputDict):
    _example_list = ToNetObj(inputDict['example_list'])
    _ignore_frequencies = ToBool(inputDict['ignore_frequencies'])
    _msd_consider = ToEnum(LemmaSharp.LemmatizerSettings.MsdConsideration, inputDict['msd_consider'], LemmaSharp.LemmatizerSettings.MsdConsideration.Distinct)
    execResult = LemmaSharpIntf.GroupExamples(_example_list, _ignore_frequencies, _msd_consider)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['example_list'] = execResultPy
    return outputDict

def lemmagen_construct_lemmatizer_settings(inputDict):
    _use_from_in_rules = ToBool(inputDict['use_from_in_rules'])
    _msd_consider = ToEnum(LemmaSharp.LemmatizerSettings.MsdConsideration, inputDict['msd_consider'], LemmaSharp.LemmatizerSettings.MsdConsideration.Distinct)
    _max_rules_per_node = ToInt(inputDict['max_rules_per_node'])
    _build_front_lemmatizer = ToBool(inputDict['build_front_lemmatizer'])
    _store_all_full_known_words = ToBool(inputDict['store_all_full_known_words'])
    execResult = LemmaSharpIntf.ConstructLemmatizerSettings(_use_from_in_rules, _msd_consider, _max_rules_per_node, _build_front_lemmatizer, _store_all_full_known_words)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['lemmatizer_settings'] = execResultPy
    return outputDict

def lemmagen_extract_lemmatizer_settings(inputDict):
    _lmtz = ToNetObj(inputDict['lmtz'])
    execResult = LemmaSharpIntf.ExtractLemmatizerSettings(_lmtz)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['lemmatizer_settings'] = execResultPy
    return outputDict

def lemmagen_construct_prebuild_lemmatizer(inputDict):
    _language = ToEnum(LemmaSharp.LanguagePrebuilt, inputDict['language'], LemmaSharp.LanguagePrebuilt.English)
    execResult = LemmaSharpIntf.ConstructPrebuildLemmatizer(_language)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['lemamtizer'] = execResultPy
    return outputDict

def lemmagen_construct_lemmatizer(inputDict):
    _lemmatizer_settings = ToNetObj(inputDict['lemmatizer_settings'])
    _example_list = ToNetObj(inputDict['example_list'])
    execResult = LemmaSharpIntf.ConstructLemmatizer(_lemmatizer_settings, _example_list)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['lemmatizer'] = execResultPy
    return outputDict

def lemmagen_display_lemmatization_rules(inputDict):
    _lmtz = ToNetObj(inputDict['lmtz'])
    execResult = LemmaSharpIntf.DisplayLemmatizationRules(_lmtz)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['lmtz_tree'] = execResultPy
    return outputDict

def lemmagen_lemmatize_words(inputDict):
    _lemmatizer = ToNetObj(inputDict['lemmatizer'])
    _words = ToNetObj(inputDict['words'])
    _leave_word = ToBool(inputDict['leave_word'])
    _ignore_case = ToBool(inputDict['ignore_case'])
    _msd = ToString(inputDict['msd'])
    execResult = LemmaSharpIntf.LemmatizeWords(_lemmatizer, _words, _leave_word, _ignore_case, _msd)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['lemmas'] = execResultPy
    return outputDict

def lemmagen_lemmatize_explain_words(inputDict):
    _lemmatizer = ToNetObj(inputDict['lemmatizer'])
    _words = ToNetObj(inputDict['words'])
    _ignore_case = ToBool(inputDict['ignore_case'])
    _msd = ToString(inputDict['msd'])
    execResult = LemmaSharpIntf.LemmatizeExplainWords(_lemmatizer, _words, _ignore_case, _msd)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['explanations'] = execResultPy
    return outputDict

def lemmagen_delimited_file2_table(inputDict):
    _file = ToString(inputDict['file'])
    _delimiter = ToString(inputDict['delimiter'])
    _first_line_is_header = ToBool(inputDict['first_line_is_header'])
    _header_line = ToString(inputDict['header_line'])
    _skip_empty_lines = ToBool(inputDict['skip_empty_lines'])
    execResult = LemmaSharpIntf.DelimitedFile2Table(_file, _delimiter, _first_line_is_header, _header_line, _skip_empty_lines)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['table'] = execResultPy
    return outputDict

def lemmagen_delimited_string2_table(inputDict):
    _examples_text = ToString(inputDict['examples_text'])
    _delimiter = ToString(inputDict['delimiter'])
    _first_line_is_header = ToBool(inputDict['first_line_is_header'])
    _header_line = ToString(inputDict['header_line'])
    _skip_empty_lines = ToBool(inputDict['skip_empty_lines'])
    execResult = LemmaSharpIntf.DelimitedString2Table(_examples_text, _delimiter, _first_line_is_header, _header_line, _skip_empty_lines)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['table'] = execResultPy
    return outputDict

def lemmagen_filter_table_rows(inputDict):
    _table = ToNetObj(inputDict['table'])
    _index_list = ToNetObj(inputDict['index_list'])
    _discard_filtered_out = ToBool(inputDict['discard_filtered_out'])
    execResult = LemmaSharpIntf.FilterTableRows(_table, _index_list, _discard_filtered_out)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['table_selected'] = execResultPy['tableSelected']
    outputDict['table_filtered'] = execResultPy['tableFiltered']
    return outputDict

def lemmagen_extract_column_as_list(inputDict):
    _table = ToNetObj(inputDict['table'])
    _column_index = ToInt(inputDict['column_index'])
    execResult = LemmaSharpIntf.ExtractColumnAsList(_table, _column_index)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['column_values'] = execResultPy['columnValues']
    outputDict['column_name'] = execResultPy['columnName']
    return outputDict

def lemmagen_insert_list_as_column(inputDict):
    _table = ToNetObj(inputDict['table'])
    _column_index = ToInt(inputDict['column_index'])
    _column_values = ToNetObj(inputDict['column_values'])
    _column_name = ToString(inputDict['column_name'])
    execResult = LemmaSharpIntf.InsertListAsColumn(_table, _column_index, _column_values, _column_name)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['table'] = execResultPy
    return outputDict

def lemmagen_table2_string_delimited(inputDict):
    _table = ToNetObj(inputDict['table'])
    _delimiter = ToString(inputDict['delimiter'])
    _output_header = ToBool(inputDict['output_header'])
    execResult = LemmaSharpIntf.Table2StringDelimited(_table, _delimiter, _output_header)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['string'] = execResultPy
    return outputDict

def lemmagen_get_set_indexes(inputDict):
    _selected_set_id = ToInt(inputDict['selected_set_id'])
    _set_list = ToNetObj(inputDict['set_list'])
    _opposite = ToBool(inputDict['opposite'])
    execResult = LemmaSharpIntf.GetSetIndexes(_selected_set_id, _set_list, _opposite)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['set_indexes'] = execResultPy
    return outputDict

def lemmagen_filter_list_elements(inputDict):
    _list = ToNetObj(inputDict['list'])
    _index_list = ToNetObj(inputDict['index_list'])
    _discard_filtered_out = ToBool(inputDict['discard_filtered_out'])
    execResult = LemmaSharpIntf.FilterListElements(_list, _index_list, _discard_filtered_out)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['list_selected'] = execResultPy['listSelected']
    outputDict['list_filtered'] = execResultPy['listFiltered']
    return outputDict

def lemmagen_save_net_object(inputDict):
    _serializable_object = ToNetObj(inputDict['serializable_object'])
    _compress = ToBool(inputDict['compress'])
    execResult = LemmaSharpIntf.SaveNetObject(_serializable_object, _compress)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['obj_string'] = execResultPy
    return outputDict

def lemmagen_load_net_object(inputDict):
    _serializable_object_str = ToString(inputDict['serializable_object_str'])
    _compress = ToBool(inputDict['compress'])
    execResult = LemmaSharpIntf.LoadNetObject(_serializable_object_str, _compress)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['obj'] = execResultPy
    return outputDict

