from django.shortcuts import render


def read_string_in_slovene(request,input_dict,output_dict,widget):
    text=input_dict.get('text')
    return render(request, 'visualizations/read_string_in_slovene.html',{'widget':widget,'text':text})


