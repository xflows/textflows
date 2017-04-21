from django.conf.urls import include, url
from mothra.settings import LOGIN_URL
from mothra.settings import DEBUG, STATIC_DOC_ROOT

import django.contrib.auth.views as auth_views
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mothra.views.home', name='home'),
    # url(r'^mothra/', include('mothra.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include('signuplogin.urls')),
    url(r'^', include('website.urls')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^workflows/', include('workflows.urls')),
    url(r'^streams/', include('streams.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('workflows.api_urls')),

    url('^' + LOGIN_URL[1:] + '$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^change-password/$', auth_views.password_change, name='password change'),
    url(r'^password-changed/$', auth_views.password_change_done, name='password change done'),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm),
    url(r'^reset/done/$', auth_views.password_reset_complete),
]

## debug stuff to serve static media
if DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': STATIC_DOC_ROOT}),
   ]