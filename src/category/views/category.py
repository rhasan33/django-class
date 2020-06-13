from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from category.models import Category
from category.serializers import CategorySerializer
from category.tasks import create_category


class CategoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def create(self, request, *args, **kwargs):
        create_category.delay(request.data)
        return Response({'message': 'Request is processing'}, status=status.HTTP_200_OK)


class CategoryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()
    lookup_field = 'id'






















