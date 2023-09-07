from django.urls import path
from apps.products.views import ProductAPIView,ProductDetailAPIView


urlpatterns = [
    path('', ProductAPIView.as_view(), name='product-list'),
    path('product/<int:pk>',ProductDetailAPIView.as_view(), name='product-detail')

]

