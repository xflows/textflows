from workflows.textflows import *

def tokenizer_hub(input_dict):
    tokenizer_dict = input_dict['tokenizer']

    if type(tokenizer_dict)!=dict:
        from ...latino.library_gen import latino_tokenize_words
        return latino_tokenize_words(input_dict)
    else:
        tokenizer_class=tokenizer_dict['object']
        args=tokenizer_dict.get('args',[])
        kwargs=tokenizer_dict.get('kargs',{})
        input_annotation = input_dict['inputAnnotation']
        output_annotation = input_dict['outputAnnotation']
        adc = input_dict['adc']
        for document in adc.documents:
            if document.features['contentType'] == "Text":
                if not document.text:
                    pass
                for annotation in document.select_annotations(input_annotation): #all annotations of this type
                    subtext = document.text[annotation.span_start:annotation.span_end+1]

                    #print #tokenizer_class().tokenize(subtext,*args,**kwargs)
                    new_token_spans=tokenizer_class.span_tokenize(subtext,*args,**kwargs)
                    for starts_at,ends_at in new_token_spans:
                        document.annotations.append(Annotation(annotation.span_start+starts_at,annotation.span_start+ends_at-1,output_annotation))

        return {'adc': adc }




def nltk_treebank_word_tokenizer(input_dict):
    raise NotImplementedError() #span_tokenize not implemented in this class

    import nltk
    return {'tokenizer': {'object': nltk.TreebankWordTokenizer()}}


def nltk_punkt_sentence_tokenizer(input_dict):
    import nltk
    return {'tokenizer': {'object': nltk.PunktSentenceTokenizer()}}

