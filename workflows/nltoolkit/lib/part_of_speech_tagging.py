from tagging_common import universal_sentence_tagger_hub
#from nltk.tag.simplify   import (simplify_brown_tag, simplify_wsj_tag,
#                                 simplify_indian_tag, simplify_alpino_tag,
#                                 simplify_tag)
from nltk.tag.sequential import (DefaultTagger, NgramTagger, AffixTagger,
                                 RegexpTagger, #<--TODO
                                 ClassifierBasedPOSTagger)
import nltk.tag.brill
from nltk.tag.brill      import BrillTagger
from nltk.tag.brill_trainer import BrillTaggerTrainer
import re
from workflows.textflows import LatinoObject
from nltk.tag.tnt        import TnT
from nltk.tag.hunpos     import HunposTagger
from nltk.tag.stanford   import StanfordTagger
#from nltk.tag.crf        import MalletCRF
from django.conf import settings

def pos_tagger_hub(input_dict):
    if isinstance(input_dict['pos_tagger'],LatinoObject): #check if this is a latino object
        from ...latino.library_gen import latino_pos_tag
        adc= latino_pos_tag(input_dict)['adc']
    else:
        adc= universal_sentence_tagger_hub(input_dict)['adc']

    number_of_letters=int(input_dict['num_of_letters'])
    if number_of_letters!=-1:
        element_annotation_name = input_dict['element_annotation']
        output_annotation_name = input_dict['output_feature']
        for doc in adc.documents:
            for annotation in doc.get_annotations(element_annotation_name):
                if not output_annotation_name in annotation.features:
                    print input_dict['pos_tagger'],annotation.features
                    print doc.features
                else:
                    annotation.features[output_annotation_name]=annotation.features[output_annotation_name][0:number_of_letters]

    return {'adc': adc }

from workflows.textflows import DocumentCorpus, LatinoObject

def extract_pos_tagger_name(input_dict):
    tagger=input_dict['pos_tagger']

    tagger_name=tagger['object'].__class__.__name__ if not isinstance(tagger,LatinoObject) else tagger.name
    tagger_name=re.search(r'[A-Za-z\.0-9]+',tagger_name).group() #extracts valid characters

    return {'pos_tagger_name': tagger_name}



def corpus_reader(corpus):
    if type(corpus)==DocumentCorpus:
        raise NotImplementedError
    else:
        return corpus.tagged_sents()

def nltk_default_pos_tagger(input_dict):
    """
    A tagger that assigns the same tag to every token.

        >>> from nltk.tag.sequential import DefaultTagger
        >>> default_tagger = DefaultTagger('NN')
        >>> default_tagger.tag('This is a test'.split())
        [('This', 'NN'), ('is', 'NN'), ('a', 'NN'), ('test', 'NN')]

    This tagger is recommended as a backoff tagger, in cases where
    a more powerful tagger is unable to assign a tag to the word
    (e.g. because the word was not seen during training).

    :param default_tag: The default tag "%(default)s". Set this to a different tag, such as "NN",
            to change the default tag.

    :returns pos_tagger: A python dictionary containing the POS tagger
        object and its arguments.
    """
    from nltk.tag import DefaultTagger
    return {'pos_tagger': {
        'function':'tag_sents',
        'object': DefaultTagger(input_dict.get('default_tag','-None-'))
        }
    }

#SEQUENTIAL TAGGERS
def nltk_affix_pos_tagger(input_dict):
    """
    A tagger that chooses a token's tag based on a leading or trailing
    substring of its word string.  (It is important to note that these
    substrings are not necessarily "true" morphological affixes).  In
    particular, a fixed-length substring of the word is looked up in a
    table, and the corresponding tag is returned.  Affix taggers are
    typically constructed by training them on a tagged corpus.

    :param training_corpus: A tagged corpus included with NLTK, such as treebank, brown, cess_esp, floresta,
        or an Annotated Document Corpus in the standard TextFlows' adc format
    :param backoff_tagger: A backoff tagger, to be used by the new
        tagger if it encounters an unknown context.
    :param affix_length: The length of the affixes that should be
        considered during training and tagging.  Use negative
        numbers for suffixes.
    :param min_stem_length: Any words whose length is less than
        min_stem_length+abs(affix_length) will be assigned a
        tag of None by this tagger.

    :returns pos_tagger: A python dictionary containing the POS tagger object and its arguments.
    """

    tagged_corpus=corpus_reader(input_dict['training_corpus'])
    backoff_tagger=input_dict['backoff_tagger']['object'] if input_dict['backoff_tagger'] else DefaultTagger('-None-')
    affix_length=int(input_dict['affix_length'])
    min_stem_length=int(input_dict['min_stem_length'])
    cutoff=int(input_dict['cutoff']) #default 0


    return {'pos_tagger': {
                'function':'tag_sents',
                'object': AffixTagger(tagged_corpus, affix_length=affix_length, cutoff=cutoff,
                         min_stem_length=min(min_stem_length, 2), backoff=backoff_tagger)
        }
    }



def nltk_ngram_pos_tagger(input_dict):
    """
    A tagger that chooses a token's tag based on its word string and
    on the preceding n word's tags.  In particular, a tuple
    (tags[i-n:i-1], words[i]) is looked up in a table, and the
    corresponding tag is returned.  N-gram taggers are typically
    trained on a tagged corpus.

    Train a new NgramTagger using the given training data or
    the supplied model.  In particular, construct a new tagger
    whose table maps from each context (tag[i-n:i-1], word[i])
    to the most frequent tag for that context.  But exclude any
    contexts that are already tagged perfectly by the backoff
    tagger.

    :param training_corpus: A tagged corpus included with NLTK, such as treebank, brown, cess_esp, floresta,
        or an Annotated Document Corpus in the standard TextFlows' adc format
    :param backoff_tagger: A backoff tagger, to be used by the new
        tagger if it encounters an unknown context.
    :param cutoff: If the most likely tag for a context occurs
        fewer than *cutoff* times, then exclude it from the
        context-to-tag table for the new tagger.
    :param n:  N-gram is a contiguous sequence of n items from a given sequence of text or speech.

    :returns pos_tagger: A python dictionary containing the POS tagger object and its arguments.
    """

    training_corpus=corpus_reader(input_dict['training_corpus'])
    backoff_tagger=input_dict['backoff_tagger']['object'] if input_dict['backoff_tagger'] else DefaultTagger('-None-')
    n=int(input_dict['n']) #default 2
    cutoff=int(input_dict['cutoff']) #default 0

    return {'pos_tagger': {
                'function':'tag_sents',
                'object': NgramTagger(n, train=training_corpus, model=None,
                 backoff=backoff_tagger, cutoff=cutoff)
            }
    }


# CLASSIFIER TAGGERS
def nltk_phonetic_classifier_based_pos_tagger(input_dict):
    raise NotImplementedError

def nltk_classifier_based_pos_tagger(input_dict):
    """
    A sequential tagger that uses a classifier to choose the tag for
    each token in a sentence.  The featureset input for the classifier
    is generated by a feature detector function::

        feature_detector(tokens, index, history) -> featureset

    Where tokens is the list of unlabeled tokens in the sentence;
    index is the index of the token for which feature detection
    should be performed; and history is list of the tags for all
    tokens before index.

    Construct a new classifier-based sequential tagger.

    :param training_corpus: A tagged corpus consisting of a list of tagged
        sentences, where each sentence is a list of (word, tag) tuples.
    :param backoff_tagger: A backoff tagger, to be used by the new tagger
        if it encounters an unknown context.

TODO: odloci se katerega se obdrzi od naslednjih dveh

    :param classifier_builder: A function used to train a new
        classifier based on the data in *train*.  It should take
        one argument, a list of labeled featuresets (i.e.,
        (featureset, label) tuples).
    :param classifier: The classifier that should be used by the
        tagger.  #This is only useful if you want to manually
        construct the classifier; normally, you would use *train*
        instead.
    :param backoff_tagger: A backoff tagger, used if this tagger is
        unable to determine a tag for a given token.
    :param cutoff_prob: If specified, then this tagger will fall
        back on its backoff tagger if the probability of the most
        likely tag is less than *cutoff_prob*.

    :returns pos_tagger: A python dictionary containing the POS tagger
        object and its arguments.
    """
    #training_corpus=corpus_reader(input_dict['training_corpus']) #TODO: should it stay or should it go
    backoff_tagger=input_dict['backoff_tagger']['object'] if input_dict['backoff_tagger'] else DefaultTagger('-None-')
    classifier=None #(input_dict['classifier'])
    cutoff_prob=int(input_dict['cutoff_prob']) if input_dict['cutoff_prob'] else None

    import nltk
    tagger_object=ClassifierBasedPOSTagger(train=nltk.corpus.brown.tagged_sents()[:5], classifier=classifier,
                 backoff=backoff_tagger, cutoff_prob=cutoff_prob)
    return {'pos_tagger': {
                'function':'tag_sents',
                'object': tagger_object
            }
    }

#BRILL TAGGERS
def nltk_brill_pos_tagger(input_dict):
    """Brill's transformational rule-based tagger.  Brill taggers use an
    initial tagger (such as ``tag.DefaultTagger``) to assign an initial
    tag sequence to a text; and then apply an ordered list of
    transformational rules to correct the tags of individual tokens.
    These transformation rules are specified by the ``BrillRule``
    interface.

    Brill taggers can be created directly, from an initial tagger and
    a list of transformational rules; but more often, Brill taggers
    are created by learning rules from a training corpus, using either
    ``BrillTaggerTrainer`` or ``FastBrillTaggerTrainer``.

    :param training_corpus: A tagged corpus consisting of a list of tagged
        sentences, where each sentence is a list of (word, tag) tuples.
    :param initial_tagger: The initial tagger. Brill taggers use an initial
        tagger (such as ``DefaultTagger``) to assign an initial tag
        sequence to a text.
    :param max_rules: The maximum number of transformations to be created
    :param min_score: The minimum acceptable net error reduction
        that each transformation must produce in the corpus.
    :param deterministic: If true, then choose between rules that
        have the same score by picking the one whose __repr__
        is lexicographically smaller.  If false, then just pick the
        first rule we find with a given score -- this will depend
        on the order in which keys are returned from dictionaries,
        and so may not be the same from one run to the next.  If
        not specified, treat as true iff trace > 0.
    :param templates: templates to be used in training

    :returns pos_tagger: A python dictionary containing the POS tagger
        object and its arguments.
    """
    training_corpus=corpus_reader(input_dict['training_corpus'])[:1000]
    initial_tagger=input_dict['initial_tagger']['object'] if input_dict['initial_tagger'] else DefaultTagger('-None-')
    max_rules=int(input_dict['max_rules']) #default 200
    min_score=int(input_dict['min_score']) #default 2
    deterministic=True

    templates = getattr(nltk.tag.brill,input_dict['templates'])()

    trainer = BrillTaggerTrainer(initial_tagger, templates, deterministic=deterministic, trace=settings.DEBUG)
    brill_tagger = trainer.train(training_corpus, max_rules=max_rules, min_score=min_score) #return BrillTagger(self._initial_tagger, rules)

    if settings.DEBUG:
        for rule in brill_tagger.rules():
            print(str(rule))

    return {'pos_tagger': {
                'function':'tag_sents',
                'object': brill_tagger
            }
    }