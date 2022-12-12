from django.contrib.auth.views import redirect_to_login
from django.urls import path

from magazinslunce.common.views import index, CatalogueView, ProductsBasketView, like_product, add_product_to_basket, \
    rate_product, comment_product, delete_product_from_basket, subtract_product_from_basket, order, redirect_to_catalogue

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('basket/', ProductsBasketView.as_view(), name='basket'),
    path('like/<int:pk>/', like_product, name='like product'),
    path('add-to-basket/<int:pk>/', add_product_to_basket, name='add product to basket'),
    path('subtract-from-basket/<int:pk>/', subtract_product_from_basket, name='subtract from basket'),
    path('delete-from-basket/<int:pk>/', delete_product_from_basket, name='delete product from basket'),
    path('order/', order, name='order'),
    path('rate/<int:pk>/', rate_product, name='rate product'),
    path('comment/<int:pk>/', comment_product, name='comment product'),
    path('redirect_catalogue/', redirect_to_catalogue, name='redirect to catalogue'),
)
