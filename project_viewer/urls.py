from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from project_viewer import views

urlpatterns = patterns('',
		#ex: /polls/
		url(r'^$', views.IndexView.as_view(), name='index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
