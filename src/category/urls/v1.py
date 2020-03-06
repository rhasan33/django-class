from django.urls import path

from category.views import CategoryListCreateAPIView, CategoryRetrieveUpdateAPIView

urlpatterns = [
    path('', CategoryListCreateAPIView.as_view(), name='category-list-create-api'),
    path('<int:id>/', CategoryRetrieveUpdateAPIView.as_view(), name='category-get-update-api')
]
