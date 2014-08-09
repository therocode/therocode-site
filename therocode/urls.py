from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

if(settings.DEBUG):
	urlpatterns = patterns('',
    url(r'^projects/', include('project_viewer.urls', namespace="pv")),
    url(r'^admin/', include(admin.site.urls)),
	) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
	urlpatterns = patterns('',
    url(r'^projects/', include('project_viewer.urls', namespace="pv")),
    url(r'^admin/', include(admin.site.urls)),
	)
