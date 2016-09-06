import multiprocessing
from functools import partial

from workflows.textflows import *


def tag_document(document,tagger,tagger_function,args,kwargs,input_annotation,output_annotation):
    if document.features['contentType'] == "Text":
        if not document.text:
            pass
        for annotation,subtext in document.get_annotations_with_text(input_annotation): #all annotations of this type
            if subtext:
                new_feature=getattr(tagger,tagger_function)(subtext,*args,**kwargs)
                if new_feature!=None:
                    annotation[3].append((output_annotation, new_feature))
    return document

def universal_word_tagger_hub(adc,tagger_dict,input_annotation,output_annotation):
    tagger=tagger_dict['object']
    tagger_function=tagger_dict['function']
    args=tagger_dict.get('args',[])
    kwargs=tagger_dict.get('kargs',{})

    #pool = multiprocessing.Pool(processes=multiprocessing.cpu_count(), maxtasksperchild=1000)

    print "evo nas!!!"
    #parallel for document in adc.documents:
    adc.documents = [tag_document(document, tagger, tagger_function, args, kwargs, input_annotation, output_annotation) for document in adc.documents]
    '''new_documents=pool.map(
        partial(tag_document,
                tagger=tagger,
                tagger_function=tagger_function,
                args=args,
                kwargs=kwargs,
                input_annotation=input_annotation,
                output_annotation=output_annotation),
        adc.documents,
        100 #chunksize, constructs list of this size which are passed to pool workers
    )
    pool.close()
    pool.join()'''
    #adc.documents=new_documents #list(new_documents)

    print "dijo!2!!"

    return {'adc': adc }

def sentance_tag_a_document(doc,tagger,tagger_function,args,kwargs,
                            element_annotation_name,group_annotation_name,output_annotation_name):

    if doc.features['contentType'] == "Text":
        if not doc.text:
            pass
        group_annotations=sorted(doc.get_annotations_with_text(group_annotation_name),key=lambda x: x[0][0])
        element_annotations=sorted(doc.get_annotations_with_text(element_annotation_name),key=lambda x: x[0][0])

        text_grouped=[] #text_groups= [['First','sentence',['Second','sentance']]
        annotations_grouped=[] #annotations_grouped= [[<Annotation span_start:0 span_ned:4>, <Annotation span_start:6 span_ned:11>],[...

        i=0
        for group_annotation,_ in group_annotations:
            elements=[]
            sentence_annotations=[]
            #find elementary annotations 'contained' in the group_annotation
            while i<len(element_annotations) and element_annotations[i][0][1]<=group_annotation[1]:
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
                annotation[3].append((output_annotation_name, feature[1]))
    return doc



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


    #pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    adc.documents = [sentance_tag_a_document(document, tagger, tagger_function, args, kwargs, element_annotation_name, group_annotation_name, output_annotation_name) for document in adc.documents]
    print "evo nas!!!"
    #parallel for document in adc.documents:
    '''new_documents=pool.map(
        partial(sentance_tag_a_document,
                tagger=tagger,
                tagger_function=tagger_function,
                args=args,
                kwargs=kwargs,
                element_annotation_name=element_annotation_name,
                group_annotation_name=group_annotation_name,
                output_annotation_name=output_annotation_name),
        adc.documents,
        100 #chunksize, constructs list of this size which are passed to pool workers
    )
    pool.close()
    pool.join()
    adc.documents=new_documents'''
    print "dijo!!!"
    return {'adc': adc }




# def chunks(l, n):
#     c=[[] for _ in range(n)]
#     for i in range(l):
#         c[i%n].append(i)
#     return c
#
# print chunks(10,6)
#
# from multiprocessing import Process, Value, Array, Pool
#
# def f(a,indices):
#     for i in indices:
#         a[i] = -a[i]
#
# if __name__ == '__main__':
#     a=[[i] for i in range(100)]
#     arr = Array('i', a)
#
#     no_of_workers=6
#     workers=[Process(target=f, args=(arr, indices)) for indices in chunks(len(arr),no_of_workers)]
#
#
#     for p in workers:
#         p.start()
#     for p in workers:
#         p.join()
#
#     print arr[:]
#     print a
#
#
#     #pool = multiprocessing.Pool(processes=6)
#     #case_data = RAW_DATASET
#     #pool.apply(f, args=(num, arr))
#     #pool.close()
#     #pool.join()
