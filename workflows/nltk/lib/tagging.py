from itertools import izip
from workflows.textflows import *
from tagging_lib.part_of_speech import *
#POS TAGGERS

# HUBS
def pos_tagger_hub(input_dict):
    if type(input_dict['tagger'])!=dict: #check if this is a latino object
        from ...latino.library_gen import latino_pos_tag
        return latino_pos_tag(input_dict)
    else:
        return universal_sentence_tagger_hub(input_dict)

def stopword_tagger_hub(input_dict):
    if type(input_dict['tagger'])!=dict: #check if this is a latino object
        from ...latino.library_gen import latino_tag_adcstopwords
        return latino_tag_adcstopwords(input_dict)
    else:
        return universal_word_tagger_hub(input_dict)

def stem_lemma_tagger_hub(input_dict):
    if type(input_dict['tagger'])!=dict: #check if this is a latino object
        from ...latino.library_gen import latino_tag_adcstem_lemma
        return latino_tag_adcstem_lemma(input_dict)
    else:
        return universal_word_tagger_hub(input_dict)

def universal_word_tagger_hub(input_dict):
    tagger_dict = input_dict['tagger']
    tagger=tagger_dict['object']
    tagger_function=tagger_dict['function']
    args=tagger_dict.get('args',[])
    kwargs=tagger_dict.get('kargs',{})

    input_annotation = input_dict['element_annotation']
    output_annotation = input_dict['output_feature']
    adc = input_dict['adc']

    #TODO
    #     outputFeature = outputFeature.Trim();
    #     TextBlockAnnotationService tba;
    #     if (tagger is ITagger)
    #         tba = ((ITagger)tagger).GetTextBlockAnnotationService(elementAnnotation);
    #     else
    #         tba = new TextBlockAnnotationService(elementAnnotation, null);


    for document in adc.documents:
        if document.features['contentType'] == "Text":
            if not document.text:
                pass
            for annotation in document.select_annotations(input_annotation): #all annotations of this type
                subtext = document.text[annotation.span_start:annotation.span_end+1]

                new_feature=getattr(tagger,tagger_function)(subtext,*args,**kwargs)
                if new_feature!=None:
                    annotation.features[output_annotation]=new_feature


    return {'adc': adc }

        #
        #     foreach (Document document in adcNew.Documents) {
        #         string contentType = document.Features.GetFeatureValue(documentFeature);
        #         if (contentType == documetnFeatureValue) {
        #             TextBlock[] textBlocks = document.GetAnnotatedBlocks(tba.Annotation);
        #             foreach (TextBlock textBlock in textBlocks) {
        #                 string word = tba.GetText(textBlock);
        #                 string tag = null;
        #                 if (word != null)
        #                     tag = tagFunct(word);
        #                 if (tag != null)
        #                     textBlock.Annotation.Features.SetFeatureValue(outputFeature, tag);
        #             }
        #         }
        #     }
        #     return adcNew;
        # }

def universal_sentence_tagger_hub(input_dict):
    tagger_dict = input_dict['tagger']
    tagger=tagger_dict['object']
    tagger_function=tagger_dict['function']
    args=tagger_dict.get('args',[])
    kwargs=tagger_dict.get('kargs',{})

    group_annotation_name = input_dict['group_annotation']
    element_annotation_name = input_dict['element_annotation']
    output_annotation_name = input_dict['output_feature']
    adc = input_dict['adc']


    for document in adc.documents:
        if document.features['contentType'] == "Text":
            if not document.text:
                pass
            group_annotations=sorted(document.select_annotations(group_annotation_name),key=lambda x: x.span_start)
            element_annotations=sorted(document.select_annotations(element_annotation_name),key=lambda x: x.span_start)

            text_grouped=[] #text_groups= [['First','sentence',['Second','sentance']]
            annotations_grouped=[] #annotations_grouped= [[<Annotation span_start:0 span_ned:4>, <Annotation span_start:6 span_ned:11>],[...

            i=0
            for group_annotation in group_annotations:
                elements=[]
                sentence_annotations=[]
                #find elementary annotations 'contained' in the group_annotation
                while i<len(element_annotations) and element_annotations[i].span_end<=group_annotation.span_end:
                    annotation=element_annotations[i]
                    elements.append(document.text[annotation.span_start:annotation.span_end+1])
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


def nltk_stop_words_tagger(input_dict):
    return {'tagger':
                {'object':StopWordTagger(input_dict.get('stop_words',''),input_dict.get('ignore_case',True)),
                 'function':'tag',
                 #'args': [stop_words],
                 #'kargs':{'ignore_case':ignore_case}
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
