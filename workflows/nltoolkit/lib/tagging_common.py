from workflows.textflows import *

def universal_word_tagger_hub(adc,tagger_dict,input_annotation,output_annotation, pos_annotation=None):
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
                    if pos_annotation:
                        if pos_annotation in annotation.features:
                            kwargs['pos_tag'] = annotation.features[pos_annotation]
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
                    annotation.features[output_annotation_name]=feature[1] #[0:number_of_letters]

    return {'adc': adc }