from rest_framework.generics import get_object_or_404
from rest_framework.request import Request

from .exceptions import NotCorrectRequest
from .models import Note
from .serializers import NoteCreateSerializer, NoteUpdateSerializer, NoteSerializer


def create_note(request: Request):
    """Creates a note from request data and returns its location"""
    note = NoteCreateSerializer(data=request.data)
    if note.is_valid():
        saved_note = note.save()
        return saved_note.get_absolute_url()
    else:
        # надо придумать получше обработку, т.к. могут быть разные случаи некорректных данных
        raise NotCorrectRequest("The invalid fields were provided")


def put_note(request: Request, id) -> None:
    """Updates all fields of a note."""
    note = get_object_or_404(Note, id=id)
    serializer = NoteUpdateSerializer(instance=note, data=request.data, partial=False)
    if serializer.is_valid():
        serializer.save()
    else:
        raise NotCorrectRequest("Not correct request. Provided data is not valid")


def delete_note(id) -> None:
    """Deletes a note"""
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        # чел написал, что delete не должен возвращать 404, если объекта нет. Не очень понял
        pass
        # raise NotCorrectRequest("Not correct request. An invalid note id was provided")
    else:
        note.delete()


def get_note_list() -> list:
    """Gets all notes from DB"""
    notes = Note.objects.all()
    return notes


def patch_note(request: Request, id):
    """Updates given fields of a note and returns its new data"""
    note = get_object_or_404(Note, id=id)
    serializer = NoteUpdateSerializer(instance=note, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        # опять же, надо получше это продумать
        raise NotCorrectRequest("Provided field/fields are incorrect")
