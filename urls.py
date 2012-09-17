from django.conf.urls.defaults import patterns, include, url
import teddy.redirect.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^new$', teddy.redirect.views.new_short),
    url(r'^recent$', teddy.redirect.views.recent),
    url(r'^(.*)$', teddy.redirect.views.get_short),
    # Examples:
    # url(r'^$', 'teddy.views.home', name='home'),
    # url(r'^teddy/', include('teddy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
