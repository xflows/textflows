from workflows.textflows_dot_net import objectPprint as opp
from workflows.textflows_dot_net.serialization_utils import *

#------------------------------------------------------------------------------
# VISUALISATIONS
#------------------------------------------------------------------------------
from workflows.latino import library_gen


def show_adc(input_dict):
    if input_dict["adc"] == None:
        raise Exception("Input ADC is required for displaying Anotated Document Corpus!")
    return {}

def show_clusters(input_dict):
    return {}

def show_classifications(input_dict):
    return {}

def advanced_object_viewer(input_dict):
    return {}

def show_table(input_dict):
    return {}

def advanced_object_converter(input_dict):
    obj = input_dict['obj']
    maxStringLen = ToInt(input_dict['maxStringLen'])
    objstr = ""
    if input_dict.has_key('attribute') and input_dict['attribute']!="":
        try:
            obj = eval("obj."+input_dict['attribute'])
        except:
            objstr += "Given attribute '" + input_dict['attribute'] + "' can not be resolved. Showing original object instead:\n"
    objstr += opp.ppprint(obj)
    if (len(objstr)>maxStringLen):
        moreChar = len(objstr) - maxStringLen
        objstr = objstr[0:maxStringLen] + "\n... <Additional " + str(moreChar) + " characters were trimmed due to widget settings.>"
    output_dict = {'objStr': objstr}
    return output_dict

#------------------------------------------------------------------------------
# SUPPLEMENTARY FUNCTIONS
#------------------------------------------------------------------------------
def split_object(input_dict):
    output_dict = {}
    obj = input_dict['object']
    output_dict['object'] = eval("obj"+input_dict['attribute'])
    return output_dict

def python_snippet(input_dict):
    output_dict = {}
    input = input_dict['in']
    for (i, val) in enumerate(input):
        vars()["in"+str(i+1)] = val
    out1 = None
    exec(input_dict['pycode'])
    output_dict['out'] = out1
    return output_dict


def latino_tokenize_words(inputDict):
    _tokenizer = inputDict['tokenizer']

    if type(_tokenizer)!=dict:
        return library_gen.latino_tokenize_words(inputDict)
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


        #            ITokenizerEnumerator tokenEnum = tokenizer.GetEnumerator();
        #            tokenEnum.Reset();
        #            while (tokenEnum.MoveNext()) //Till not finished do print
        #            {
        #                Pair<int, int> pos = tokenEnum.CurrentPos;
        #                if (pos.Second > pos.First)
        #                    document.AddAnnotation(new Annotation(textBlock.SpanStart + pos.First, textBlock.SpanStart + (pos.Second - 1), outputAnnotation));
        #            }
        #        }
        #    }
        #}

        _inputAnnotation = ToString(inputDict['inputAnnotation'])
        _outputAnnotation = ToString(inputDict['outputAnnotation'])

        return {'adc': adc }

        # DocumentCorpus adcNew = adc.Clone();
        #
        # foreach (Document document in adcNew.Documents) {
        #     string contentType = document.Features.GetFeatureValue("contentType");
        #     if (contentType == "Text") {
        #         if (string.IsNullOrEmpty(document.Text)) continue;
        #         TextBlock[] textBlocks = document.GetAnnotatedBlocks(inputAnnotation);
        #         foreach (TextBlock textBlock in textBlocks) {
        #             tokenizer.Text = textBlock.Text;
        #             ITokenizerEnumerator tokenEnum = tokenizer.GetEnumerator();
        #             tokenEnum.Reset();
        #             while (tokenEnum.MoveNext()) //Till not finished do print
        #             {
        #                 Pair<int, int> pos = tokenEnum.CurrentPos;
        #                 if (pos.Second > pos.First)
        #                     document.AddAnnotation(new Annotation(textBlock.SpanStart + pos.First, textBlock.SpanStart + (pos.Second - 1), outputAnnotation));
        #             }
        #         }
        #     }
        # }
        # return adcNew;
