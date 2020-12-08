from rest_framework.request import Request
from rest_framework.response import Response

from .exceptions import NotCorrectRequest
from .models import Note
from .serializers import NoteCreateSerializer, NoteUpdateSerializer, NoteSerializer


def create_response(*, success: bool, status: int, **kwargs) -> Response:
    data = {
        "success": success,
    }
    if kwargs:
        for key, value in kwargs.items():
            data[key] = value
    return Response(data, status=status)


def create_note(request: Request):
    note = NoteCreateSerializer(data=request.data)
    if note.is_valid():
        saved_note = note.save()
        return saved_note.id
    else:
        raise NotCorrectRequest("Not correct request. Note can not be created")


def update_note(request: Request):
    id = request.data.get('id', None)
    if id:
        try:
            note = Note.objects.get(id=id)
        except Note.DoesNotExist:
            raise NotCorrectRequest(f"Not correct request. Note with id={id} doesn't exist")
        else:
            serializer = NoteUpdateSerializer(instance=note, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                raise NotCorrectRequest("Not correct request. Provided data is not valid")
    else:
        raise NotCorrectRequest("Not correct request. id was not provided")


def delete_note(request: Request):
    id = request.data.get('id')
    if id:
        try:
            note = Note.objects.get(id=id)
        except Note.DoesNotExist:
            raise NotCorrectRequest("Not correct request. An invalid note id was provided")
        else:
            note.delete()
    else:
        raise NotCorrectRequest("Not correct request. Note id was not provided")


def get_note_by_id(id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        raise NotCorrectRequest(f"Note with id={id} doesn't exist")
    else:
        serializer = NoteSerializer(note)
        return serializer.data


def get_note_list():
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return serializer.data
