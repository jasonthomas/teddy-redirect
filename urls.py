from django.conf.urls.defaults import patterns, include, url
from teddy.views import get_short
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^(.*)$', get_short),
    # Examples:
    # url(r'^$', 'teddy.views.home', name='home'),
    # url(r'^teddy/', include('teddy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
