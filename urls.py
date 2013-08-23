from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', 'tapwn.news.views.login_page', name='login'),
    url(r'^logout/$', 'tapwn.news.views.logout_view', name='logout'),
    url(r'^about/$', 'tapwn.news.views.about', name='about'),
    url(r'^maintenance/$', 'tapwn.news.views.maintenance', name='maintenance'),
    url(r'^$', 'tapwn.news.views.home', name='home'),
    # url(r'^tapwn/', include('tapwn.foo.urls')),
    url(r'^headlines/$', 'tapwn.news.views.headline_index', name='headlines'),
    url(r'^headlines/(?P<headline_id>\d+)/$', 'tapwn.news.views.headline_detail', name='headline_detail'),
    url(r'^headlines/create/$', 'tapwn.news.views.headline_create', name='headline_create'),
    url(r'^headlines/update/(?P<headline_id>\d+)/$', 'tapwn.news.views.headline_update', name='headline_update'),
    url(r'^headlines/delete/(?P<headline_id>\d+)/$', 'tapwn.news.views.headline_delete', name='headline_delete'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()