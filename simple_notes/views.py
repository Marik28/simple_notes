from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Note
from .serializers import NoteDetailSerializer, NoteListSerializer


class NoteListView(generics.ListCreateAPIView):
    """View for listing of all notes and creating a new note."""
    serializer_class = NoteListSerializer
    queryset = Note.objects.all()

    def create(self, request: Request, *args, **kwargs):
        """Method used to create a new note instance.
        If provided data is valid, creates new note and returns response with status 201,
        full note info and 'Location' header with note's url address """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note = self.perform_create(serializer)
        resp_serializer = NoteDetailSerializer(note, many=False)
        headers = self.get_success_headers(note)
        return Response(data=resp_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_success_headers(self, note):
        """Adds 'Location' header with note's url address """
        return {'Location': note.get_absolute_url()}


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View, implementing GET, PUT, PATCH and DELETE methods to a note"""
    lookup_field = 'id'
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()
