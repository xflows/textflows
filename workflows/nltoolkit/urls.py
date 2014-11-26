from django.conf.urls import patterns, url

urlpatterns = patterns("workflows.nltoolkit.visualization_views",
    url(r'^get-adc-index/widget(?P<widget_id>[0-9]+)/nx/Index.html$', 'document_corpus', name='nltk get adc index'),
    url(r'^get-adc-index/widget(?P<widget_id>[0-9]+)/(?P<narrow_doc>n?)x/Index.html$', 'document_corpus', name='nltk get adc index'),
    url(r'^get-adc-index/widget(?P<widget_id>[0-9]+)/(?P<narrow_doc>n?)x/Document(?P<document_id>[0-9]+).html', 'document_page', name='nltk get adc page')
)
