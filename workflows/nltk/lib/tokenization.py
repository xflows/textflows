from workflows.textflows import *

def tokenizer_hub(input_dict):
    """
    Apply the *tokenizer* object on the Annotated Document Corpus (*adc*):

    1. first select only annotations of type *input_annotation*,
    2. apply the tokenizer
    3. create new annotations *output_annotation* with the outputs of the tokenizer.

    :param adc: Annotated Document Corpus (workflows.textflows.DocumentCorpus)
    :param tokenizer: A python dictionary containing the Tokenizer object and its arguments.
    :param input_annotation: Which annotated part of document to be splited
    :param output_annotation: How to annotate the newly discovered tokens
    """

    tokenizer_dict = input_dict['tokenizer']

    if type(tokenizer_dict)!=dict:
        from ...latino.library_gen import latino_tokenize_words
        return latino_tokenize_words(input_dict)
    else:
        tokenizer=tokenizer_dict['object']
        args=tokenizer_dict.get('args',[])
        kwargs=tokenizer_dict.get('kargs',{})
        input_annotation = input_dict['input_annotation']
        output_annotation = input_dict['output_annotation']
        adc = input_dict['adc']
        for document in adc.documents:
            if document.features['contentType'] == "Text":
                if not document.text:
                    pass
                for annotation,subtext in document.get_annotations_with_text(input_annotation): #all annotations of this type
                    new_token_spans=tokenizer.span_tokenize(subtext,*args,**kwargs)
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

