from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.NoteListView.as_view(), name="notes"),
    url(r'^(?P<id>[\w-]+)$', views.NoteDetailView.as_view(), name="note_detail"),
]
