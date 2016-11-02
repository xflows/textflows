import django.template.loader
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from workflows.models import Widget
import nltk
from nltk.collocations import *

@login_required
def display_document_corpus(request, input_dict, output_dict, widget, narrow_doc='n'):
    """
    Display Document Corpus widget displays ADC (Annotated Document Corpus) structure.
    It shows a detail view for selected document with annotations.

    user runs a display corpus widget. We return index template, which calls a document_corpus function.
    """
    view = django.shortcuts.render(request, 'visualizations/document_corpus_index_page.html', {'widget': widget,
                                                                                               'input_dict': input_dict,
                                                                                               'narrow_doc': narrow_doc})
    return view

@login_required
def document_corpus(request, widget_id, document_id_from=0, document_id_to=-1,  narrow_doc='n'):
    """
    Function display a list of documents, if there is less than 100 documents.
    If there is more than 100 document, it groups documents in groups of 100 documents.
    """
    w = get_object_or_404(Widget, pk=widget_id)
    features = w.inputs.all()[0].value.features  # features like source_name, corpus_create_date etc.

    if document_id_to == -1:  # if there is default value for document_id_to
        documents = w.inputs.all()[0].value.documents  # get all documents
        back_url = ""
    else:
        #get interval of documents. document_id_from has -1, because we start counting documents from 1 and not 0.
        #document_id_to does not have -1, because we output documents to document x, with document x included.
        documents = w.inputs.all()[0].value.documents[int(document_id_from):int(document_id_to)]
        back_url = request.environ["HTTP_REFERER"]

    if len(documents) <= 100:
        #display 100 documents or less

        for i, document in enumerate(documents):
            document.additions = {"id": i+int(document_id_from)} #add document ids to the document object
            #count annotations for a document
            document.additions["basic_types"] = len(set([annotation.type for annotation in document.annotations]))


        view = django.shortcuts.render(request, 'visualizations/document_corpus.html', {'widget_id': widget_id,
                                                                                        'documents': documents,
                                                                                        "features": features,
                                                                                        'back_url': back_url,
                                                                                        'narrow_doc': narrow_doc})
    else:
        #group documents in groups of 100 documents
        document_catalog = []
        for i in range(len(documents)):
            if i % 100 == 0:
                interval = i+100 if i+100 < len(documents) else len(documents)
                last_index = interval-1 if i+100 < len(documents) else interval-1

                sum_features = sum([len(documents[j].features) for j in range(i, interval)])
                sum_annotations = sum([len(documents[j].annotations) for j in range(i, interval)])

                document_catalog.append({"first": (documents[i], i+1),  # first document in a group with id
                                         "last": (documents[last_index], interval),  # last document in a group with id
                                         "sum_annotations": sum_annotations,  # sum of annotations  for this group
                                         "sum_features": sum_features,  # sum of features  for this group
                                         "length": 100 if i+100 < len(documents) else len(documents)-i})

        view = django.shortcuts.render(request, 'visualizations/document_corpus_catalog.html', {'widget_id': widget_id,
                                                                                                'document_catalog': document_catalog,
                                                                                                "features": features,
                                                                                                'back_url': back_url,
                                                                                                'narrow_doc': narrow_doc})

    return view

@login_required
def document_page(request, widget_id, document_id, narrow_doc='n'):
    """
    Function displays details for a single document.
    """
    import random_colors
    w = get_object_or_404(Widget, pk=widget_id)
    document = w.inputs.all()[0].value.documents[int(document_id)]
    back_url = request.environ["HTTP_REFERER"]

    #create a new data structure for annotations that is more appropriate for django template language
    annotations = {}
    for annotation in document.annotations:

        annotations[annotation.type] = annotations.get(annotation.type, "") + \
                                       str(annotation.span_start) + "," + \
                                       str(annotation.span_end) + "," + \
            str(annotation.features)[1:-1].replace(",", "<br/>").replace(":", " =").replace("u'", "").replace("'", "").replace("u\"", "").replace("\"", "") \
            + ":"  # annotations for tipsy. We format string, so that tipsy shows it correctly

    #create a color for each annotation
    annotation_colors = random_colors.get_colors(len(annotations))
    for i, (k, v) in enumerate(annotations.iteritems()):
        annotations[k] = [v, annotation_colors[i]]

    view = django.shortcuts.render(request, 'visualizations/document_page.html', {'widget_id': widget_id,
                                                                                  'document': document,
                                                                                  'annotations': annotations,
                                                                                  'back_url': back_url,
                                                                                  'narrow_doc': narrow_doc})
    return view


@login_required
def display_annotation_statistic(request, input_dict, output_dict, widget, narrow_doc='n'):
    """
    Display POS statistics, basicaly frequencies of specific tags
    """

    adc = input_dict['adc']
    annotation_name = input_dict['annotation_name']
    stat_type = input_dict['stat_type']
    allAnnotations = 0
    result_list = []
    print(stat_type)
    if stat_type[0].isdigit():
        n = int(stat_type[0])
        annotation_dict = {}
        for doc in adc.documents:
            annotations = doc.get_annotations_with_text(annotation_name)
            length = len(annotations)
            for i in range(0, length - n + 1):
                combo = ""
                for j in range(i, i + n):
                    _, value = annotations[j]
                    if j > i:
                        combo += "_"
                    combo += value
                            
                if len(combo) > 0:
                    allAnnotations += 1
                    if combo in annotation_dict:
                        annotation_dict[combo] = annotation_dict[combo] + 1
                    else:
                        annotation_dict[combo] = 1
            title = "Annotation frequency"
        
        allAnnotations = float(allAnnotations)
        for pos, number in annotation_dict.items():
            result_list.append((pos, "{0:.2f}".format(float(number)/allAnnotations)))

        result_list = sorted(result_list, key=lambda x: x[1], reverse=True)[:40]

    else:
        all_annotations = []
        for doc in adc.documents:
            annotations = doc.get_annotations_with_text(annotation_name)
            for annotation in annotations:
                _, value = annotation
                all_annotations.append(value)

        if stat_type == 'pmi_bigrams':
            bigram_measures = nltk.collocations.BigramAssocMeasures()
            finder = BigramCollocationFinder.from_words(all_annotations)
            best = finder.score_ngrams(bigram_measures.pmi)[:40]
            for tags, score in best:
                tag1, tag2 = tags
                result_list.append((tag1 + " " + tag2, "{0:.2f}".format(score)))
            title = "Bigrams PMI"


        elif stat_type == 'pmi_trigrams':
            trigram_measures = nltk.collocations.TrigramAssocMeasures()
            finder = TrigramCollocationFinder.from_words(all_annotations)
            best = finder.score_ngrams(trigram_measures.pmi)[:40]
            for tags, score in best:
                tag1, tag2, tag3 = tags
                result_list.append((tag1 + " " + tag2 + " " + tag3, "{0:.2f}".format(score)))
            title = "Trigrams PMI"
        
    view = django.shortcuts.render(request, 'visualizations/pos_statistics.html', {'widget': widget,
                                                                                               'data': [result_list, title],
                                                                                               'narrow_doc': narrow_doc})
    return view


