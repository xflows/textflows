# -----------------------------------------------------------------------------------------------------
# WARNING: THIS IS AUTOMATICALLY GENERATED FILE, DO NOT EDIT IT MANUALLY AS YOU MAY LOOSE YOUR CHANGES!
# -----------------------------------------------------------------------------------------------------

from workflows.textflows_dot_net.import_dotnet import *
from workflows.textflows_dot_net.serialization_utils import *

import Latino
import LatinoInterfaces
from LatinoInterfaces import LatinoCF

def latino_flatten_object_to_string_array(inputDict):
    _data = ToNetObj(inputDict['data'])
    execResult = LatinoCF.FlattenObjectToStringArray(_data)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['flat_data'] = execResultPy
    return outputDict

def latino_generate_integer_range(inputDict):
    _start = ToInt(inputDict['start'])
    _stop = ToInt(inputDict['stop'])
    _step = ToInt(inputDict['step'])
    execResult = LatinoCF.GenerateIntegerRange(_start, _stop, _step)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['range'] = execResultPy
    return outputDict

def latino_load_adc(inputDict):
    _file = ToString(inputDict['file'])
    _tab_separated_title = ToBool(inputDict['tab_separated_title'])
    _leading_labels = ToBool(inputDict['leading_labels'])
    execResult = LatinoCF.LoadADC(_file, _tab_separated_title, _leading_labels)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_load_adc_from_string(inputDict):
    _plain_string = ToString(inputDict['plain_string'])
    _tab_separated_title = ToBool(inputDict['tab_separated_title'])
    _leading_labels = ToBool(inputDict['leading_labels'])
    execResult = LatinoCF.LoadADCFromString(_plain_string, _tab_separated_title, _leading_labels)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_save_adc_to_xml(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    execResult = LatinoCF.SaveADCToXml(_adc)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['string'] = execResultPy
    return outputDict

def latino_load_adc_from_xml(inputDict):
    _xml = ToString(inputDict['xml'])
    execResult = LatinoCF.LoadADCFromXml(_xml)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_get_doc_strings(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _element_annotation = ToString(inputDict['element_annotation'])
    _element_feature_conditions = ToString(inputDict['element_feature_conditions'])
    _delimiter = ToString(inputDict['delimiter'])
    _include_doc_id = ToBool(inputDict['include_doc_id'])
    execResult = LatinoCF.GetDocStrings(_adc, _element_annotation, _element_feature_conditions, _delimiter, _include_doc_id)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['strings'] = execResultPy
    return outputDict

def latino_extract_documents_features(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _feature_name = ToString(inputDict['feature_name'])
    execResult = LatinoCF.ExtractDocumentsFeatures(_adc, _feature_name)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['strings'] = execResultPy
    return outputDict

def latino_add_documents_features(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _feature_values = ToNetObj(inputDict['feature_values'])
    _feature_name = ToString(inputDict['feature_name'])
    _feature_value_prefix = ToString(inputDict['feature_value_prefix'])
    execResult = LatinoCF.AddDocumentsFeatures(_adc, _feature_values, _feature_name, _feature_value_prefix)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_add_computed_features(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _feature_name = ToString(inputDict['feature_name'])
    _feature_computataion = ToString(inputDict['feature_computataion'])
    _feature_spec = ToString(inputDict['feature_spec'])
    execResult = LatinoCF.AddComputedFeatures(_adc, _feature_name, _feature_computataion, _feature_spec)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_split_documents_by_feature_value(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _feature_condition = ToString(inputDict['feature_condition'])
    _discard_filtered_out = ToBool(inputDict['discard_filtered_out'])
    execResult = LatinoCF.SplitDocumentsByFeatureValue(_adc, _feature_condition, _discard_filtered_out)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc_filtered'] = execResultPy['adcFiltered']
    outputDict['adc_rest'] = execResultPy['adcRest']
    return outputDict

def latino_extract_documents(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _index_list = ToNetObj(inputDict['index_list'])
    _discard_filtered_out = ToBool(inputDict['discard_filtered_out'])
    execResult = LatinoCF.ExtractDocuments(_adc, _index_list, _discard_filtered_out)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc_filtered'] = execResultPy['adcFiltered']
    outputDict['adc_rest'] = execResultPy['adcRest']
    return outputDict

def latino_join_documents_corpora(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    execResult = LatinoCF.JoinDocumentsCorpora(_adc)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_mark_documents_with_set_feature(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _feature_name = ToString(inputDict['feature_name'])
    _feature_value_prefix = ToString(inputDict['feature_value_prefix'])
    _num_of_sets = ToInt(inputDict['num_of_sets'])
    _random = ToBool(inputDict['random'])
    _use_seed = ToBool(inputDict['use_seed'])
    _random_seed = ToInt(inputDict['random_seed'])
    execResult = LatinoCF.MarkDocumentsWithSetFeature(_adc, _feature_name, _feature_value_prefix, _num_of_sets, _random, _use_seed, _random_seed)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_corpus_statistics(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    execResult = LatinoCF.CorpusStatistics(_adc)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['doc_count'] = execResultPy['docCount']
    outputDict['feature_count'] = execResultPy['featureCount']
    outputDict['description'] = execResultPy['description']
    return outputDict

def latino_random_cross_validation_sets(inputDict):
    _num_of_sets = ToInt(inputDict['num_of_sets'])
    _num_of_examples = ToInt(inputDict['num_of_examples'])
    _random = ToBool(inputDict['random'])
    _use_seed = ToBool(inputDict['use_seed'])
    _random_seed = ToInt(inputDict['random_seed'])
    _examples = ToNetObj(inputDict['examples'])
    execResult = LatinoCF.RandomCrossValidationSets(_num_of_sets, _num_of_examples, _random, _use_seed, _random_seed, _examples)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['example_set_id'] = execResultPy
    return outputDict

def latino_random_sequential_validation_sets(inputDict):
    _num_of_sets = ToInt(inputDict['num_of_sets'])
    _num_of_examples = ToInt(inputDict['num_of_examples'])
    _random = ToBool(inputDict['random'])
    _use_seed = ToBool(inputDict['use_seed'])
    _random_seed = ToInt(inputDict['random_seed'])
    _train_size = ToString(inputDict['train_size'])
    _test_size = ToString(inputDict['test_size'])
    _train_test_delay = ToString(inputDict['train_test_delay'])
    _examples = ToNetObj(inputDict['examples'])
    execResult = LatinoCF.RandomSequentialValidationSets(_num_of_sets, _num_of_examples, _random, _use_seed, _random_seed, _train_size, _test_size, _train_test_delay, _examples)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['dict'] = execResultPy
    return outputDict

def latino_get_multi_set_indexes(inputDict):
    _sets = ToNetObj(inputDict['sets'])
    execResult = LatinoCF.GetMultiSetIndexes(_sets)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['dict'] = execResultPy
    return outputDict

def latino_construct_english_maximum_entropy_sentence_detector(inputDict):
    execResult = LatinoCF.ConstructEnglishMaximumEntropySentenceDetector()
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tokenizer'] = execResultPy
    return outputDict

def latino_construct_english_maximum_entropy_tokenizer(inputDict):
    _alpha_numeric_optimization = ToBool(inputDict['alpha_numeric_optimization'])
    execResult = LatinoCF.ConstructEnglishMaximumEntropyTokenizer(_alpha_numeric_optimization)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tokenizer'] = execResultPy
    return outputDict

def latino_construct_unicode_tokenizer(inputDict):
    _filter = ToEnum(Latino.TextMining.TokenizerFilter, inputDict['filter'], Latino.TextMining.TokenizerFilter.None)
    _min_token_len = ToInt(inputDict['min_token_len'])
    execResult = LatinoCF.ConstructUnicodeTokenizer(_filter, _min_token_len)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tokenizer'] = execResultPy
    return outputDict

def latino_construct_simple_tokenizer(inputDict):
    _type = ToEnum(Latino.TextMining.TokenizerType, inputDict['type'], Latino.TextMining.TokenizerType.AllChars)
    _min_token_len = ToInt(inputDict['min_token_len'])
    execResult = LatinoCF.ConstructSimpleTokenizer(_type, _min_token_len)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tokenizer'] = execResultPy
    return outputDict

def latino_construct_regex_tokenizer(inputDict):
    _token_regex = ToString(inputDict['token_regex'])
    _ignore_unknown_tokens = ToBool(inputDict['ignore_unknown_tokens'])
    _regex_options_ignore_case = ToBool(inputDict['regex_options_ignore_case'])
    _regex_options_multiline = ToBool(inputDict['regex_options_multiline'])
    _regex_options_explicit_capture = ToBool(inputDict['regex_options_explicit_capture'])
    _regex_options_compiled = ToBool(inputDict['regex_options_compiled'])
    _regex_options_singleline = ToBool(inputDict['regex_options_singleline'])
    _regex_options_ignore_pattern_whitespace = ToBool(inputDict['regex_options_ignore_pattern_whitespace'])
    _regex_options_right_to_left = ToBool(inputDict['regex_options_right_to_left'])
    _regex_options_ecma_script = ToBool(inputDict['regex_options_ecma_script'])
    _regex_options_culture_invariant = ToBool(inputDict['regex_options_culture_invariant'])
    execResult = LatinoCF.ConstructRegexTokenizer(_token_regex, _ignore_unknown_tokens, _regex_options_ignore_case, _regex_options_multiline, _regex_options_explicit_capture, _regex_options_compiled, _regex_options_singleline, _regex_options_ignore_pattern_whitespace, _regex_options_right_to_left, _regex_options_ecma_script, _regex_options_culture_invariant)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tokenizer'] = execResultPy
    return outputDict

def latino_tokenize_sentences(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _tokenizer = ToNetObj(inputDict['tokenizer'])
    _input_annotation = ToString(inputDict['input_annotation'])
    _output_annotation = ToString(inputDict['output_annotation'])
    execResult = LatinoCF.TokenizeSentences(_adc, _tokenizer, _input_annotation, _output_annotation)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_tokenize_words(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _tokenizer = ToNetObj(inputDict['tokenizer'])
    _input_annotation = ToString(inputDict['input_annotation'])
    _output_annotation = ToString(inputDict['output_annotation'])
    execResult = LatinoCF.TokenizeWords(_adc, _tokenizer, _input_annotation, _output_annotation)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_tokenize_multiple(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _tokenizers = ToNetObj(inputDict['tokenizers'])
    _input_annotations = ToString(inputDict['input_annotations'])
    _output_annotations = ToString(inputDict['output_annotations'])
    execResult = LatinoCF.TokenizeMultiple(_adc, _tokenizers, _input_annotations, _output_annotations)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_tokenize_string_string(inputDict):
    _text = ToNetObj(inputDict['text'])
    _tokenizer = ToNetObj(inputDict['tokenizer'])
    execResult = LatinoCF.TokenizeStringString(_text, _tokenizer)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['string'] = execResultPy
    return outputDict

def latino_tokenize_string_words(inputDict):
    _text = ToNetObj(inputDict['text'])
    _tokenizer = ToNetObj(inputDict['tokenizer'])
    execResult = LatinoCF.TokenizeStringWords(_text, _tokenizer)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['string'] = execResultPy
    return outputDict

def latino_construct_english_maximum_entropy_pos_tagger(inputDict):
    _beam_size = ToInt(inputDict['beam_size'])
    execResult = LatinoCF.ConstructEnglishMaximumEntropyPosTagger(_beam_size)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['pos_tagger'] = execResultPy
    return outputDict

def latino_pos_tag(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _pos_tagger = ToNetObj(inputDict['pos_tagger'])
    _group_annotation = ToString(inputDict['group_annotation'])
    _element_annotation = ToString(inputDict['element_annotation'])
    _output_feature = ToString(inputDict['output_feature'])
    execResult = LatinoCF.PosTag(_adc, _pos_tagger, _group_annotation, _element_annotation, _output_feature)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_pos_tag_string(inputDict):
    _text = ToNetObj(inputDict['text'])
    _pos_tagger = ToNetObj(inputDict['pos_tagger'])
    _output_feature = ToString(inputDict['output_feature'])
    execResult = LatinoCF.PosTagString(_text, _pos_tagger, _output_feature)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['string'] = execResultPy
    return outputDict

def latino_get_stop_words(inputDict):
    _language = ToEnum(Latino.TextMining.Language, inputDict['language'], Latino.TextMining.Language.English)
    execResult = LatinoCF.GetStopWords(_language)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['strings'] = execResultPy
    return outputDict

def latino_construct_lemma_sharp_lemmatizer(inputDict):
    _language = ToEnum(Latino.TextMining.Language, inputDict['language'], Latino.TextMining.Language.English)
    execResult = LatinoCF.ConstructLemmaSharpLemmatizer(_language)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tagger'] = execResultPy
    return outputDict

def latino_construct_snowball_stemmer(inputDict):
    _language = ToEnum(Latino.TextMining.Language, inputDict['language'], Latino.TextMining.Language.English)
    execResult = LatinoCF.ConstructSnowballStemmer(_language)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tagger'] = execResultPy
    return outputDict

def latino_construct_stop_words_tagger(inputDict):
    _stop_words = ToNetObj(inputDict['stop_words'])
    _ignore_case = ToBool(inputDict['ignore_case'])
    execResult = LatinoCF.ConstructStopWordsTagger(_stop_words, _ignore_case)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tagger'] = execResultPy
    return outputDict

def latino_construct_condition_tagger(inputDict):
    _feature_condition = ToString(inputDict['feature_condition'])
    _output_feature_value = ToString(inputDict['output_feature_value'])
    _elements_text_to_feature_value = ToBool(inputDict['elements_text_to_feature_value'])
    execResult = LatinoCF.ConstructConditionTagger(_feature_condition, _output_feature_value, _elements_text_to_feature_value)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tagger'] = execResultPy
    return outputDict

def latino_tag_adc_stem_lemma(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _tagger = ToNetObj(inputDict['tagger'])
    _element_annotation = ToString(inputDict['element_annotation'])
    _output_feature = ToString(inputDict['output_feature'])
    execResult = LatinoCF.TagADCStemLemma(_adc, _tagger, _element_annotation, _output_feature)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_tag_adc_stopwords(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _tagger = ToNetObj(inputDict['tagger'])
    _element_annotation = ToString(inputDict['element_annotation'])
    _output_feature = ToString(inputDict['output_feature'])
    execResult = LatinoCF.TagADCStopwords(_adc, _tagger, _element_annotation, _output_feature)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_tag_adc_multiple(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _taggers = ToNetObj(inputDict['taggers'])
    _element_annotations = ToString(inputDict['element_annotations'])
    _output_features = ToString(inputDict['output_features'])
    execResult = LatinoCF.TagADCMultiple(_adc, _taggers, _element_annotations, _output_features)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['adc'] = execResultPy
    return outputDict

def latino_tag_string_stem_lemma(inputDict):
    _text = ToNetObj(inputDict['text'])
    _tagger = ToNetObj(inputDict['tagger'])
    _output_feature = ToString(inputDict['output_feature'])
    execResult = LatinoCF.TagStringStemLemma(_text, _tagger, _output_feature)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['string'] = execResultPy
    return outputDict

def latino_tag_string_stopwords(inputDict):
    _text = ToNetObj(inputDict['text'])
    _tagger = ToNetObj(inputDict['tagger'])
    _output_feature = ToString(inputDict['output_feature'])
    execResult = LatinoCF.TagStringStopwords(_text, _tagger, _output_feature)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['string'] = execResultPy
    return outputDict

def latino_construct_bow_space_1(inputDict):
    _documents = ToNetObj(inputDict['documents'])
    _tokenizer = ToNetObj(inputDict['tokenizer'])
    _stemmer = ToNetObj(inputDict['stemmer'])
    _stopwords = ToNetObj(inputDict['stopwords'])
    _max_n_gram_len = ToInt(inputDict['max_n_gram_len'])
    _min_word_freq = ToInt(inputDict['min_word_freq'])
    _word_weight_type = ToEnum(Latino.TextMining.WordWeightType, inputDict['word_weight_type'], Latino.TextMining.WordWeightType.TfIdf)
    _cut_low_weights_perc = ToFloat(inputDict['cut_low_weights_perc'])
    _normalize_vectors = ToBool(inputDict['normalize_vectors'])
    execResult = LatinoCF.ConstructBowSpace(_documents, _tokenizer, _stemmer, _stopwords, _max_n_gram_len, _min_word_freq, _word_weight_type, _cut_low_weights_perc, _normalize_vectors)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['bow'] = execResultPy['bow']
    outputDict['ds'] = execResultPy['ds']
    return outputDict

def latino_construct_bow_space_2(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _token_id = ToString(inputDict['token_id'])
    _stem_id = ToString(inputDict['stem_id'])
    _stopword_id = ToString(inputDict['stopword_id'])
    _label_id = ToString(inputDict['label_id'])
    _max_n_gram_len = ToInt(inputDict['max_n_gram_len'])
    _min_word_freq = ToInt(inputDict['min_word_freq'])
    _word_weight_type = ToEnum(Latino.TextMining.WordWeightType, inputDict['word_weight_type'], Latino.TextMining.WordWeightType.TfIdf)
    _cut_low_weights_perc = ToFloat(inputDict['cut_low_weights_perc'])
    _normalize_vectors = ToBool(inputDict['normalize_vectors'])
    execResult = LatinoCF.ConstructBowSpace(_adc, _token_id, _stem_id, _stopword_id, _label_id, _max_n_gram_len, _min_word_freq, _word_weight_type, _cut_low_weights_perc, _normalize_vectors)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['bow'] = execResultPy['bow']
    outputDict['ds'] = execResultPy['ds']
    return outputDict

def latino_construct_bow_model(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _token_id = ToString(inputDict['token_id'])
    _stem_id = ToString(inputDict['stem_id'])
    _stopword_id = ToString(inputDict['stopword_id'])
    _label_id = ToString(inputDict['label_id'])
    _max_n_gram_len = ToInt(inputDict['max_n_gram_len'])
    _min_word_freq = ToInt(inputDict['min_word_freq'])
    _word_weight_type = ToEnum(Latino.TextMining.WordWeightType, inputDict['word_weight_type'], Latino.TextMining.WordWeightType.TfIdf)
    _cut_low_weights_perc = ToFloat(inputDict['cut_low_weights_perc'])
    _normalize_vectors = ToBool(inputDict['normalize_vectors'])
    execResult = LatinoCF.ConstructBowModel(_adc, _token_id, _stem_id, _stopword_id, _label_id, _max_n_gram_len, _min_word_freq, _word_weight_type, _cut_low_weights_perc, _normalize_vectors)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['bow'] = execResultPy
    return outputDict

def latino_parse_documents(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _bow = ToNetObj(inputDict['bow'])
    execResult = LatinoCF.ParseDocuments(_adc, _bow)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['pdc'] = execResultPy
    return outputDict

def latino_get_vocabulary_table(inputDict):
    _bow = ToNetObj(inputDict['bow'])
    _start_index = ToInt(inputDict['start_index'])
    _max_words = ToInt(inputDict['max_words'])
    execResult = LatinoCF.GetVocabularyTable(_bow, _start_index, _max_words)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['vocabulary'] = execResultPy
    return outputDict

def latino_process_new_documents_from_adc(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _bow = ToNetObj(inputDict['bow'])
    execResult = LatinoCF.ProcessNewDocumentsFromADC(_adc, _bow)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['ds'] = execResultPy
    return outputDict

def latino_process_new_documents_from_string(inputDict):
    _lst = ToNetObj(inputDict['lst'])
    _bow = ToNetObj(inputDict['bow'])
    execResult = LatinoCF.ProcessNewDocumentsFromString(_lst, _bow)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['ds'] = execResultPy
    return outputDict

def latino_get_vocabulary(inputDict):
    _bow = ToNetObj(inputDict['bow'])
    _start_index = ToInt(inputDict['start_index'])
    _max_words = ToInt(inputDict['max_words'])
    execResult = LatinoCF.GetVocabulary(_bow, _start_index, _max_words)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['terms'] = execResultPy
    return outputDict

def latino_create_term_dataset_from_adc(inputDict):
    _adc = ToNetObj(inputDict['adc'])
    _bow = ToNetObj(inputDict['bow'])
    execResult = LatinoCF.CreateTermDatasetFromAdc(_adc, _bow)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['term_dataset'] = execResultPy
    return outputDict

def latino_add_labels_to_document_vectors(inputDict):
    _ds = ToNetObj(inputDict['ds'])
    _labels = ToNetObj(inputDict['labels'])
    execResult = LatinoCF.AddLabelsToDocumentVectors(_ds, _labels)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['ds'] = execResultPy
    return outputDict

def latino_remove_document_vectors_labels(inputDict):
    _ds = ToNetObj(inputDict['ds'])
    execResult = LatinoCF.RemoveDocumentVectorsLabels(_ds)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['ds'] = execResultPy
    return outputDict

def latino_extract_dataset_labels(inputDict):
    _ds = ToNetObj(inputDict['ds'])
    execResult = LatinoCF.ExtractDatasetLabels(_ds)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['labels'] = execResultPy
    return outputDict

def latino_dataset_split_simple(inputDict):
    _ds = ToNetObj(inputDict['ds'])
    _percentage = ToFloat(inputDict['percentage'])
    _random_seed = ToInt(inputDict['random_seed'])
    execResult = LatinoCF.DatasetSplitSimple(_ds, _percentage, _random_seed)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['ds1'] = execResultPy['ds1']
    outputDict['ds2'] = execResultPy['ds2']
    return outputDict

def latino_dataset_split_predefined(inputDict):
    _ds = ToNetObj(inputDict['ds'])
    _sets = ToNetObj(inputDict['sets'])
    _set_id = ToInt(inputDict['set_id'])
    execResult = LatinoCF.DatasetSplitPredefined(_ds, _sets, _set_id)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['ds1'] = execResultPy['ds1']
    outputDict['ds2'] = execResultPy['ds2']
    return outputDict

def latino_dataset_to_object(inputDict):
    _ds = ToNetObj(inputDict['ds'])
    execResult = LatinoCF.DatasetToObject(_ds)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['obj'] = execResultPy
    return outputDict

def latino_object_to_dataset(inputDict):
    _obj = ToNetObj(inputDict['obj'])
    execResult = LatinoCF.ObjectToDataset(_obj)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['ds'] = execResultPy
    return outputDict

def latino_calculate_similarity_matrix(inputDict):
    _ds1 = ToNetObj(inputDict['ds1'])
    _ds2 = ToNetObj(inputDict['ds2'])
    _thresh = ToFloat(inputDict['thresh'])
    _full_matrix = ToBool(inputDict['full_matrix'])
    execResult = LatinoCF.CalculateSimilarityMatrix(_ds1, _ds2, _thresh, _full_matrix)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['smx'] = execResultPy
    return outputDict

def latino_sparse_matrix_to_table(inputDict):
    _smx = ToNetObj(inputDict['smx'])
    execResult = LatinoCF.SparseMatrixToTable(_smx)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['tbl'] = execResultPy
    return outputDict

def latino_construct_k_means_clusterer(inputDict):
    _k = ToInt(inputDict['k'])
    _centroid_type = ToEnum(Latino.Model.CentroidType, inputDict['centroid_type'], Latino.Model.CentroidType.NrmL2)
    _similarity_model = ToEnum(LatinoInterfaces.SimilarityModel, inputDict['similarity_model'], LatinoInterfaces.SimilarityModel.Cosine)
    _random_seed = ToInt(inputDict['random_seed'])
    _eps = ToFloat(inputDict['eps'])
    _trials = ToInt(inputDict['trials'])
    execResult = LatinoCF.ConstructKMeansClusterer(_k, _centroid_type, _similarity_model, _random_seed, _eps, _trials)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['clusterer'] = execResultPy
    return outputDict

def latino_construct_k_means_fast_clusterer(inputDict):
    _k = ToInt(inputDict['k'])
    _random_seed = ToInt(inputDict['random_seed'])
    _eps = ToFloat(inputDict['eps'])
    _trials = ToInt(inputDict['trials'])
    execResult = LatinoCF.ConstructKMeansFastClusterer(_k, _random_seed, _eps, _trials)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['clusterer'] = execResultPy
    return outputDict

def latino_construct_hierarchical_bisecting_clusterer(inputDict):
    _min_quality = ToFloat(inputDict['min_quality'])
    execResult = LatinoCF.ConstructHierarchicalBisectingClusterer(_min_quality)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['clusterer'] = execResultPy
    return outputDict

def latino_cluster_document_vectors(inputDict):
    _clusterer = ToNetObj(inputDict['clusterer'])
    _dataset = ToNetObj(inputDict['dataset'])
    execResult = LatinoCF.ClusterDocumentVectors(_clusterer, _dataset)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['clust_res'] = execResultPy
    return outputDict

def latino_clustering_results_info(inputDict):
    _clust_res = ToNetObj(inputDict['clust_res'])
    execResult = LatinoCF.ClusteringResultsInfo(_clust_res)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['doc_labels'] = execResultPy['docLabels']
    outputDict['clust_tree'] = execResultPy['clustTree']
    return outputDict

def latino_construct_centroid_classifier(inputDict):
    _similarity_model = ToEnum(LatinoInterfaces.SimilarityModel, inputDict['similarity_model'], LatinoInterfaces.SimilarityModel.Cosine)
    _normalize_centorids = ToBool(inputDict['normalize_centorids'])
    execResult = LatinoCF.ConstructCentroidClassifier(_similarity_model, _normalize_centorids)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_construct_naive_bayes_classifier(inputDict):
    _normalize = ToBool(inputDict['normalize'])
    _log_sum_exp_trick = ToBool(inputDict['log_sum_exp_trick'])
    execResult = LatinoCF.ConstructNaiveBayesClassifier(_normalize, _log_sum_exp_trick)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_construct_svm_binary_classifier(inputDict):
    _c = ToFloat(inputDict['c'])
    _biased_hyperplane = ToBool(inputDict['biased_hyperplane'])
    _kernel_type = ToEnum(Latino.Model.SvmLightKernelType, inputDict['kernel_type'], Latino.Model.SvmLightKernelType.Linear)
    _kernel_param_gamma = ToFloat(inputDict['kernel_param_gamma'])
    _kernel_param_d = ToFloat(inputDict['kernel_param_d'])
    _kernel_param_s = ToFloat(inputDict['kernel_param_s'])
    _kernel_param_c = ToFloat(inputDict['kernel_param_c'])
    _eps = ToFloat(inputDict['eps'])
    _max_iter = ToInt(inputDict['max_iter'])
    _custom_params = ToString(inputDict['custom_params'])
    execResult = LatinoCF.ConstructSvmBinaryClassifier(_c, _biased_hyperplane, _kernel_type, _kernel_param_gamma, _kernel_param_d, _kernel_param_s, _kernel_param_c, _eps, _max_iter, _custom_params)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_construct_svm_multiclass_fast(inputDict):
    _c = ToFloat(inputDict['c'])
    _eps = ToFloat(inputDict['eps'])
    execResult = LatinoCF.ConstructSvmMulticlassFast(_c, _eps)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_construct_majority_classifier(inputDict):
    execResult = LatinoCF.ConstructMajorityClassifier()
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_construct_maximum_entropy_classifier(inputDict):
    _move_data = ToBool(inputDict['move_data'])
    _num_iter = ToInt(inputDict['num_iter'])
    _cut_off = ToInt(inputDict['cut_off'])
    _num_threads = ToInt(inputDict['num_threads'])
    _normalize = ToBool(inputDict['normalize'])
    execResult = LatinoCF.ConstructMaximumEntropyClassifier(_move_data, _num_iter, _cut_off, _num_threads, _normalize)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_construct_maximum_entropy_classifier_fast(inputDict):
    _move_data = ToBool(inputDict['move_data'])
    _num_iter = ToInt(inputDict['num_iter'])
    _cut_off = ToInt(inputDict['cut_off'])
    _num_threads = ToInt(inputDict['num_threads'])
    _normalize = ToBool(inputDict['normalize'])
    execResult = LatinoCF.ConstructMaximumEntropyClassifierFast(_move_data, _num_iter, _cut_off, _num_threads, _normalize)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_construct_knn_classifier(inputDict):
    _similarity_model = ToEnum(LatinoInterfaces.SimilarityModel, inputDict['similarity_model'], LatinoInterfaces.SimilarityModel.Cosine)
    _k = ToInt(inputDict['k'])
    _soft_voting = ToBool(inputDict['soft_voting'])
    execResult = LatinoCF.ConstructKnnClassifier(_similarity_model, _k, _soft_voting)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_construct_knn_classifier_fast(inputDict):
    _k = ToInt(inputDict['k'])
    _soft_voting = ToBool(inputDict['soft_voting'])
    execResult = LatinoCF.ConstructKnnClassifierFast(_k, _soft_voting)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['classifier'] = execResultPy
    return outputDict

def latino_train_classifier(inputDict):
    _classifier = ToNetObj(inputDict['classifier'])
    _training_data = ToNetObj(inputDict['training_data'])
    execResult = LatinoCF.TrainClassifier(_classifier, _training_data)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['trained_classifier'] = execResultPy
    return outputDict

def latino_predict_classification(inputDict):
    _csf = ToNetObj(inputDict['csf'])
    _ds = ToNetObj(inputDict['ds'])
    execResult = LatinoCF.PredictClassification(_csf, _ds)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['predictions'] = execResultPy['predictions']
    outputDict['ds'] = execResultPy['ds']
    return outputDict

def latino_prediction_info(inputDict):
    _predictions = ToNetObj(inputDict['predictions'])
    execResult = LatinoCF.PredictionInfo(_predictions)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['labels'] = execResultPy['labels']
    outputDict['predict_infos'] = execResultPy['predictInfos']
    return outputDict

def latino_cross_validation(inputDict):
    _csf = ToNetObj(inputDict['csf'])
    _ds = ToNetObj(inputDict['ds'])
    _num_of_sets = ToInt(inputDict['num_of_sets'])
    _random = ToBool(inputDict['random'])
    _use_seed = ToBool(inputDict['use_seed'])
    _random_seed = ToInt(inputDict['random_seed'])
    execResult = LatinoCF.CrossValidation(_csf, _ds, _num_of_sets, _random, _use_seed, _random_seed)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['obj'] = execResultPy
    return outputDict

def latino_cross_validation_predef_splits(inputDict):
    _csf = ToNetObj(inputDict['csf'])
    _ds = ToNetObj(inputDict['ds'])
    _sets = ToNetObj(inputDict['sets'])
    execResult = LatinoCF.CrossValidationPredefSplits(_csf, _ds, _sets)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['obj'] = execResultPy
    return outputDict

def latino_cross_validation_predef_multi_splits(inputDict):
    _csf = ToNetObj(inputDict['csf'])
    _ds = ToNetObj(inputDict['ds'])
    _multi_sets = ToNetObj(inputDict['multi_sets'])
    execResult = LatinoCF.CrossValidationPredefMultiSplits(_csf, _ds, _multi_sets)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['obj'] = execResultPy
    return outputDict

def latino_accuracy_claculation(inputDict):
    _list1 = ToNetObj(inputDict['list1'])
    _list2 = ToNetObj(inputDict['list2'])
    execResult = LatinoCF.AccuracyClaculation(_list1, _list2)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['accuracy'] = execResultPy['accuracy']
    outputDict['statistics'] = execResultPy['statistics']
    return outputDict

def latino_run_c_sharp_snippet(inputDict):
    _snippet_params = ToNetObj(inputDict['snippet_params'])
    _snippet_code = ToString(inputDict['snippet_code'])
    _aditional_references = ToString(inputDict['aditional_references'])
    _usings = ToString(inputDict['usings'])
    execResult = LatinoCF.RunCSharpSnippet(_snippet_params, _snippet_code, _aditional_references, _usings)
    execResultPy = ToPyObj(execResult)
    outputDict = {}
    outputDict['out'] = execResultPy['out']
    outputDict['console_out'] = execResultPy['consoleOut']
    outputDict['error'] = execResultPy['error']
    outputDict['code'] = execResultPy['code']
    return outputDict

