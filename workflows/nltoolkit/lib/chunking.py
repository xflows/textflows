import nltk
from workflows.textflows import *
from tagging_common import universal_word_tagger_hub
#from tagging_common_parallel import universal_word_tagger_hub


def chunking_hub(input_dict):
    adc = input_dict['adc']
    chunker_dict = input_dict['chunker']
    chunker = input_dict['chunker']['object']
    chunker_function = input_dict['chunker']['function']
    output_annotation = input_dict['output_feature']
    input_annotation = input_dict['input_feature']
    args = chunker_dict.get('args',[])
    kwargs = chunker_dict.get('kargs',{})

    for doc in adc.documents:
        if doc.features['contentType'] == "Text":
            if not doc.text:
                pass
            group_annotations=sorted(doc.get_annotations_with_text("Sentence"),key=lambda x: x[0][0])
            element_annotations=sorted(doc.get_annotations_with_text('Token'),key=lambda x: x[0][0])

            text_grouped=[] #text_groups= [['First','sentence',['Second','sentance']]
            annotations_grouped=[] #annotations_grouped= [[<Annotation span_start:0 span_ned:4>, <Annotation span_start:6 span_ned:11>],[...

            i=0
            for group_annotation,_ in group_annotations:
                sentence_annotations=[]
                #find elementary annotations 'contained' in the group_annotation
                while i<len(element_annotations) and element_annotations[i][0][1]<=group_annotation[1]:
                    annotation_list=element_annotations[i][0][3]
                    annotation = ""
                    for name, value in annotation_list:
                        if name == input_annotation:
                            annotation = value
                            break
                    text_block=element_annotations[i][1]
                    sentence_annotations.append((text_block, annotation))
                    i+=1
                annotations_grouped.append(sentence_annotations)
                #print list(izip(annotations_grouped, text_grouped))
            new_features=[getattr(chunker,chunker_function)(tagged_sentence,*args,**kwargs) for tagged_sentence in annotations_grouped]
            for annotation, chunk in izip(group_annotations, new_features):
                annotation[0][3].append((output_annotation, chunk)) #[0:number_of_letters]

    return {'adc': adc }

# Chunkers
def regex_parser(input_dict):
    grammar = input_dict['grammar']
    """
    regex parser, requires grammar as input
    """
    return {'chunker':
                {'object': nltk.RegexpParser(grammar),
                 'function': 'parse', }
    }

def tags_since_dt(sentence, i):
    tags = set()
    for word, pos in sentence[:i]:
        if pos == 'DT':
            tags = set()
        else:
            tags.add(pos)
    return '+'.join(sorted(tags))


def npchunk_features(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = "<START>", "<START>"
    else:
        prevword, prevpos = sentence[i-1]
    if i == len(sentence)-1:
        nextword, nextpos = "<END>", "<END>"
    else:
        nextword, nextpos = sentence[i+1]
    return {"pos": pos,
            "word": word,
            "prevpos": prevpos,
            "nextpos": nextpos,
            "prevpos+pos": "%s+%s" % (prevpos, pos),
            "pos+nextpos": "%s+%s" % (pos, nextpos),
            "tags-since-dt": tags_since_dt(sentence, i)}


class ConsecutiveNPChunkTagger(nltk.TaggerI):

    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append( (featureset, tag))
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)


class ClassifierBasedChunkParser(nltk.ChunkParserI):
    def __init__(self, train_sents):
        tagged_sents = [[((w,t),c) for (w,t,c) in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)


from nltk.corpus import conll2000

def classifier_based_parser(input_dict):
    train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
    classifier_based_chunker = ClassifierBasedChunkParser(train_sents)
    return {'chunker':
                {'object': classifier_based_chunker,
                 'function': 'parse', }
    }