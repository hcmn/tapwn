from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', 'project_name.app_name.views.login_page', name='login'),
    url(r'^logout/$', 'project_name.app_name.views.logout_view', name='logout'),
    url(r'^about/$', 'project_name.app_name.views.about', name='about'),
    url(r'^maintenance/$', 'project_name.app_name.views.maintenance', name='maintenance'),
    url(r'^$', 'project_name.app_name.views.home', name='home'),
    # url(r'^tapwn/', include('tapwn.foo.urls')),
    url(r'^headlines/$', 'project_name.app_name.views.headline_index', name='headlines'),
    url(r'^headlines/(?P<headline_id>\d+)/$', 'project_name.app_name.views.headline_detail', name='headline_detail'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
