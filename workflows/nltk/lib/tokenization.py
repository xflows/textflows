from workflows.textflows import *

def tokenizer_hub(inputDict):
    from ...latino.library_gen import latino_tokenize_words
    _tokenizer = inputDict['tokenizer']

    if type(_tokenizer)!=dict:
        return latino_tokenize_words(inputDict)
    else:
        tokenizer_class=_tokenizer['type']
        args=_tokenizer.get('args',[])
        kwargs=_tokenizer.get('kargs',{})
        input_annotation = inputDict['inputAnnotation']
        output_annotation = inputDict['outputAnnotation']
        adc = inputDict['adc']
        for document in adc.documents:
            if document.features['contentType'] == "Text":
                if not document.text:
                    pass
                for annotation in document.select_annotations(input_annotation): #all annotations of this type
                    subtext = document.text[annotation.span_start:annotation.span_end+1]

                    #print #tokenizer_class().tokenize(subtext,*args,**kwargs)
                    new_token_spans=tokenizer_class().span_tokenize(subtext,*args,**kwargs)
                    for starts_at,ends_at in new_token_spans:
                        document.annotations.append(Annotation(annotation.span_start+starts_at,annotation.span_start+ends_at-1,output_annotation))

        return {'adc': adc }




def nltk_treebank_word_tokenizer(input_dict):
    raise NotImplementedError() #span_tokenize not implemented in this class

    import nltk
    return {'tokenizer': {'type': nltk.TreebankWordTokenizer}}


def nltk_punkt_sentence_tokenizer(input_dict):
    import nltk
    return {'tokenizer': {'type': nltk.PunktSentenceTokenizer}}

