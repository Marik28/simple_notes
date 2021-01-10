from http import HTTPStatus

from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotCorrectRequest
from .models import Note
from .serializers import NoteSerializer
from .services import create_note, put_note, delete_note, get_note_list, patch_note


class NoteListAPIView(APIView):
    """
    APIView for retrieving a list of notes and creating, updating, deleting a note by its id
    """

    def get(self, request: Request):
        """Returns serialized list of all notes in database"""
        notes = get_note_list()
        serializer = NoteSerializer(notes, many=True)
        return Response(data=serializer.data, status=HTTPStatus.OK)

    def post(self, request: Request):
        """Method used to create a note"""
        try:
            note_location = create_note(request)
        except NotCorrectRequest as exc:
            response = Response(str(exc), status=HTTPStatus.BAD_REQUEST)
        else:
            response = Response(status=HTTPStatus.CREATED, headers={"Location": note_location})
        return response


class NoteDetailAPIView(APIView):
    """Returns serialized data of a single note"""

    def get(self, request: Request, id):
        note = get_object_or_404(Note, id=id)
        serializer = NoteSerializer(note, many=False)
        return Response(data=serializer.data, status=HTTPStatus.OK)

    def delete(self, request: Request, id):
        """Method used to delete a note"""
        delete_note(id)
        return Response(status=HTTPStatus.NO_CONTENT)

    def put(self, request: Request, id):
        """Method used to update all fields of a note"""
        try:
            put_note(request, id)
        except NotCorrectRequest as exc:
            response = Response(str(exc), status=HTTPStatus.UNPROCESSABLE_ENTITY)
        else:
            response = Response(status=HTTPStatus.NO_CONTENT)
        return response

    def patch(self, request: Request, id):
        """Method for updating particular field of a note"""
        try:
            new_note_data = patch_note(request, id)
        except NotCorrectRequest as exc:
            response = Response(str(exc), status=HTTPStatus.UNPROCESSABLE_ENTITY)
        else:
            response = Response(data=new_note_data, status=HTTPStatus.OK)
        return response
