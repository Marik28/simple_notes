from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note
from .serializers import NoteListSerializer, NoteDetailSerializer, NoteCreateSerializer


class NoteListAPIView(APIView):
    """Returns serialized list of all notes in database"""
    def get(self, request: HttpRequest):
        notes = Note.objects.all()
        serializer = NoteListSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest):
        print(request.data)
        note = NoteCreateSerializer(data=request.data)
        if note.is_valid():
            note.save()
            return Response(status=201)
        else:
            return Response(status=400)


class NoteDetailAPIView(APIView):
    """Returns serialized data of a single note"""
    def get(self, request: HttpRequest, id):
        note = Note.objects.get(id=id)
        serializer = NoteDetailSerializer(note)
        return Response(serializer.data)


