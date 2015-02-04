from django.shortcuts import render


def lbd_explore_in_crossbee(request,input_dict,output_dict,widget):
    return render(request, 'visualizations/open_data_in_crossbee.html',{'widget':widget})
