from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UsersSerializer, RegisterSerializer, LoginSerializer


def get_token(user):
    user, token = AuthToken.objects.create(user)
    return token


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UsersSerializer

    def get_object(self):
        return self.request.user


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UsersSerializer(user, context=self.get_serializer_context()).data,
            "token": get_token(user)
        })


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UsersSerializer(user, context=self.get_serializer_context()).data,
            "token": get_token(user)
        })
