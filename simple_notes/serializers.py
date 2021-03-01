from rest_framework import serializers

from .models import Note


class NoteDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ("id", "title", "text", "creation_date_timestamp", "update_date_timestamp")
        read_only_fields = ("id",)
