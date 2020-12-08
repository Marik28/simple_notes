from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotCorrectRequest
from .services import create_note, create_response, update_note, delete_note, get_note_by_id, get_note_list


class NoteListAPIView(APIView):
    """
    APIView for retrieving a list of notes and creating, updating, deleting a note by its id
    """
    def get(self, request: Request):
        """Returns serialized list of all notes in database"""
        notes = get_note_list()
        response = create_response(success=True, status=200, note=notes)
        return response

    def post(self, request: Request):
        """Method used to create a note"""
        try:
            note_id = create_note(request)
        except NotCorrectRequest as exc:
            response = create_response(success=False, status=400, error_message=str(exc))
        else:
            response = create_response(success=True, status=201, note_id=note_id)
        return response

    def put(self, request: Request):
        """Method used to update a note"""
        try:
            update_note(request)
        except NotCorrectRequest as exc:
            response = create_response(status=400, success=False, error_message=str(exc))
        else:
            response = create_response(status=200, success=True)
        return response

    def delete(self, request: Request):
        """Method used to delete a note"""
        try:
            delete_note(request)
        except NotCorrectRequest as exc:
            response = create_response(success=False, status=400, error_message=str(exc))
        else:
            response = create_response(success=True, status=204)
        return response


class NoteDetailAPIView(APIView):
    """Returns serialized data of a single note"""
    def get(self, request: Request, id):
        try:
            note = get_note_by_id(id)
        except NotCorrectRequest as exc:
            response = create_response(success=False, status=400, error_message=str(exc))
        else:
            response = create_response(success=True, status=200, note=note)
        return response
