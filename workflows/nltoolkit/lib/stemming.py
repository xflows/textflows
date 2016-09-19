from django.conf import settings
from workflows.tasks import executeFunction

import nltk
from workflows.textflows import *
from tagging_common import universal_word_tagger_hub
from nltk.corpus import wordnet
#from tagging_common_parallel import universal_word_tagger_hub


def stem_lemma_tagger_hub(input_dict):
    if isinstance(input_dict['tagger'],LatinoObject): #check if this is a latino object
        from ...latino.library_gen import latino_tag_adc_stem_lemma
        return latino_tag_adc_stem_lemma(input_dict) if not settings.USE_WINDOWS_QUEUE \
            else executeFunction.apply_async([latino_tag_adc_stem_lemma,input_dict],queue="windows").wait()
    else:
        adc = input_dict['adc']
        tagger_dict = input_dict['tagger']
        input_annotation = input_dict['element_annotation']
        output_annotation = input_dict['output_feature']
        return universal_word_tagger_hub(adc,tagger_dict,input_annotation,output_annotation)

def lemmatizer_evaluate(input_dict, *args,**kwargs):
    corpus = input_dict['ptb_corpus']
    
    print('corpus zloadan')
    stemmer_dict = input_dict['tagger']
    stemmer=stemmer_dict['object']
    stemmer_function = stemmer_dict['function']
    tagger_dict = input_dict['pos_tagger']
    stemmer_name=stemmer.__class__.__name__ if not isinstance(stemmer,LatinoObject) else stemmer.name
    stemmer_name=re.search(r'[A-Za-z\.0-9]+',stemmer_name).group() #extracts valid characters

    morphy_tag = {'NN':wordnet.NOUN, 'NNS':wordnet.NOUN,
                  'NNP':wordnet.NOUN, 'NNPS':wordnet.NOUN, 'JJ':wordnet.ADJ,
                  'JJR':wordnet.ADJ, 'JJS':wordnet.ADJ, 'VB':wordnet.VERB,
                  'VBD':wordnet.VERB, 'VBG':wordnet.VERB, 'VBN':wordnet.VERB,
                  'VBP':wordnet.VERB, 'VBZ':wordnet.VERB,'RB':wordnet.ADV,
                  'RBR':wordnet.ADV, 'RBS':wordnet.ADV}
    if tagger_dict:
        tagger=tagger_dict['object']
    
    corpus = [[(w, t) for (w, t) in sent if not " " in w and not "_" in w] for sent in corpus]
    predicted = []
    if stemmer_name == 'WordNetLemmatizer':
        tagged_sents = tagger.tag_sents([w for (w, t) in sent if w] for sent in corpus)
        for sent in tagged_sents:
            for word, pos in sent:
                if pos in morphy_tag:
                    predicted.append(stemmer.lemmatize(word, morphy_tag[pos]).lower())
                else:
                    predicted.append(stemmer.lemmatize(word).lower())
    else:
        for sent in corpus:
            for w, t in sent:
                predicted.append(getattr(stemmer, stemmer_function)(w.lower(), *args, **kwargs))
    
    corpus = [[(w, t) for (w, t) in sent if not " " in w and not "_" in w] for sent in corpus]
    actual = [t.lower() for sent in corpus for (w, t) in sent if w]

    print actual[:100]
    print predicted[:100]

    print 'finished'
    return {'actual_and_predicted': [actual, predicted]}

# STEMMERS
def nltk_lancaster_stemmer(input_dict):
    """
    A word stemmer based on the Lancaster stemming algorithm.
    """
    return {'tagger':
                {'object': nltk.stem.lancaster.LancasterStemmer(),
                 'function': 'stem', }
    }


def nltk_porter_stemmer(input_dict):
    """
    A word stemmer based on the Porter stemming algorithm.
    """
    return {'tagger':
                {'object': nltk.stem.porter.PorterStemmer(),
                 'function': 'stem',
                }
    }


def nltk_isri_stemmer(input_dict):
    """
    ISRI Arabic stemmer based on algorithm: Arabic Stemming without a root dictionary.
    Information Science Research Institute. University of Nevada, Las Vegas, USA.
    """
    return {'tagger':
                {'object': nltk.stem.isri.ISRIStemmer(),
                 'function': 'stem',
                }
    }


def nltk_regexp_stemmer(input_dict):
    """
    A stemmer that uses regular expressions to identify morphological
    affixes.  Any substrings that match the regular expressions will
    be removed.

    :type regexp: str or regexp
    :param regexp: The regular expression that should be used to
        identify morphological affixes.
    :type min: int
    :param min: The minimum length of string to stem
    """

    regexp = input_dict["regexp"] #default ing$|s$|e$|able$
    min = int(input_dict["min"]) #default 4
    return {'tagger':
                {'object': NltkRegexpStemmer(regexp, min=min),
                 'function': 'stem',
                }
    }


def nltk_rslp_stemmer(input_dict):
    """
   A stemmer for Portuguese.

   """
    return {'tagger':
                {'object': nltk.stem.rslp.RSLPStemmer(),
                 'function': 'stem',
                }}


def nltk_snowball_stemmer(input_dict):
    """
    Snowball Stemmer
    The following languages are supported:
    Danish, Dutch, English, Finnish, French, German,
    Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian,
    Spanish and Swedish.

    The algorithm for English is documented here:
    Porter, M. \"An algorithm for suffix stripping.\"
    Program 14.3 (1980): 130-137.

    The algorithms have been developed by Martin Porter.
    These stemmers are called Snowball, because Porter created
    a programming language with this name for creating
    new stemming algorithms. There is more information available
    at http://snowball.tartarus.org/

    :param language: The language whose subclass is instantiated.
    :type language: str or unicode
    :param ignore_stopwords: If set to True, stopwords are
                         not stemmed and returned unchanged.
                         Set to False by default.
    :type ignore_stopwords: bool
    """

    language = input_dict["language"]
    ignore_stopwords = input_dict["ignore_stopwords"] == "true"

    if language == "danish":
        stemmer = nltk.stem.snowball.DanishStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "dutch":
        stemmer = nltk.stem.snowball.DutchStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "english":
        stemmer = nltk.stem.snowball.EnglishStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "finnish":
        stemmer = nltk.stem.snowball.FinnishStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "french":
        stemmer = nltk.stem.snowball.FrenchStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "german":
        stemmer = nltk.stem.snowball.GermanStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "hungarian":
        stemmer = nltk.stem.snowball.HungarianStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "italian":
        stemmer = nltk.stem.snowball.ItalianStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "norwegian":
        stemmer = nltk.stem.snowball.NorwegianStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "portuguese":
        stemmer = nltk.stem.snowball.PortugueseStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "romanian":
        stemmer = nltk.stem.snowball.RomanianStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "russian":
        stemmer = nltk.stem.snowball.RussianStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "spanish":
        stemmer = nltk.stem.snowball.SpanishStemmer(ignore_stopwords=ignore_stopwords)
    elif language == "swedish":
        stemmer = nltk.stem.snowball.SwedishStemmer(ignore_stopwords=ignore_stopwords)

    return {'tagger':
            {'object': stemmer,
             'function': 'stem',
            }}


def nltk_wordnet_lemmatizer(input_dict):
    """
    WordNet Lemmatizer
    Lemmatize using WordNet's built-in morphy function.
    Returns the input word unchanged if it cannot be found in WordNet.
    """
    return {'tagger':
                {'object': nltk.stem.wordnet.WordNetLemmatizer(),
                 'function': 'lemmatize',
                }}

































