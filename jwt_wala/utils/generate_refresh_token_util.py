import os
import json
import jwt
import datetime
from django.conf import settings


class GenerateRefreshTokenUtil:
    @staticmethod
    def refresh_token_generator(data):

        payload = {
            "user_uuid": data["user_uuid"],
            "user_type": data["user_type"],
            "iat": datetime.datetime.utcnow(),
            "nbf": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=3, minutes=5)
        }

        refresh_token = jwt.encode(
            payload,
            settings.REFRESH_TOKEN_SECRET,
            algorithm="HS256"

        )
        return refresh_token
