from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jwt_wala.views import (
    AccessTokenView,
    RefreshTokenView
)
from django.conf import settings
url = settings.URLS


router = DefaultRouter()


router.register(url["access_token"], AccessTokenView, basename="access_token")
router.register(url["refresh_token"], RefreshTokenView, basename="refresh_token")

urlpatterns = [
    path(url['jwt_wala_api'], include(router.urls)),
]
