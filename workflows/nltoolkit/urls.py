from django.conf.urls import patterns, url

"""
module cotains url redirections

:param widget_id: unique identifier of a widget globally in textflows. It used to separate views from others.
:param narrow_doc: it used to select a css style template, if the view is displayed as frame or in a new tab.
:param document_id_from: id of first document. It is used, if there is more than 100 documents.
:param document_id_to: id of last document. It is used, if there is more than 100 documents.
:param document_id: id of a document. It is used to output details of a document.
"""

urlpatterns = patterns("workflows.nltoolkit.visualization_views",
    #display a first view of document corpus, when user runs a widget
    url(r'^get-adc-index/widget(?P<widget_id>[0-9]+)/nx/Index.html$', 'document_corpus', name='nltk get adc index'),
    #display document corpus, when user clicks on a link: Open view in new window
    url(r'^get-adc-index/widget(?P<widget_id>[0-9]+)/(?P<narrow_doc>n?)x/Index.html$', 'document_corpus', name='nltk get adc index'),
    #if there is more than 100 documents, we display a catalog view, which groups documents in groups with 100 documents.
    url(r'^get-adc-index/widget(?P<widget_id>[0-9]+)/(?P<narrow_doc>n?)x/Index(?P<document_id_from>[0-9]+)-(?P<document_id_to>[0-9]+).html$', 'document_corpus', name='nltk get adc index'),
    #displays a document_page.html with details for a single document.
    url(r'^get-adc-index/widget(?P<widget_id>[0-9]+)/(?P<narrow_doc>n?)x/Document(?P<document_id>[0-9]+).html', 'document_page', name='nltk get adc page')
)
