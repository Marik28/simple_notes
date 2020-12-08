import datetime as dt
import uuid

from django.db import models


class Note(models.Model):
    """Model representing a note instance"""
    id = models.UUIDField('identifier', primary_key=True, default=uuid.uuid4)
    title = models.CharField('title', max_length=30)
    text = models.TextField('text', max_length=500, blank=True)
    creation_date = models.DateTimeField('creation_date', auto_now_add=True)
    update_date = models.DateTimeField('update_date', auto_now=True)

    def __str__(self):
        return self.title

    def creation_date_timestamp(self) -> int:
        """Returns a timestamp of a note creation date"""
        return int(self.creation_date.timestamp())

    def update_date_timestamp(self) -> int:
        """Returns a timestamp of a note last update date"""
        return int(self.update_date.timestamp())
