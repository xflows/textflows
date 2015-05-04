import requests
import json
from workflows.textflows import Annotation


class TripletClient(object):
    def __init__(self,url="http://concreteflows.ijs.si:8080/tripletserver/"):
        self.base_url = url

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    def reverb(self,text):
        r = requests.post(self.base_url+"api/reverb/extract",data=json.dumps({"text":text}))
        return r.json()

    def ollie(self,text):
        r = requests.post(self.base_url+"api/ollie/extract",data=json.dumps({"text":text}))
        return r.json()


def triplet_extraction_hub(input_dict):
    input_annotation = input_dict['input_annotation']
    output_annotation = input_dict['output_annotation']

    adc = input_dict['adc']
    t = TripletClient()


    all_triplets=[]

    for document in adc.documents:
        if document.features['contentType'] == "Text":
            if not document.text:
                pass
            for annotation,subtext in document.get_annotations_with_text(input_annotation): #all annotations of this type
                if subtext:
                    if False:
                        extractions = t.reverb(subtext)['extractions']

                        if extractions:
                            most_confident=max(extractions,key=lambda a: a['conf'])
                            print "aaa",subtext
                            subject=most_confident['arg1']
                            print subject
                            start=annotation.span_start+subtext.find(subject)
                            end=start+len(subject)-1
                            print subtext[start:end]
                            document.annotations.append(Annotation(start,end,
                                                                   output_annotation+"_subject"))
                            verb=most_confident['rel']
                            start=end+subtext[end:].find(verb)
                            end=start+len(verb)-1
                            print subtext[start:end]
                            document.annotations.append(Annotation(start,end,
                                                                   output_annotation+"_verb"))
                            predicate=most_confident['arg2']
                            start=end+subtext[end:].find(predicate)
                            end=start+len(predicate)-1
                            print subtext[start:end]
                            document.annotations.append(Annotation(start,end,
                                       output_annotation+"_predicate"))
                    else: #ollie extractor
                        extractions = t.ollie(subtext)['extractions']

                        if False:
                            most_confident=max(extractions,key=lambda a: a['confidence'])

                            subject=most_confident['arg1']
                            if subtext.find(subject)==-1:
                                aaa=3

                            start=annotation.span_start+subtext.find(subject)
                            end=start+len(subject)-1
                            print subtext[start:end]
                            document.annotations.append(Annotation(start,end,
                                                                   output_annotation+"_subject"))
                            verb=most_confident['rel'].replace("be ","").replace("Be ","")

                            if subtext[end:].find(verb)==-1:
                                aaa=3
                            start=end+subtext[end:].find(verb)
                            end=start+len(verb)-1
                            print subtext[start:end]
                            document.annotations.append(Annotation(start,end,
                                                                   output_annotation+"_verb"))
                            predicate=most_confident['arg2']
                            if subtext[end:].find(predicate)==-1:
                                aaa=3

                            start=end+subtext[end:].find(predicate)
                            end=start+len(predicate)-1
                            print subtext[start:end]
                            document.annotations.append(Annotation(start,end,
                                       output_annotation+"_predicate"))
                        else:
                            triplets=[(e['arg1'],e['rel'],e['arg2']) for e in extractions]
                            annotation.features[output_annotation]=triplets
                            all_triplets.extend(triplets)

    return {'adc': adc,'triplets': all_triplets }

    # text_grouped=[] #text_groups= [['First','sentence',['Second','sentance']]
    # annotations_grouped=[] #annotations_grouped= [[<Annotation span_start:0 span_ned:4>, <Annotation span_start:6 span_ned:11>],[...
    #
    # i=0
    # for group_annotation,_ in group_annotations:
    #     elements=[]
    #     sentence_annotations=[]
    #     #find elementary annotations 'contained' in the group_annotation
    #     while i<len(element_annotations) and element_annotations[i][0].span_end<=group_annotation.span_end:
    #         annotation=element_annotations[i][0]
    #         text_block=element_annotations[i][1]
    #         elements.append(text_block)
    #         sentence_annotations.append(annotation)
    #         i+=1
    #     text_grouped.append(elements)
    #     annotations_grouped.append(sentence_annotations)
    #
    # new_features=getattr(tagger,tagger_function)(text_grouped,*args,**kwargs)
    # for sentence_features, sentence_annotations in izip(new_features,annotations_grouped):
    #     for feature,annotation in izip(sentence_features,sentence_annotations):
    #         annotation.features[output_annotation_name]=feature[1] #[0:number_of_letters]