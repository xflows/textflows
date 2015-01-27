from django.shortcuts import render


def open_data_in_crossbee(request,input_dict,output_dict,widget):
    #from mothra.settings import MEDIA_ROOT
    #from workflows.helpers import ensure_dir
    #destination = MEDIA_ROOT+'/'+str(request.user.id)+'/'+str(widget.id)+'.txt'
    #ensure_dir(destination)
    #f = open(destination,'w')
    #f.write(str(input_dict['string']))
    #f.close()
    #filename = str(request.user.id)+'/'+str(widget.id)+'.txt'
    #output_dict['filename'] = filename
    return render(request, 'visualizations/open_data_in_crossbee.html',{'widget':widget}) #,'input_dict':input_dict,'output_dict':output_dict})
