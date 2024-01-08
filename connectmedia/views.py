"""Home view for connectmedia project."""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
)


@api_view()
def home_view(request):
    """Home view for connectmedia project."""
    return Response(
        {
            "message": "Welcome to TeamAwesome ConnectMedia API service!",
            "available_routes": [
                "/admin",
                "/comments",
                "/followers",
                "/likes",
                "/posts",
                "/profiles",
            ],
        }
    )


@api_view(["POST"])
def logout_view(request):
    """Logout view"""
    response = Response()
    response.set_cookie(
        JWT_AUTH_COOKIE,
        value="",
        max_age=0,
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.data = {"message": "You've successfully logout"}
    return response
