import time

from django.test import TestCase
from rest_framework.response import Response

from rest_framework.test import APIClient
from rest_framework import status


NOTE_LIST_URL = "/api/v1/"


def create_valid_note_data() -> dict:
    return {
        "title": "some title",
        "text": "some text",
    }


class NoteListViewTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def create_new_note(self) -> str:
        """Creates new note and returns its location"""
        note_fields = create_valid_note_data()
        create_response: Response = self.client.post(NOTE_LIST_URL, note_fields)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        return create_response["Location"]

    def change_fields(self, note: dict) -> dict:
        changed_note = note.copy()
        changed_note["title"] = str(time.time())
        return changed_note

    def test_create_valid_note(self):
        payload = create_valid_note_data()
        response: Response = self.client.post(NOTE_LIST_URL, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.has_header('Location'))

    def test_create_note_with_empty_body(self):
        payload = {}
        response: Response = self.client.post(NOTE_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_note_with_blank_title(self):
        payload = {"title": ""}
        response: Response = self.client.post(NOTE_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_and_get_valid_note(self):
        payload = create_valid_note_data()
        response: Response = self.client.post(NOTE_LIST_URL, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        note_location = response.get("Location")
        note_response: Response = self.client.get(note_location)
        self.assertEqual(note_response.status_code, status.HTTP_200_OK)
        for key, value in payload.items():
            self.assertEqual(value, note_response.data[key])

    def test_get_not_existing_note(self):
        invalid_note_id = "12345"
        url = f"{NOTE_LIST_URL}{invalid_note_id}/"
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_note_with_valid_data(self):
        # create new note
        note_fields = {
            "title": "initial title",
            "text": "initial text",
        }
        response: Response = self.client.post(NOTE_LIST_URL, note_fields)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        note_location = response["Location"]
        new_note_fields = {
            "title": "updated title",
            "text": "updated text",
        }
        update_response: Response = self.client.put(note_location, new_note_fields)
        self.assertEqual(update_response.status_code, status.HTTP_204_NO_CONTENT)
        for key, updated_field in new_note_fields.items():
            self.assertEqual(update_response.data[key], updated_field)

    def test_delete_note(self):
        # create new note
        note_fields = create_valid_note_data()
        create_response: Response = self.client.post(NOTE_LIST_URL, note_fields)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        note_location = create_response["Location"]

        # successfully get this note
        get_response = self.client.get(note_location)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        # delete this note and get status 204
        delete_response = self.client.delete(note_location)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # after this note no longer exists
        response = self.client.get(note_location)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_timestamp_changing(self):
        note_url = self.create_new_note()
        first_response: Response = self.client.get(note_url)
        note = first_response.data
        changed_note = self.change_fields(note)
        time.sleep(1)
        self.client.put(note_url, changed_note)

        second_response: Response = self.client.get(note_url)
        updated_note = second_response.data
        self.assertTrue(note["update_date_timestamp"] < updated_note["update_date_timestamp"])
