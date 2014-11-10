from django.shortcuts import render
import django.template.loader

def nltk_show_adc(request,input_dict,output_dict,widget):
    view = django.shortcuts.render(request, 'visualizations/nltk_adc.html', {'widget': widget,
                                                                        'input_dict': input_dict,
                                                                        'output_dict': output_dict})
    return view