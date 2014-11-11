def nltk_corpus(input_dict):
    """Returns the nltk.corpus for the selected corpus name"""
    import nltk.corpus
    return {'corpus': getattr(nltk.corpus,input_dict['corpus_name'])}
