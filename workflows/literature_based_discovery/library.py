import numpy as np
from workflows.literature_based_discovery.lib.heuristics.heuristic_calculations import HeuristicCalculations
from workflows.textflows import flatten, BowDataset


def lbd_select_ensemble_heuristic(input_dict):
    return {}

def lbd_select_ensemble_heuristic_post(postdata, input_dict, output_dict):
    widget_id = postdata.get('widget_id')[0]

    from workflows.textflows_dot_net.serialization_utils import ToNetObj
    import LatinoInterfaces
    output_dict={}
    output_dict['serialized_adc']=LatinoInterfaces.LatinoCF.Save(ToNetObj(input_dict['adc']))
    output_dict['vocabulary']=input_dict['bow_model_constructor'].get_feature_names()
    output_dict['heuristic_scores']=[{'name': hevr.name, 'scores': hevr.scores.tolist()} for hevr in flatten(input_dict['heuristic_scores'])]
    output_dict['bterms']=input_dict['bterms']
    output_dict['serialized_dataset']=LatinoInterfaces.LatinoCF.Save(ToNetObj(input_dict['dataset']))
    #output_dict['primary_heuristic_index']=input_dict['primary_heuristic_index']

    output_dict['primary_heuristic_index']=int(postdata.get('heuristic_index',[-1])[0])

    return output_dict #{'heuristic_index': selected_heuristic}

def lbd_only_terms_from_both_domains(input_dict):
    adc=input_dict['adc']
    bmc=input_dict['bow_model_constructor']

    raw_documents=bmc.get_raw_text(adc.documents,join_annotations_with='|##|')
    classes=bmc.get_document_labels(adc,binary=True)

    hc=HeuristicCalculations(raw_documents,classes,bmc) #only creates counts for each domain
    terms_in_both_domains_idx= np.where((hc._count_term_A() > 0) & (hc._count_term_C() > 0)==True)[0]
    orig_vocabulary=bmc.get_feature_names()
    terms_in_both_domains=[orig_vocabulary[i] for i in terms_in_both_domains_idx]

    # if predefined_vocabulary:
    #     vocab_vectorizer=CountVectorizer(ngram_range=(1,max_ngram))
    #     vocab_vectorizer.fit(predefined_vocabulary)
    #     self.set_new_vocabulary(vocab_vectorizer.vocabulary_,raw_documents)
    bmc.set_new_vocabulary(terms_in_both_domains,raw_documents)

    bow_dataset=BowDataset.from_adc(adc,bmc)

    return {'bow_model_constructor': bmc,'bow_dataset': bow_dataset}


def lbd_frequency_based_heuristics_selection(input_dict):
    return {'heuristics': [u'freq_doc', u'freq_ratio', u'freq_term']}
def lbd_tfidf_based_heuristics_selection(input_dict):
    return {'heuristics': [u'tfidf_avg', u'tfidf_sum']}
def lbd_similarity_based_heuristics_selection(input_dict):
    return {}
def lbd_outlier_based_heuristics_selection(input_dict):
    return {}

def lbd_heuristic_selection_post(postdata, input_dict, output_dict):
    widget_id = postdata.get('widget_id')[0]
    selected_heuristics=postdata.get('selected[]',[])

    return {'heuristics': selected_heuristics}


def lbd_heuristic_min(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'heuristic': ('Min',heuristic_names)}

def lbd_heuristic_max(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'heuristic': ('Max',heuristic_names)}

def lbd_heuristic_sum(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'heuristic': ('Sum',heuristic_names)}

def lbd_heuristic_norm(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'norm_heuristics': [('Norm',heuristic_name) for heuristic_name in heuristic_names]}

def lbd_ensemble_heuristic_vote(input_dict):
    heuristic_names=flatten(input_dict['heuristics'])
    return {'heuristic': ('Vote',heuristic_names)}

def lbd_ensemble_average_position(input_dict):
    heuristic_names=flatten(input_dict['heuristics'])
    return {'heuristic': ('AvgPos',heuristic_names)}

def lbd_calculate_heuristics(input_dict):
    heuristic_names=input_dict.get('heuristics',[])
    adc=input_dict['adc']
    bow_model=input_dict['bow_model_constructor']

    raw_documents=bow_model.get_raw_text(adc.documents,join_annotations_with='|##|')
    classes=bow_model.get_document_labels(adc,binary=True)
    #stress_idx=bow_model.get_feature_names().index("stress")
    hc=HeuristicCalculations(raw_documents,classes,bow_model)#,stress_idx=stress_idx)
    calcs=hc.calculate_heuristics(heuristic_names)
    return {'calcs': calcs}

def lbd_actual_and_predicted_values(input_dict):
    bterms=input_dict['bterms']
    bow_model_constructor=input_dict['bow_model_constructor']
    vocabulary=bow_model_constructor._vocab_to_idx()

    actual_values=[0]*len(vocabulary)
    for bterm in bterms:
        if bterm in vocabulary:
            actual_values[vocabulary[bterm]]=1
            #print bterm

    heuristics=flatten(input_dict['heuristics'])

    return {'apv':[{'name': h.name,'predicted':list(h.scores),'actual':actual_values} for h in heuristics]}

def lbd_explore_in_crossbee(input_dict):
    return {} #output_dict
    #return render(request, 'visualizations/open_data_in_crossbee.html',{'widget':widget}) #,'input_dict':input_dict,'output_dict':output_dict})