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
        annotations_with_text=[]
        selector_split=selector.split("/")
        element_annotation=selector_split[0].strip()
        element_feature=False if len(selector_split)==1 else selector_split[1].strip()

        for a in self.annotations:
            if a.type== element_annotation:
                if element_feature:
                    try:
                        text=a.features[element_feature]
                    except KeyError:
                        text='Feature does not exist!'
                else:
                    text=self.text[a.span_start:a.span_end+1]
                annotations_with_text.append((a, text))
        return annotations_with_text


class Annotation:
    def __init__(self, span_start, span_end, type, features={}):
        self.features=features
        self.span_start=span_start
        self.span_end=span_end
        self.type=type
    def __repr__(self):
        return '<Annotation span_start:%d span_ned:%d>' % (self.span_start, self.span_end)

    def __unicode__(self):
        return 'span_start; %d\tspan_ned: %d' % (self.span_start, self.span_end)
    def __str__(self):
        return unicode(self).encode('utf-8')


import nltk
class NltkCorpus(object):
    corpus_name=""
    corpus=None
    def __init__(self,name):
        self.corpus_name=name

    def _corpus(self):
        self.corpus = self.corpus or getattr(nltk.corpus,self.corpus_name)
        return self.corpus

    def __getattr__(self, name):
        if name.startswith("__"):
            raise AttributeError
        else:
            def method():
                return getattr(self._corpus(),name)()
            return method
