from itertools import izip
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB


class DocumentCorpus:
    def __init__(self, documents,features):
        self.documents=documents
        self.features=features
    def __unicode__(self):
        #for i in itemDir:
        return 'Documents; {0}' % (self.documents)


class Document:
    def __init__(self, name,text,annotations,features):
        self.annotations=annotations
        self.features=features
        self.name=name

        self.text=text

    def __unicode__(self):
        return 'Name; {0}\nText: {1}' % (self.name, self.text)

    def get_annotations_with_text(self, selector):
        """
        :param selector: textual string in one of the following formats:
           a) annotation_name
           b) annotation_name/feature_name       so you can do for instance stopword tagging on lemmas
        :return: list of selected (annotation,text) tuples
        """
        annotations_with_text = []
        selector_split = selector.split("/")
        element_annotation = selector_split[0].strip()
        element_feature = False if len(selector_split) == 1 else selector_split[1].strip()

        for a in self.annotations:
            if a.type == element_annotation:
                try:
                    if element_feature:
                            text = a.features[element_feature]
                    else:
                        text = self.text[a.span_start:a.span_end+1]
                    annotations_with_text.append((a, text))
                except KeyError:
                     #raise KeyError("The Annotation (%s) does not have feature named '%s'!" % (a.__str__(), element_feature))
                     pass
        return annotations_with_text

    def raw_text(self,selector=None,stop_word_feature_name="StopWord",join_annotations_with=" "):
        if not selector:
            return self.text
        else:
            selected_subtexts=[text for (ann,text) in self.get_annotations_with_text(selector)
                               if not ann.features.has_key(stop_word_feature_name)]
            return join_annotations_with.join(selected_subtexts)

    def get_first_label(self,classes):
        for klass in classes:
            if klass in self.features:
                return klass


class Annotation:
    def __init__(self, span_start, span_end, type, features=None):
        self.features=features or {}
        self.span_start=span_start
        self.span_end=span_end
        self.type=type
    def __repr__(self):
        return '<Annotation span_start:%d span_ned:%d>' % (self.span_start, self.span_end)

    def __unicode__(self):
        return 'span_start: %d, span_ned: %d' % (self.span_start, self.span_end)
    def __str__(self):
        return unicode(self).encode('utf-8')


class BowDataset:
    def __init__(self,sparse_bow_matrix,labels=None):
        self.sparse_bow_matrix=sparse_bow_matrix
        self.labels=labels

    @classmethod
    def from_raw_documents(cls,documents,bow_vectorizer,labels=None):
        sparse_bow_matrix = bow_vectorizer.transform(documents)
        return cls(sparse_bow_matrix,labels)

    @classmethod
    def from_adc(cls,adc,bow_model):
        sparse_bow_matrix = bow_model.vectorizer.transform(bow_model.get_raw_text(adc.documents))
        labels=bow_model.get_labels(adc)

        return cls(sparse_bow_matrix,labels)

    def sparce_bow_matrix(self):
        return self.sparse_bow_matrix
    def dense_bow_matrix(self):
        return self.sparse_bow_matrix.toarray()

    def nltk_dataset_with_labels(self):
        train_data=[({},label) for label in self.labels]
        cx=self.sparse_bow_matrix.tocoo() #A sparse matrix in COOrdinate format.
        if cx.shape[0]!=len(self.labels):
            raise Exception("Nekaj gnilega je v dezeli Danski, sporoci maticu.")
        for (i,j,v) in izip(cx.row, cx.col, cx.data):
            train_data[i][0][j]=v   #seting the dict in (list(tuple(dict, str)))
        return train_data

    def nltk_dataset_without_labels(self):
        cx=self.sparse_bow_matrix.tocoo() #A sparse matrix in COOrdinate format.
        train_data=[{} for _ in range(cx.shape[0])]
        for (i,j,v) in izip(cx.row, cx.col, cx.data):
            train_data[i][j]=v   #seting the dict in (list(dict))
        return train_data

    def bow_in_proper_format(self,classifier,no_labels=False):
        #check if classifier can deal with sparse data
        if isinstance(classifier,NltkClassifier):
            return self.nltk_dataset_without_labels() if no_labels else self.nltk_dataset_with_labels()
        elif isinstance(classifier, (GaussianNB, MultinomialNB,  DecisionTreeClassifier)):
            return self.dense_bow_matrix()
        else: #if latino classifier or a classifier that can deal with sparse data
            return self.sparse_bow_matrix

# try:
#     from nltk.classify import scikitlearn
#     from sklearn.feature_extraction.text import TfidfTransformer
#     from sklearn.pipeline import Pipeline
#     from sklearn import ensemble, feature_selection, linear_model, naive_bayes, neighbors, svm, tree
#
#     classifiers = [
#         ensemble.ExtraTreesClassifier,
#         ensemble.GradientBoostingClassifier,
#         ensemble.RandomForestClassifier,
#         linear_model.LogisticRegression,
#         #linear_model.SGDClassifier, # NOTE: this seems terrible, but could just be the options
#         naive_bayes.BernoulliNB,
#         naive_bayes.GaussianNB,
#         naive_bayes.MultinomialNB,
#         neighbors.KNeighborsClassifier,  # TODO: options for nearest neighbors
#         svm.LinearSVC,
#         svm.NuSVC,
#         svm.SVC,
#         tree.DecisionTreeClassifier,
#     ]


class BowModel:
    def __init__(self,adc,token_annotation,stem_feature_name,stop_word_feature_name,label_doc_feature_name):
        self._label_feature_name=token_annotation
        self._token_annotation=token_annotation
        self._stem_feature_name=stem_feature_name
        self._stop_word_feature_name=stop_word_feature_name
        self._label_doc_feature_name=label_doc_feature_name


        self.vectorizer =TfidfVectorizer() #DictVectorizer(dtype=dtype, sparse=sparse)
        raw_documents=self.get_raw_text(adc.documents)
        self.vectorizer.fit(raw_documents)
        self._vocab_to_idx=self.vectorizer.vocabulary_
        self._idx_to_vocab = {v: k for k, v in self._vocab_to_idx.items()}


    def get_raw_text(self,documents):
        feature_name=self._token_annotation+('/'+self._stem_feature_name if self._stem_feature_name else '')
        return [document.raw_text(self._token_annotation,feature_name) for document in documents]

    def get_labels(self,adc):
        return [doc.features.get(self._label_feature_name,'') for doc in adc.documents] if self._label_feature_name else None


#BowSpace
        # private ITokenizer mTokenizer
        #     = new UnicodeTokenizer();
        # private Set<string>.ReadOnly mStopWords
        #     = null;
        # private IStemmer mStemmer
        #     = null;
        # private Dictionary<string, Word> mWordInfo
        #     = new Dictionary<string, Word>();
        # private ArrayList<Word> mIdxInfo
        #     = new ArrayList<Word>();
        # private int mMaxNGramLen
        #     = 2;
        # private int mMinWordFreq
        #     = 5;
        # private WordWeightType mWordWeightType
        #     = WordWeightType.TermFreq;
        # private double mCutLowWeightsPerc
        #     = 0.2;
        # private bool mNormalizeVectors
        #     = true;
        # private bool mKeepWordForms
        #     = false;


class NltkCorpus():
    """ Wrapper for Nltk corpora. In Nltk 3.x Nltk corpora is not picklable.
    """
    corpus_name=""
    corpus=None
    _corpus_methods=[]
    def __init__(self,name):
        self.corpus_name=name
        self._corpus_methods=dir(getattr(nltk.corpus,self.corpus_name))

    def _corpus(self):
        self.corpus = self.corpus or getattr(nltk.corpus,self.corpus_name)
        return self.corpus

    def __getattr__(self, name):
        if not name in self._corpus_methods:
            raise AttributeError
        else:
            def method():
                return getattr(self._corpus(),name)()
            return method


class NltkRegexpTokenizer():
    """ Wrapper for Nltk RegexTokenizer. Python's regular expressions are not picklable.
    """
    _pattern=''
    _kargs={}

    def __init__(self,pattern,**kargs):
        self._pattern=pattern
        self._kargs=kargs

    def span_tokenize(self,text):
        return nltk.RegexpTokenizer(self._pattern,**self._kargs).span_tokenize(text)

class NltkRegexpStemmer():
    """ Wrapper for Nltk RegexStemmer. Python's regular expressions are not picklable.
    """
    _pattern=''
    _kargs={}

    def __init__(self,pattern,**kargs):
        self._pattern=pattern
        self._kargs=kargs

    def stem(self,text):
        return nltk.stem.RegexpStemmer(self._pattern,**self._kargs).stem(text)


class NltkClassifier():
    """ This is a wrapper for Nltk classifiers. Nltk classifiers do not have an appropriate __init__
        method which could save kargs and use them latter when .train(train_data) is called.
    """
    _classifier=None
    _kargs={}

    def __init__(self,csf,**kargs):
        self._classifier=csf
        self._kargs=kargs

    def train(self,training_data):
        self._classifier=self._classifier.train(training_data,**self._kargs)
        return self

    def prob_classify_many(self,testing_dataset):
        return self._classifier.prob_classify_many(testing_dataset)

    def __repr__(self):
        return '<NltkClassifier object for %s>' % (self._classifier)


class LatinoObject:
    def __init__(self,latino_object):
        import LatinoInterfaces
        self.serialized_object = LatinoInterfaces.LatinoCF.Save(latino_object)
        self.name=latino_object.__str__()

    def __repr__(self):
        return "<LatinoObject: " + self.name + ">"

    def load(self):
        import LatinoInterfaces
        return LatinoInterfaces.LatinoCF.Load(self.serialized_object)


from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize import TextTilingTokenizer
from nltk.tokenize import TreebankWordTokenizer


class SpanTokenizeMixin():

    def span_tokenize(self, s):
        r"""
        Return the offsets of the tokens in *s*, as a sequence of ``(start, end)``
        tuples, by splitting the string at each successive match of *regexp*.

            >>> from workflows.textflows import StanfordTokenizer
            >>> s = '''Good muffins cost $3.88\nin New York.  Please buy me
            ... two of them.\n\nThanks.'''
            >>> list(StanfordTokenizer().span_tokenize(s))
            [(0, 4), (5, 12), (13, 17), (18, 23), (24, 26), (27, 30), (31, 36),
            (38, 44), (45, 48), (49, 51), (52, 55), (56, 58), (59, 64), (66, 73)]

        :param s: the string to be tokenized
        :type s: str
        :rtype: iter(tuple(int, int))
        """
        tokens = self.tokenize(s)
        right = 0

        for token in tokens:
            left = right + s[right:].find(token)
            right = left + len(token)
            yield left, right


class StanfordTokenizer(SpanTokenizeMixin, StanfordTokenizer):
    pass


class TextTilingTokenizer(SpanTokenizeMixin, TextTilingTokenizer):
    pass


class TreebankWordTokenizer(SpanTokenizeMixin, TreebankWordTokenizer):
    pass



def simulate_cf_pickling(obj_to_pickle,compress_object=False):
    from base64 import b64encode, b64decode
    from zlib import compress, decompress
    from cPickle import dumps,loads

    if not compress_object:
        return loads(b64decode(b64encode(dumps(obj_to_pickle))))
    else:
        return loads(decompress(b64decode(b64encode(compress(dumps(obj_to_pickle))))))

#python manage.py export_package workflows/nltoolkit/db/package_data.json nltoolkit
#python manage.py celery worker -l info
