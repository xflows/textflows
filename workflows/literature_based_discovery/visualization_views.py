from django.shortcuts import render


def lbd_explore_in_crossbee(request,input_dict,output_dict,widget):
    from urlparse import urlparse
    parsed_uri = urlparse(request.META.get('HTTP_REFERER'))
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    json_widget_url=domain+"api/widgets/" + str(widget.id) + "/.json"
    return render(request, 'visualizations/open_data_in_crossbee.html',{'json_widget_url':json_widget_url,
                                                                        'widget': widget,
                                                                        'crossbee_url':input_dict['crossbee_url']})
