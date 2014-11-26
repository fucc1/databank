from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'databank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^etldata/', include('etldata.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# ... your normal urlpatterns here

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
