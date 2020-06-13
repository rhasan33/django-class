from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from user.serializers import UserSerializer
from user.models import User
from user.permissions import UserPermission


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        elif self.request.method == 'GET':
            return (UserPermission('can_get_users'),)
        raise MethodNotAllowed(method=self.request.method)

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.create_user(
                first_name=self.request.data['first_name'],
                last_name=self.request.data['last_name'],
                gender=self.request.data.get('gender', 'male'),
                email=self.request.data['email'],
                password=self.request.data['password'],
                username=self.request.data['username']
            )
            serializer = self.get_serializer(user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(data={'message': 'cannot create user'}, status=status.HTTP_409_CONFLICT)
