from django.conf.urls import  url

import signuplogin

urlpatterns = [
    url(r'^signuplogin/$', signuplogin, name='signuplogin'),
]