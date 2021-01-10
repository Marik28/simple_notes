from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for list of notes"""

    class Meta:
        model = Note
        fields = ("id", "title", "text", "creation_date_timestamp", "update_date_timestamp")


class NoteCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a note"""

    class Meta:
        model = Note
        fields = ("title", "text")


class NoteUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating a note"""

    class Meta:
        model = Note
        fields = ("title", "text")

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
