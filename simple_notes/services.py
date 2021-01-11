from rest_framework.generics import get_object_or_404
from rest_framework.request import Request

from .exceptions import NotCorrectRequest
from .models import Note
from .serializers import NoteDetailSerializer
