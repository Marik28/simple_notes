from rest_framework import serializers

from .models import Note


class NoteListSerializer(serializers.ModelSerializer):
    """Serializer for list of notes"""

    class Meta:
        model = Note
        fields = ("id", "title", "text", "creation_date_timestamp", "update_date_timestamp")


class NoteDetailSerializer(serializers.ModelSerializer):
    """Serializer for a single note"""

    class Meta:
        model = Note
        fields = ("id", "title", "creation_date_timestamp", "update_date_timestamp",)


class NoteCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating a note"""
    class Meta:
        model = Note
        fields = ("title", "text")

    def create(self, validated_data):
        note = Note.objects.update_or_create(
            id=validated_data.get('id', None),
            defaults={
                'title': validated_data.get('title'),
                'text': validated_data.get('text'),
            }
        )
        return note
