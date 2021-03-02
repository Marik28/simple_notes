from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Note
from .serializers import NoteDetailSerializer


class NoteListView(generics.ListCreateAPIView):
    """View for listing of all notes and creating a new note."""
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()

    def create(self, request: Request, *args, **kwargs):
        """Method used to create a new note instance.
        If provided data is valid, creates a new note and returns a response with empty body, status 201
        and 'Location' header with note's url address """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note = self.perform_create(serializer)
        headers = self.get_success_headers(note)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_success_headers(self, note: Note) -> dict:
        """Adds 'Location' header with note's url address """
        return {'Location': note.get_absolute_url()}


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View, implementing GET, PUT, PATCH and DELETE methods to a note"""
    lookup_field = 'id'
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()

    def update(self, request, *args, **kwargs) -> Response:
        """Performs default update method changes response's status code to 204"""
        response: Response = super().update(request, *args, **kwargs)
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
