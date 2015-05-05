from django.shortcuts import render
from lib.heuristics.frequency_heuristics import FrequencyBasedHeuristicCalculations
from lib.heuristics.tfidf_heuristics import TfIdfBasedHeuristicCalculations
from lib.heuristics.outlier_heuristics import OutlierBasedHeuristicCalculations
from lib.heuristics.similarity_heuristics import SimilarityBasedHeuristicCalculations
from workflows.textflows import flatten


def lbd_frequency_heuristics(request, input_dict, output_dict, widget):
    heuristics=extract_heuristic_names_and_descriptions(FrequencyBasedHeuristicCalculations)
    return render(request, 'interactions/lbd_select_heuristics.html',  {'heuristics': heuristics, 'widget':widget})

def lbd_tfidf_heuristics(request, input_dict, output_dict, widget):
    heuristics=extract_heuristic_names_and_descriptions(TfIdfBasedHeuristicCalculations)
    return render(request, 'interactions/lbd_select_heuristics.html',  {'heuristics': heuristics, 'widget':widget})

def lbd_similarity_heuristics(request, input_dict, output_dict, widget):
    heuristics=extract_heuristic_names_and_descriptions(SimilarityBasedHeuristicCalculations)
    return render(request, 'interactions/lbd_select_heuristics.html',  {'heuristics': heuristics, 'widget':widget})

def lbd_outlier_heuristics(request, input_dict, output_dict, widget):
    heuristics=extract_heuristic_names_and_descriptions(OutlierBasedHeuristicCalculations)
    return render(request, 'interactions/lbd_select_heuristics.html',  {'heuristics': heuristics, 'widget':widget})

def lbd_select_ensemble_heuristic(request, input_dict, output_dict, widget):
    heuristics=[h.name for h in flatten(input_dict['heuristic_scores'])]
    return render(request, 'interactions/lbd_select_ensemble_heuristic.html',  {'heuristics': heuristics, 'widget':widget})


#HELPERS
def extract_heuristic_names_and_descriptions(cls):
    heuristics=[]
    for a in dir(cls):
        if not a.startswith('_') and not a.startswith("calculate"):
            heuristics.append((a,getattr(cls,a).__doc__))
    return heuristics



