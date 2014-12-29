from django.shortcuts import render

def scikit_classifiers_filter_integers(request,input_dict,output_dict,widget):
    return render(request, 'interactions/scikit_classifiers_filter_integers.html',{'widget':widget,'intList':input_dict['intList']})