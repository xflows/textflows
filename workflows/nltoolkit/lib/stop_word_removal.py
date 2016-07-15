from django.conf import settings
from workflows.tasks import executeFunction

from workflows.textflows import *
from tagging_common import universal_word_tagger_hub

def stop_word_tagger_hub(input_dict):
    """
    Apply the *stop_word_tagger* object on the Annotated Document Corpus (*adc*):

    1. first select only annotations of type Token Annotation *element_annotation*,
    2. apply the stop_word tagger
    3. create new annotations *output_feature* with the outputs of the stop word tagger.

    :param adc: Annotated Document Corpus (workflows.textflows.DocumentCorpus)
    :param stop_word_tagger: A python dictionary containing the stop word tagger object and its arguments.
    :param element_annotation: Which annotated part of document to be searched for stopwords.
    :param output_features: How to annotate the newly discovered stop word features.

    :returns adc: Annotated Document Corpus (workflows.textflows.DocumentCorpus)
    """

    if isinstance(input_dict['stop_word_tagger'],LatinoObject):
        from ...latino.library_gen import latino_tag_adcstopwords
        input_dict['tagger']=input_dict['stop_word_tagger']  #TODO temporary
        return executeFunction.apply_async([latino_tag_adcstopwords,input_dict],queue="windows").wait() if settings.USE_WINDOWS_QUEUE \
            else latino_tag_adcstopwords(input_dict)

    else:
        adc = input_dict['adc']
        tagger_dict = input_dict['stop_word_tagger']
        input_annotation = input_dict['element_annotation']
        output_annotation = input_dict['output_feature']
        return universal_word_tagger_hub(adc,tagger_dict,input_annotation,output_annotation)



#STOPWORD TAGGERS
class StopWordTagger:
    def __init__(self,stop_words,ignore_case=True):
        self.ignore_case=ignore_case
        self.stop_words=stop_words
        if type(stop_words) in [str,unicode]:
            self.stop_words=self.stop_words.split("\n")
        if ignore_case:
            self.stop_words=[sw.lower() for sw in self.stop_words]

    def tag(self,token):
        return "true" if (token.lower() if self.ignore_case else token) in self.stop_words else None


def nltk_stop_word_tagger(input_dict):
    """
    Constructs a python stop word tagger object.

    :param stop_words: A list or string (stop words separated by new lines) of stop words.
    :param ignore_case: If true than words are marked as stop word regardless of their casing.

    :returns stop_word_tagger: A python dictionary containing the StopWordTagger object and its arguments.
    """

    return {'stop_word_tagger':
                {'object':StopWordTagger(input_dict.get('stop_words',''),input_dict.get('ignore_case',True)),
                 'function':'tag',
                }
    }


class POSFilterTagger:
    def __init__(self, pos_tags):
        self.pos_tags = pos_tags
        if type(pos_tags) in [str,unicode]:
            self.pos_tags=self.pos_tags.split("\n")

    def tag(self,token):
        return "true" if (token.lower() if self.ignore_case else token) in self.stop_words else None


# import nltk
# # STOP_TYPES = ['DET', 'CNJ']
# text = "I have a python module installed on my system."
# # tokens = nltk.pos_tag(nltk.word_tokenize(text))
# # good_words = [w for w, wtype in token if wtype not in STOP_TYPES]
#
# nltk.pos_tag(nltk.word_tokenize(text))

# import nltk
#
# with open('sample.txt', 'r') as f:
#     sample = f.read()
#
# sentences = nltk.sent_tokenize(sample)
# tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
# tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
# chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)
#
# def extract_entity_names(t):
#     entity_names = []
#
#     if hasattr(t, 'node') and t.node:
#         if t.node == 'NE':
#             entity_names.append(' '.join([child[0] for child in t]))
#         else:
#             for child in t:
#                 entity_names.extend(extract_entity_names(child))
#
#     return entity_names
#
# entity_names = []
# for tree in chunked_sentences:
#     # Print results per sentence
#     # print extract_entity_names(tree)
#
#     entity_names.extend(extract_entity_names(tree))
#
# # Print all entity names
# #print entity_names
#
# # Print unique entity names
# print set(entity_names)