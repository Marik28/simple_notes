from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.NoteListAPIView.as_view()),
    url(r'^(?P<id>[\w-]+)$', views.NoteDetailAPIView.as_view()),
]