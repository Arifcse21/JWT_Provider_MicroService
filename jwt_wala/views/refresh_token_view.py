from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from jwt_wala.utils import GenerateRefreshTokenUtil


class RefreshTokenView(ViewSet):
    def create(self, request):
        print("data = ", request.data)

        data = {
            "user_uuid": request.data["user_uuid"],
            "user_type": request.data["user_type"]
        }

        refresh_token = GenerateRefreshTokenUtil.refresh_token_generator(data)

        api_response = {
            "error": False,
            "message": "Refresh token",
            "refresh_token": refresh_token

        }
        return Response(api_response, status=status.HTTP_200_OK)
