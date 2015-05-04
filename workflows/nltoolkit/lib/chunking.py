from itertools import izip
from nltk.corpus import conll2000
from nltk.tag.sequential import DefaultTagger
from nltk.tag.sequential import NgramTagger
from workflows.nltoolkit.lib.part_of_speech_tagging import corpus_reader
from workflows.nltoolkit.lib.tagging_common import universal_sentence_tagger_hub
from workflows.textflows import Annotation

__author__ = 'mperice'

import nltk.tag
from nltk.chunk import ChunkParserI
from nltk.chunk.util import conlltags2tree, tree2conlltags
from nltk.tag import UnigramTagger, BigramTagger, ClassifierBasedTagger

from nltk.tree import Tree
import nltk

class TagChunker(ChunkParserI):
    '''Chunks tagged tokens using Ngram Tagging.'''
    def __init__(self, tagger_class, args,kargs): #=[UnigramTagger, BigramTagger]):
        '''Train Ngram taggers on chunked sentences'''
        self.tagger = tagger_class(*args,**kargs)

    def parse(self, tagged_sent):
        '''Parsed tagged tokens into parse Tree of chunks'''
        if not tagged_sent: return None
        (words, tags) = zip(*tagged_sent)
        chunks = self.tagger.tag(tags)
        # create conll str for tree parsing
        print chunks
        return conlltags2tree([(w,t,c) for (w,(t,c)) in zip(words, chunks)])

def nltk_ngram_chunker(input_dict):

    training_corpus=corpus_reader(input_dict['training_corpus'],'chunked_sents')
    backoff_tagger=input_dict['backoff_chunker']['object'] if input_dict['backoff_chunker'] else DefaultTagger('-None-')
    n=int(input_dict['n']) #default 2
    #cutoff=int(input_dict['cutoff']) #default 0 'backoff': backoff_tagger,
    return {'chunker': TagChunker(NgramTagger,[1],{'train': training_corpus})}



def nltk_regex_chunker(input_dict):
    """
    A grammar based chunk parser.  ``chunk.RegexpParser`` uses a set of
    regular expression patterns to specify the behavior of the parser.
    The chunking of the text is encoded using a ``ChunkString``, and
    each rule acts by modifying the chunking in the ``ChunkString``.
    The rules are all implemented using regular expression matching
    and substitution.

    A grammar contains one or more clauses in the following form::

     NP:
       {<DT|JJ>}          # chunk determiners and adjectives
       }<[\.VI].*>+{      # chink any tag beginning with V, I, or .
       <.*>}{<DT>         # split a chunk at a determiner
       <DT|JJ>{}<NN.*>    # merge chunk ending with det/adj
                          # with one starting with a noun

    The patterns of a clause are executed in order.  An earlier
    pattern may introduce a chunk boundary that prevents a later
    pattern from executing.  Sometimes an individual pattern will
    match on multiple, overlapping extents of the input.  As with
    regular expression substitution more generally, the chunker will
    identify the first match possible, then continue looking for matches
    after this one has ended.

    The clauses of a grammar are also executed in order.  A cascaded
    chunk parser is one having more than one clause.  The maximum depth
    of a parse tree created by this chunk parser is the same as the
    number of clauses in the grammar.

    When tracing is turned on, the comment portion of a line is displayed
    each time the corresponding pattern is applied.

    :type _start: str
    :ivar _start: The start symbol of the grammar (the root node of
        resulting trees)
    :type _stages: int
    :ivar _stages: The list of parsing stages corresponding to the grammar

    """


    grammar = r"""
      NP:
        {<.*>+}          # Chunk everything
        }<VBD|IN>+{      # Chink sequences of VBD and IN
      """
    #grammar=input_dict['grammar']
    chunker = nltk.RegexpParser(grammar)


    return {'chunker': chunker}


def chunking_hub(input_dict):
    chunker=input_dict['chunker']

    group_annotation_name = input_dict['group_annotation']
    element_annotation_name = input_dict['element_annotation']
    element_pos_feature_name = input_dict['element_pos_feature_name']
    output_annotation_name = input_dict['output_feature']


    adc = input_dict['adc']


    for doc in adc.documents:
        if doc.features['contentType'] == "Text":
            if not doc.text:
                pass
            text_grouped,annotations_grouped=doc.get_grouped_annotations_with_texts(element_annotation_name,group_annotation_name)

            for element_texts,element_annotations in izip(text_grouped,annotations_grouped):
                tagged_sent=zip(element_texts,[ann.features[element_pos_feature_name] for ann in element_annotations])
                tree=chunker.parse(tagged_sent) #generate a tree
                conll_tags= nltk.chunk.tree2conlltags(tree) #convert to IOB tags

                for iob_tag,annotation in izip([a[2] for a in conll_tags],element_annotations):
                    annotation.features[output_annotation_name]=iob_tag

            #for sentence_features, sentence_annotations in izip(new_features,annotations_grouped):
            #    for feature,annotation in izip(sentence_features,sentence_annotations):
            #        annotation.features[output_annotation_name]=feature[1] #[0:number_of_letters]


    return {'adc': adc}


def extract_annotations_from_IOB_tags(input_dict):
    group_annotation_name = input_dict['group_annotation']
    element_annotation_name = input_dict['element_annotation']
    element_iob_feature_name = input_dict['element_iob_feature_name']
    element_pos_feature_name = input_dict['element_pos_feature_name']

    output_annotation_name = input_dict['output_annotation']
    labels=set([l.strip() for l in input_dict['labels'].split(",")])

    adc = input_dict['adc']


    for doc in adc.documents:
        if doc.features['contentType'] == "Text":
            if not doc.text:
                pass
            _,annotations_grouped=doc.get_grouped_annotations_with_texts(element_annotation_name,group_annotation_name)

            for element_annotations in annotations_grouped:
                conll_tags=[(ann,ann.features[element_pos_feature_name],ann.features[element_iob_feature_name])
                            for ann in element_annotations]

                tree=nltk.chunk.conlltags2tree(conll_tags)

                for label in labels:
                    for subtree in tree.subtrees(filter=lambda t: t.label()==label):
                        # print the noun phrase as a list of part-of-speech tagged words
                        leaves= subtree.leaves()
                        doc.annotations.append(Annotation(leaves[0][0].span_start,leaves[-1][0].span_end,
                                                          output_annotation_name+"_"+label,
                                                          features={'Chunk Label': subtree.label()}))

                #for iob_tag,annotation in izip([a[2] for a in aaa],element_annotations):
                #    annotation.features[output_annotation_name]=iob_tag

            #for sentence_features, sentence_annotations in izip(new_features,annotations_grouped):
            #    for feature,annotation in izip(sentence_features,sentence_annotations):
            #        annotation.features[output_annotation_name]=feature[1] #[0:number_of_letters]


    return {'adc': adc}





def flatten_deeptree(tree):
    '''
    >>> flatten_deeptree(Tree('S', [Tree('NP-SBJ', [Tree('NP', [Tree('NNP', ['Pierre']), Tree('NNP', ['Vinken'])]), Tree(',', [',']), Tree('ADJP', [Tree('NP', [Tree('CD', ['61']), Tree('NNS', ['years'])]), Tree('JJ', ['old'])]), Tree(',', [','])]), Tree('VP', [Tree('MD', ['will']), Tree('VP', [Tree('VB', ['join']), Tree('NP', [Tree('DT', ['the']), Tree('NN', ['board'])]), Tree('PP-CLR', [Tree('IN', ['as']), Tree('NP', [Tree('DT', ['a']), Tree('JJ', ['nonexecutive']), Tree('NN', ['director'])])]), Tree('NP-TMP', [Tree('NNP', ['Nov.']), Tree('CD', ['29'])])])]), Tree('.', ['.'])]))
    Tree('S', [Tree('NP', [('Pierre', 'NNP'), ('Vinken', 'NNP')]), (',', ','), Tree('NP', [('61', 'CD'), ('years', 'NNS')]), ('old', 'JJ'), (',', ','), ('will', 'MD'), ('join', 'VB'), Tree('NP', [('the', 'DT'), ('board', 'NN')]), ('as', 'IN'), Tree('NP', [('a', 'DT'), ('nonexecutive', 'JJ'), ('director', 'NN')]), Tree('NP-TMP', [('Nov.', 'NNP'), ('29', 'CD')]), ('.', '.')])
    '''
    return Tree(tree.lable(), flatten_childtrees([c for c in tree]))

def flatten_childtrees(trees):
    children = []

    for t in trees:
        if t.height() < 3:
            children.extend(t.pos())
        elif t.height() == 3:
            children.append(Tree(t.label(), t.pos()))
        else:
            children.extend(flatten_childtrees([c for c in t]))

    return children

def shallow_tree(tree):
    '''
    >>> shallow_tree(Tree('S', [Tree('NP-SBJ', [Tree('NP', [Tree('NNP', ['Pierre']), Tree('NNP', ['Vinken'])]), Tree(',', [',']), Tree('ADJP', [Tree('NP', [Tree('CD', ['61']), Tree('NNS', ['years'])]), Tree('JJ', ['old'])]), Tree(',', [','])]), Tree('VP', [Tree('MD', ['will']), Tree('VP', [Tree('VB', ['join']), Tree('NP', [Tree('DT', ['the']), Tree('NN', ['board'])]), Tree('PP-CLR', [Tree('IN', ['as']), Tree('NP', [Tree('DT', ['a']), Tree('JJ', ['nonexecutive']), Tree('NN', ['director'])])]), Tree('NP-TMP', [Tree('NNP', ['Nov.']), Tree('CD', ['29'])])])]), Tree('.', ['.'])]))
    Tree('S', [Tree('NP-SBJ', [('Pierre', 'NNP'), ('Vinken', 'NNP'), (',', ','), ('61', 'CD'), ('years', 'NNS'), ('old', 'JJ'), (',', ',')]), Tree('VP', [('will', 'MD'), ('join', 'VB'), ('the', 'DT'), ('board', 'NN'), ('as', 'IN'), ('a', 'DT'), ('nonexecutive', 'JJ'), ('director', 'NN'), ('Nov.', 'NNP'), ('29', 'CD')]), ('.', '.')])
    '''
    children = []

    for t in tree:
        if t.height() < 3:
            children.extend(t.pos())
        else:
            children.append(Tree(t.label(), t.pos()))

    return Tree(tree.label(), children)



#####################
## tree conversion ##
#####################

def chunk_trees2train_chunks(chunk_sents):
    tag_sents = [tree2conlltags(sent) for sent in chunk_sents]
    return [[((w,t),c) for (w,t,c) in sent] for sent in tag_sents]

def conll_tag_chunks(chunk_sents):
    '''Convert each chunked sentence to list of (tag, chunk_tag) tuples,
    so the final result is a list of lists of (tag, chunk_tag) tuples.
    >>> from nltk.tree import Tree
    >>> t = Tree('S', [Tree('NP', [('the', 'DT'), ('book', 'NN')])])
    >>> conll_tag_chunks([t])
    [[('DT', 'B-NP'), ('NN', 'I-NP')]]
    '''
    tagged_sents = [tree2conlltags(tree) for tree in chunk_sents]
    return [[(t, c) for (w, t, c) in sent] for sent in tagged_sents]

def ieertree2conlltags(tree, tag=nltk.tag.pos_tag):
    # tree.pos() flattens the tree and produces [(word, label)] where label is
    # from the word's parent tree label. words in a chunk therefore get the
    # chunk tag, while words outside a chunk get the same tag as the tree's
    # top label
    words, ents = zip(*tree.pos())
    iobs = []
    prev = None
    # construct iob tags from entity names
    for ent in ents:
        # any entity that is the same as the tree's top label is outside a chunk
        if ent == tree.label():
            iobs.append('O')
            prev = None
        # have a previous entity that is equal so this is inside the chunk
        elif prev == ent:
            iobs.append('I-%s' % ent)
        # no previous equal entity in the sequence, so this is the beginning of
        # an entity chunk
        else:
            iobs.append('B-%s' % ent)
            prev = ent
    # get tags for each word, then construct 3-tuple for conll tags
    words, tags = zip(*tag(words))
    return zip(words, tags, iobs)

#################
## tag chunker ##
#################

# def chunk_tagger_hub:
#     train_sents = conll_tag_chunks(train_chunks)
#     self.tagger = None
#
#     for cls in tagger_classes:
#         self.tagger = cls(train_sents, backoff=self.tagger)




brown = nltk.corpus.brown
########################
## classifier chunker ##
########################

def prev_next_pos_iob(tokens, index, history):
    word, pos = tokens[index]

    if index == 0:
        prevword, prevpos, previob = ('<START>',)*3
    else:
        prevword, prevpos = tokens[index-1]
        previob = history[index-1]

    if index == len(tokens) - 1:
        nextword, nextpos = ('<END>',)*2
    else:
        nextword, nextpos = tokens[index+1]

    feats = {
        'word': word,
        'pos': pos,
        'nextword': nextword,
        'nextpos': nextpos,
        'prevword': prevword,
        'prevpos': prevpos,
        'previob': previob
    }

    return feats

class ClassifierChunker(ChunkParserI):
    def __init__(self, train_sents, feature_detector=prev_next_pos_iob, **kwargs):
        if not feature_detector:
            feature_detector = self.feature_detector

        train_chunks = chunk_trees2train_chunks(train_sents)
        self.tagger = ClassifierBasedTagger(train=train_chunks,
            feature_detector=feature_detector, **kwargs)

    def parse(self, tagged_sent):
        if not tagged_sent: return None
        chunks = self.tagger.tag(tagged_sent)
        return conlltags2tree([(w,t,c) for ((w,t),c) in chunks])

#############
## pattern ##
#############

# class PatternChunker(ChunkParserI):
# 	def parse(self, tagged_sent):
# 		# don't import at top since don't want to fail if not installed
# 		from pattern.en import parse
# 		s = ' '.join([word for word, tag in tagged_sent])
# 		# not tokenizing ensures that the number of tagged tokens returned is
# 		# the same as the number of input tokens
# 		sents = parse(s, tokenize=False).split()
# 		if not sents: return None
# 		return conlltags2tree([(w, t, c) for w, t, c, p in sents[0]])


