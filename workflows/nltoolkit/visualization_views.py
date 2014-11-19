
from django.shortcuts import render
import django.template.loader
from django.shortcuts import get_object_or_404

from workflows.models import Widget


def display_document_corpus(request, input_dict, output_dict, widget):
    view = django.shortcuts.render(request, 'visualizations/document_corpus_index_page.html', {'widget': widget,
                                                                        'input_dict': input_dict})
    return view


def document_corpus(request, widget_id):
    w = get_object_or_404(Widget, pk=widget_id)
    documents = w.inputs.all()[0].value.documents
    features = w.inputs.all()[0].value.features
    for document in documents:
        document.features["basic_types"] = len(set([annotation.type for annotation in document.annotations]))

    view = django.shortcuts.render(request, 'visualizations/document_corpus.html', {'widget_id': widget_id,
                                                                                    'documents': documents,
                                                                                    "features": features})
    return view


def document_page(request, widget_id, document_id, narrow_doc = 'n'):
    w = get_object_or_404(Widget, pk=widget_id)
    document = w.inputs.all()[0].value.documents[int(document_id)-1]
    back_url = request.environ["HTTP_REFERER"]
    annotations = {}
    for annotation in document.annotations:
        annotations[annotation.type] = annotations.get(annotation.type, "")+str(annotation.span_start)+","+str(annotation.span_end)+",:"

    view = django.shortcuts.render(request, 'visualizations/document_page.html', {'widget_id': widget_id,
                                                                                    'document': document,
                                                                                    'annotations': annotations,
                                                                                    'back_url': back_url})
    return view


