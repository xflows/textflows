from itertools import izip
from workflows.textflows import *
from tagging_lib.part_of_speech import * #POS TAGGERS
from tagging_lib.stemming import * #STEMMERS

# HUBS
def pos_tagger_hub(input_dict):
    if type(input_dict['pos_tagger'])!=dict: #check if this is a latino object
        from ...latino.library_gen import latino_pos_tag
        return latino_pos_tag(input_dict)
    else:
        return universal_sentence_tagger_hub(input_dict)

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

    if type(input_dict['stop_word_tagger'])!=dict: #check if this is a latino object
        from ...latino.library_gen import latino_tag_adcstopwords
        input_dict['tagger']=input_dict['stop_word_tagger']  #TODO temporary
        return latino_tag_adcstopwords(input_dict)
    else:
        adc = input_dict['adc']
        tagger_dict = input_dict['stop_word_tagger']
        input_annotation = input_dict['element_annotation']
        output_annotation = input_dict['output_feature']
        return universal_word_tagger_hub(adc,tagger_dict,input_annotation,output_annotation)

def stem_lemma_tagger_hub(input_dict):
    raise NotImplementedError
    if type(input_dict['tagger'])!=dict: #check if this is a latino object
        from ...latino.library_gen import latino_tag_adcstem_lemma
        return latino_tag_adcstem_lemma(input_dict)
    else:
        return universal_word_tagger_hub(input_dict)

def universal_word_tagger_hub(adc,tagger_dict,input_annotation,output_annotation):
    tagger=tagger_dict['object']
    tagger_function=tagger_dict['function']
    args=tagger_dict.get('args',[])
    kwargs=tagger_dict.get('kargs',{})

    for document in adc.documents:
        if document.features['contentType'] == "Text":
            if not document.text:
                pass
            for annotation,subtext in document.get_annotations_with_text(input_annotation): #all annotations of this type
                if subtext:
                    new_feature=getattr(tagger,tagger_function)(subtext,*args,**kwargs)
                    if new_feature!=None:
                        annotation.features[output_annotation]=new_feature
    return {'adc': adc }


def universal_sentence_tagger_hub(input_dict):
    tagger_dict = input_dict['pos_tagger']
    tagger=tagger_dict['object']
    tagger_function=tagger_dict['function']
    args=tagger_dict.get('args',[])
    kwargs=tagger_dict.get('kargs',{})

    group_annotation_name = input_dict['group_annotation']
    element_annotation_name = input_dict['element_annotation']
    output_annotation_name = input_dict['output_feature']
    adc = input_dict['adc']


    for doc in adc.documents:
        if doc.features['contentType'] == "Text":
            if not doc.text:
                pass
            group_annotations=sorted(doc.get_annotations_with_text(group_annotation_name),key=lambda x: x[0].span_start)
            element_annotations=sorted(doc.get_annotations_with_text(element_annotation_name),key=lambda x: x[0].span_start)

            text_grouped=[] #text_groups= [['First','sentence',['Second','sentance']]
            annotations_grouped=[] #annotations_grouped= [[<Annotation span_start:0 span_ned:4>, <Annotation span_start:6 span_ned:11>],[...

            i=0
            for group_annotation,_ in group_annotations:
                elements=[]
                sentence_annotations=[]
                #find elementary annotations 'contained' in the group_annotation
                while i<len(element_annotations) and element_annotations[i][0].span_end<=group_annotation.span_end:
                    annotation=element_annotations[i][0]
                    text_block=element_annotations[i][1]
                    elements.append(text_block)
                    sentence_annotations.append(annotation)
                    i+=1
                text_grouped.append(elements)
                annotations_grouped.append(sentence_annotations)

            new_features=getattr(tagger,tagger_function)(text_grouped,*args,**kwargs)
            for sentence_features, sentence_annotations in izip(new_features,annotations_grouped):
                for feature,annotation in izip(sentence_features,sentence_annotations):
                    annotation.features[output_annotation_name]=feature[1]

            return {'adc': adc }



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

nltk.classify.scikitlearn