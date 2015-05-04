from workflows.textflows import *

def universal_word_tagger_hub(adc,tagger_dict,input_annotation,output_annotation):
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
            text_grouped,annotations_grouped=doc.get_grouped_annotations_with_texts(element_annotation_name,group_annotation_name)

            new_features=getattr(tagger,tagger_function)(text_grouped,*args,**kwargs)
            for sentence_features, sentence_annotations in izip(new_features,annotations_grouped):
                for feature,annotation in izip(sentence_features,sentence_annotations):
                    annotation.features[output_annotation_name]=feature[1] #[0:number_of_letters]

    return {'adc': adc }