from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simulator.views.home', name='home'),
    # url(r'^simulator/', include('simulator.foo.urls')),

    url(r'^ekg/(?P<ekg_id>\d+)/(?P<outputtype>[-A-Za-z0-9_]+)/$',
        'ekg.views.ekg', name='ekg'),

    url(r'^select/(?P<outputtype>[-A-Za-z0-9_]+)/$',
        'ekg.views.selected', name='selected-ekg'),

    url(r'^instant/(?P<ekg_id>\d+)/(?P<outputtype>[-A-Za-z0-9_]+)/$',
        'ekg.views.instant', name='instant'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
