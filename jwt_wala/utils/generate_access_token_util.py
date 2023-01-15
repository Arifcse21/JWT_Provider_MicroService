import os
import jwt
import datetime
import json
from django.conf import settings


class GenerateAccessTokenUtil:
    @staticmethod
    def access_token_generator(data):
        user_uuid = data["user_uuid"]
        user_type = data["user_type"]

        access_token_payload = {
            "user_uuid": user_uuid,
            "user_type": user_type,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=5, minutes=10),
            "iat": datetime.datetime.utcnow()
        }

        access_token = jwt.encode(
            access_token_payload,
            settings.SECRET_KEY,
            algorithm="HS256"
        )

        return access_token

