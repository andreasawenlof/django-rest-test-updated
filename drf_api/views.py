from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my sexy API!"
    })


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=settings.REST_AUTH['JWT_AUTH_COOKIE'],
        value='',
        httponly=settings.REST_AUTH['JWT_AUTH_HTTPONLY'],
        secure=settings.REST_AUTH['JWT_AUTH_SECURE'],
        samesite=settings.REST_AUTH['JWT_AUTH_SAMESITE'],
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
    )
    response.set_cookie(
        key=settings.REST_AUTH['JWT_AUTH_REFRESH_COOKIE'],
        value='',
        httponly=settings.REST_AUTH['JWT_AUTH_HTTPONLY'],
        secure=settings.REST_AUTH['JWT_AUTH_SECURE'],
        samesite=settings.REST_AUTH['JWT_AUTH_SAMESITE'],
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
    )
    return response
