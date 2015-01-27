from workflows.literature_based_discovery.lib.heuristics.heuristic_calculations import HeuristicCalculations
import numpy as np


def lbd_heuristics_selection(input_dict):
    return {}

def lbd_heuristic_selection_post(postdata, input_dict, output_dict):
    widget_id = postdata.get('widget_id')[0]
    selected_heuristics=postdata.get('selected[]',[])

    return {'heuristics': selected_heuristics}


def lbd_heuristic_sum(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'heuristic': ('Sum',heuristic_names)}

def lbd_heuristic_vote(input_dict):
    heuristic_names=flatten(input_dict['heuristics'])
    return {'heuristic': ('Vote',heuristic_names)}

def lbd_calculate_heuristics(input_dict):
    heuristic_names=input_dict.get('heuristics',[])
    adc=input_dict['adc']
    bow_model=input_dict['bow_model']

    raw_documents=bow_model.get_raw_text(adc.documents)
    classes=bow_model.get_labels(adc,binary=True)

    hc=HeuristicCalculations(raw_documents,classes,bow_model)
    calcs=hc.calculate_heuristics(heuristic_names)
    return {'calcs': calcs}


from collections import Iterable
def flat(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, basestring):
             for x in flat(item):
                 yield x
         else:
             yield item

def flatten(lis):
    return list(flat(lis))