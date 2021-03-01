from django.conf.urls import url
from django.conf import settings
from . import views
from .yasg import url_patterns as doc_urls

urlpatterns = [
    url(r'^$', views.NoteListView.as_view(), name="notes"),
    url(r'^(?P<id>[\w-]+)$', views.NoteDetailView.as_view(), name="note_detail"),
]

if settings.DEBUG:
    urlpatterns += doc_urls
