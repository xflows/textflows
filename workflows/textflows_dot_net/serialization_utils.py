import time
from scipy.sparse.csr import csr_matrix
from ..textflows import *
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


#------------------------------------------------------------------------------
# Conversion functions
#------------------------------------------------------------------------------
def ToInt(s):
    try:
        return int(s)
    except:
        return 0
def ToFloat(s):
    try:
        return float(s)
    except:
        return 0
def ToBool(s):
    if s == 'true' or s == 'True':
        return True
    else:
        return False
def ToString(s):
    return s
def ToEnum(typ, s,defaultValue):
    import LatinoInterfaces
    return LatinoInterfaces.LatinoCF.ParseEnum[typ](s, defaultValue)
def ToIntList(s):
    il = []
    for i in s:
        il.append(ToInt(i))
    return il
def ToPyList(l):
    return [x for x in l]
def ToNetList(Type,l):
    import System
    a = System.Array[Type](l)
    return a
def IsSequence(arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))
def Flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)

MAP_TO_PYTHON_OBJECTS=True

def ToNetObj(data):
    import System
    import Latino
    import LatinoInterfaces
    #if hasattr(data, "netObj"):
    #    return data.netObj
    if isinstance(data,LatinoObject):
        return data.load()
    if isinstance(data, dict):
        if not len(data):
            return System.Collections.Generic.Dictionary[System.Object,System.Object]()
        else:
            key = ToNetObj(data.keys()[0])
            val = ToNetObj(data.values()[0])
            for tryIndex in [0, 1]:
                try:
                    if not tryIndex:
                        d = System.Collections.Generic.Dictionary[type(key),type(val)]()
                    else:
                        d = System.Collections.Generic.Dictionary[System.Object,System.Object]()
                    for key,val in data.items():
                        k = ToNetObj(key)
                        v = ToNetObj(val)
                        d[k] = v
                    return d
                except:
                    pass
            return System.Object()
    if isinstance(data, list):
        if not len(data):
            return System.Collections.Generic.List[System.Object]()
        else:
            dataNet = ToNetObj(data[0])
            for tryIndex in [0, 1]:
                try:
                    if not tryIndex:
                        l = System.Collections.Generic.List[type(dataNet)]()
                    else:
                        l = System.Collections.Generic.List[System.Object]()
                    for i, val in enumerate(data):
                        l.Add(ToNetObj(val))
                    return l
                except:
                    pass
            return System.Object()
    if isinstance(data, tuple):
        if not len(data):
            return System.Collections.Generic.LinkedList[System.Object]()
        else:
            dataNet = ToNetObj(data[0])
            for tryIndex in [0, 1]:
                try:
                    if not tryIndex:
                        a = System.Collections.Generic.LinkedList[type(dataNet)]()
                    else:
                        a = System.Collections.Generic.LinkedList[System.Object]()
                    for i, val in enumerate(data):
                        a.AddLast(ToNetObj(val))
                    return a
                except:
                    pass
            return System.Object()
    if MAP_TO_PYTHON_OBJECTS:
        if isinstance(data,Document): #name,text,annotations,features
            d=Latino.Workflows.TextMining.Document(data.name,data.text)
            latino_object_set_feature_values(d,data.features)
            d.AddAnnotations(ToNetObj(data.annotations))

            return d
        elif isinstance(data,Annotation):
            a=Latino.Workflows.TextMining.Annotation(data.span_start,data.span_end,data.type)
            latino_object_set_feature_values(a,data.features)
            return a
        elif isinstance(data,DocumentCorpus):
            d=LatinoInterfaces.DocumentCorpus()
            d.AddRange(ToNetObj(data.documents))
            latino_object_set_feature_values(d,data.features)
            return d
        elif isinstance(data,BowDataset):
            cx=data.sparse_bow_matrix.tocoo() #A sparse matrix in COOrdinate format.

            if data.labels and cx.shape[0]!=len(data.labels):
                raise Exception("Nekaj gnilega je v dezeli Danski, sporoci maticu.")
            sparse_vectors=[ Latino.SparseVector[System.Double]() for _ in range(cx.shape[0])] #empty SparseVectors

            for (i,j,v) in izip(cx.row, cx.col, cx.data):
                sparse_vectors[i][j]=v

            ds=Latino.Model.LabeledDataset[System.String,Latino.SparseVector[System.Double]]()
            for i,ex in enumerate(sparse_vectors):
                label=data.labels[i] if data.labels else ''
                ds.Add(label,ex)

            return ds
        elif isinstance(data,DictionaryProbDist):
            p=Latino.Model.Prediction[System.Double]()
            genType = p.GetType().GetGenericTypeDefinition()
            KeyDats=[]

            for key,score in data._prob_dict.items():
                KeyDats.append(Latino.KeyDat[System.Double,System.String](score,key))
            aaa=Latino.ArrayList[Latino.KeyDat[System.Double,System.String]](ToNetObj(KeyDats))
            p.AddRange(Latino.ArrayList[Latino.KeyDat[System.Double,System.String]](ToNetObj(KeyDats)))

            # elif genType.Equals(Latino.Model.Prediction):
            # probs=dict([(keyDat.Dat,keyDat.Key) for keyDat in data.Inner])
            # return DictionaryProbDist(prob_dict=probs)
            return p
    return data

def latino_object_set_feature_values(latinoObj,features):
    for k,v in features.items():
        latinoObj.Features.SetFeatureValue(k,str(v))
    return None




def ToPyObj(data):
    import System
    import Latino
    import LatinoInterfaces
    if hasattr(data, "GetType") and data.GetType().IsGenericType:
        genType = data.GetType().GetGenericTypeDefinition()
        if genType.Equals(System.Collections.Generic.Dictionary):
            d = {}
            for keyVal in data:
                k = ToPyObj(keyVal.Key)
                v = ToPyObj(keyVal.Value)
                d[k] = v
            return d
        if genType.Equals(System.Collections.Generic.List):
            l = []
            for val in data:
                l.append(ToPyObj(val))
            return l
        if genType.Equals(System.Collections.Generic.LinkedList):
            l = []
            for val in data:
                l.append(ToPyObj(val))
            return tuple(l)
        if MAP_TO_PYTHON_OBJECTS:
            if genType.Equals(Latino.Model.LabeledDataset):
                labels=[]
                row=[]
                col=[]
                values=[]
                for i,labeled_example in enumerate(data): #if genType.Equals(Latino.Model.LabeledExample)
                    labels.append(labeled_example.get_Label())
                    sparse_vector=labeled_example.get_Example()

                    for el in sparse_vector:
                        row.append(i)
                        col.append(el.get_Idx())
                        values.append(el.get_Dat())

                bow_matrix=csr_matrix((values,(row,col)))
                return BowDataset(bow_matrix,labels)
            elif genType.Equals(Latino.Model.Prediction):
                probs=dict([(keyDat.Dat,keyDat.Key) for keyDat in data.Inner])
                return DictionaryProbDist(prob_dict=probs)



    if MAP_TO_PYTHON_OBJECTS and hasattr(data, "GetType"):
        if data.GetType().Equals(LatinoInterfaces.DocumentCorpus):
            return DocumentCorpus([ToPyObj(el) for el in data.Documents],ToPyObj(data.Features))
        if data.GetType().Equals(Latino.Workflows.TextMining.Document):
            return Document(data.Name,data.Text,[ToPyObj(el) for el in data.Annotations],ToPyObj(data.Features))
        if data.GetType().Equals(Latino.Workflows.TextMining.Annotation):
            return Annotation(data.SpanStart,data.SpanEnd,data.Type,ToPyObj(data.Features))
        if data.GetType().Equals(Latino.Workflows.TextMining.Features):
            d = {}
            for keyVal in data:
                k = keyVal.Key
                v = keyVal.Value
                d[k] = v
            return d

    if hasattr(data, "GetType"):
        type = data.GetType()
        if type.IsArray:
            return [ToPyObj(x) for x in data]
        for interface in type.GetInterfaces():
            if interface.Name == u'ISerializable':
                return LatinoObject(data) #if other type of latino object
    return data #usually types like string, list which are converted from c# objects

class SerializableObject:
    netObj = None
    constructor = '<constructor_func_name>'
    def __init__(self, object = None):
        self.netObj = object
        self.copyAttributes()
    def createInstance(self, dict):
        constr = eval(self.constructor)
        args = self.getConstructorArgs(dict)
        self.netObj = constr(*args)
        self.copyAttributes()
    def getConstructorArgs(self, dict):
        if dict.has_key('constructorArgs'):
            return tuple([val for key,val in dict['constructorArgs'].items()])
        return ()
    def copyAttributes(self): #copy all attributes from wrapped object to the wrapper
        pass
        #for attr in dir(self.netObj):
        #    if hasattr(self.netObj, attr) and not hasattr(self, attr):
        #        setattr(self, attr, getattr(self.netObj, attr))
    def __repr__(self):
        #return "<" + self.netObj.__str__() + " wrapped in "+self.__class__.__name__+">"
        return "<" + self.netObj.__str__() + ">"
    def netObj(self):
        return self.netObj
class LatinoSerializableObject(SerializableObject):
    def __getstate__(self):
        logging.info('Serialize {0} with latino serializer (start)'.format(self.netObj.__class__.__name__))
        start = time.clock()
        byteData = LatinoCF.Save(self.netObj)
        elapsed = (time.clock() - start)
        logging.info('Serialize {0} with latino serializer (end, size: {1:,} chars) in {2} ms'.format(self.netObj.__class__.__name__, len(byteData),elapsed))
        return {'byteData': byteData}
    def __setstate__(self, dict):
        logging.info('Deserialize {0} with latino deserializer (start)'.format("<LatinoObject>"))
        start = time.clock()
        self.netObj = LatinoCF.Load(dict['byteData'])
        self.copyAttributes()
        elapsed = (time.clock() - start)
        logging.info('Deserialize {0} with latino deserializer (end, size: {1:,} chars) in {2} ms'.format(self.netObj.__class__.__name__, len(dict['byteData']),elapsed))
    def __repr__(self):
        return "<LSO: " + self.netObj.__str__() + ">"