def nltk_treebank_word_tokenizer(input_dict):
    raise NotImplementedError() #span_tokenize not implemented in this class

    import nltk
    return {'tokenizer': {'type': nltk.TreebankWordTokenizer}}


def nltk_punkt_sentence_tokenizer(input_dict):
    import nltk
    return {'tokenizer': {'type': nltk.PunktSentenceTokenizer}}