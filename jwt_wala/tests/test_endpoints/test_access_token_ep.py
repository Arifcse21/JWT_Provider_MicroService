from django.urls import reverse
import uuid
import pytest

pytestmark = pytest.mark.django_db


class TestAccessTokenEp:
    ep = reverse('access_token-list')

    def test_access_token_ep(self, api_client):

        payload = {
            "user_uuid": uuid.uuid4(),
            "user_type": "admin"
        }
        response = api_client().post(self.ep, payload)
        resp = response.json()

        assert response.status_code == 200
        assert resp['error'] is False
        assert resp['message'] == 'Access token'

    @pytest.mark.xfail
    def test_access_token_dont_care_failure(self, api_client):
        payload = {
            "user_uuid": uuid.uuid5(uuid.uuid4(), "hi,babe"),
            "user_type": "babe"
        }
        response = api_client().post(self.ep, payload)

        assert response.status_code == 200  # 400

