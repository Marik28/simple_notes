from rest_framework import serializers

from .models import Note


class NoteDetailSerializer(serializers.ModelSerializer):
    """Serializer for list of notes"""

    class Meta:
        model = Note
        fields = ("id", "title", "text", "creation_date_timestamp", "update_date_timestamp")


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "title", "text")
