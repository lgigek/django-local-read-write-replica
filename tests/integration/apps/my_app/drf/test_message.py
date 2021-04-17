import pytest
from rest_framework.response import Response
from rest_framework.test import APIClient

from django_local_read_write_replica.apps.my_app.models import Message


@pytest.mark.django_db
def test_should_return_201_and_create_message_object(api_client: APIClient):

    request_body = {"text": "this is a test"}

    response: Response = api_client.post("/api/v1/message", request_body, format="json")
    response_body = response.json()

    assert response.status_code == 201
    # Using '.using("default")' to bypass 'db_router'.
    # It's necessary due pytest's transaction, it isn't commited on database yet!
    assert Message.objects.using("default").filter(id=response_body["id"]).count() == 1


def test_should_return_400_for_none_text(api_client: APIClient):

    request_body = {"text": None}

    response: Response = api_client.post("/api/v1/message", request_body, format="json")

    assert response.status_code == 400
    assert response.json() == {"text": ["This field may not be null."]}
