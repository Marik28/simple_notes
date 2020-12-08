import datetime as dt

from models import Note

notes = Note.objects.all()
for note in notes:
    print(note)
