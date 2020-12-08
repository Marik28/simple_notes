#NOTES

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
To get started just copy this repository

You'll need to install required python packages by following command:

> $ pip install -r requirements.txt

## Provided URL with request methods:

#GET / 

Returns a list of notes in the following format:

    {
        "success": true,
        "note": [
            {
                "id": "fc812336-e545-41a9-96fd-61b1601d443c",
                "title": "kekw",
                "text": "lol",
                "creation_date_timestamp": 1607432910,
                "update_date_timestamp": 1607432910
            },
            {
                "id": "e38c0144-54df-4783-bb86-200586774c4a",
                "title": "a kak kakat'",
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
    }

##POST /

This method is used to create a new note by sending its title and text

Required request:

    {
        "title": "some title",
        "text": "som text"
    }

If data is correct, creates a new note and returns its id:

    {
        "success": true,
        "note_id": "4ec8a398-8465-46de-ab3c-3981f3329bae"
    }


##PUT / 

This method is used to update data of an existing note by its id. If update was successful, returns 
    
    {
        "success": true
    }

Example:

    {
        "id": "dc991384-9561-4e73-bf58-aab45154d8bd",
        "title": "new title",
        "text": "new text"
    }

##DELETE / 

This method is used to delete a note by given id. If a note was deleted successfully, returns status 204

Example:

    {
        "id": "dc991384-9561-4e73-bf58-aab45154d8bd",
    }

##GET /\<note-id>

Returns a note by given id