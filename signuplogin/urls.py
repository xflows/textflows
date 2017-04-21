from django.conf.urls import  url
import signuplogin.views as signuplogin_views

import signuplogin.views as signuplogin_views

urlpatterns = [
    url(r'^signuplogin/$', signuplogin_views.signuplogin, name='signuplogin'),
]