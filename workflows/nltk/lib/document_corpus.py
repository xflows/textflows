from workflows.textflows import NltkCorpus

def nltk_corpus(input_dict):
    """Returns the nltk.corpus for the selected corpus name"""
    return {'corpus': NltkCorpus(input_dict['corpus_name'])}

print nltk_corpus