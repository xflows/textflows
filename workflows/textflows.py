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
        #for i in itemDir:
        return 'Name; {0}\nText: {1}' % (self.name, self.text)

    def select_annotations(self, selector):
        return [a for a in self.annotations if a.type== selector]  #self.text ???
    def get_annotated_blocks(self,selector):
        annotations=self.select_annotations(selector)



class Annotation:
    def __init__(self, span_start,span_end,type1,features={}):
        self.features=features
        self.span_start=span_start
        self.span_end=span_end
        self.type=type1
    def __repr__(self):
        return '<Annotation span_start:%d span_ned:%d>' % (self.span_start, self.span_end)

    def __unicode__(self):
        return 'span_start; %d\tspan_ned: %d' % (self.span_start, self.span_end)
    def __str__(self):
        return unicode(self).encode('utf-8')