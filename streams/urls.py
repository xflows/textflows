from django.conf.urls import url

from streams.views import stream_widget_visualization

urlpatterns = [
    url(r'^data/(?P<stream_id>[0-9]+)/(?P<widget_id>[0-9]+)/$', stream_widget_visualization, name='stream widget visualization'),
]
