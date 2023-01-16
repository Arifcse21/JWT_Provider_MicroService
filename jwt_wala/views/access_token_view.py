from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from jwt_wala.utils import GenerateAccessTokenUtil


class AccessTokenView(ViewSet):
    def create(self, request):
        print("data = ", request.data)

        data = {
            "user_uuid": request.data["user_uuid"],
            "user_type": request.data["user_type"]
        }

        access_token = GenerateAccessTokenUtil.access_token_generator(data)

        api_response = {
            "error": False,
            "message": "Access token",
            "access_token": access_token
        }

        return Response(api_response, status=status.HTTP_200_OK)
