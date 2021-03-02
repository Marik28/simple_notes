# NOTES

This is my test project - API service for keeping notes 
This service allows you to create, update, delete notes

A is represented in JSON in the following format:

    {
        "id": "fc812336-e545-41a9-96fd-61b1601d443c",
        "title": "kekw",
        "text": "lol",
        "creation_date_timestamp": 1607432910,
        "update_date_timestamp": 1607432910
    }

Where 
* __id__ - unique uuid4 identifier if a note
* __title__ - title of a note
* __text__ - text of a note
* __creation_date_timestamp__ - integer, _unix timestamp_, date the note was created
* __update_date_timestamp__ - integer, _unix timestamp_, date the note was last edited

# Installation and launch:

> $ git clone https://github.com/Marik28/simple_notes.git

> $ cd simple_notes

> $ pip install -r requirements.txt

> $ python manage.py runserver

# Provided URL with request methods:

## GET / 

Returns a list of notes in the following format:

    [
        {
            "id": "fc812336-e545-41a9-96fd-61b1601d443c",
            "title": "kekw",
            "text": "lol",
            "creation_date_timestamp": 1607432910,
            "update_date_timestamp": 1607432910
        },
        {
            "id": "e38c0144-54df-4783-bb86-200586774c4a",
            "title": "to be or not to be",
            "text": "vot v chem vopros",
            "creation_date_timestamp": 1607436479,
            "update_date_timestamp": 1607436479
        },
        {
            "id": "dc991384-9561-4e73-bf58-aab45154d8bd",
            "title": "а так?",
            "text": "текст",
            "creation_date_timestamp": 1607443463,
            "update_date_timestamp": 1607443463
        }
    ]

## POST /

This method is used to create a new note by sending its title and text

Required request:

    {
        "title": "some title",
        "text": "som text"
    }

## PUT /\{note_id} 

This method is used to update data of an existing note

Request example:

    {
        "title": "new title",
        "text": "new text"
    }

## DELETE /\{note_id} 

This method is used to delete a note.

## GET /\{note-id}

Returns a note instance.
