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
    def __init__(self, spanStart,spanEnd,type1,features={}):
        self.features=features
        self.span_start=spanStart
        self.span_end=spanEnd
        self.type=type1