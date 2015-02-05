from django.shortcuts import render

def lexicology_mesh_filter(request, input_dict, output_dict, widget):
    import json
    from os.path import normpath, join, dirname

    categories=json.load(open(normpath(join(dirname(__file__), 'data/mesh_toplevels.json')))) #{'a':['a1','a2','a3'],'b':['b1','b2']}
    return render(request, 'visualizations/mesh_filter.html',   {'categories': categories, 'widget':widget})

