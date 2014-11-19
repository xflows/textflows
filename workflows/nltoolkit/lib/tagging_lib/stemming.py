import nltk
#STEMMERS
def nltk_lancaster_stemmer(input_dict):
    from nltk.stem.lancaster import LancasterStemmer
    return {'tagger':
                {'object':LancasterStemmer(),
                 'function':'stem',
                }
    }

def nltk_porter_stemmer(input_dict):
    from nltk.stem.porter import PorterStemmer
    return {'tagger':
                {'object':PorterStemmer(),
                 'function':'stem',
                }
    }