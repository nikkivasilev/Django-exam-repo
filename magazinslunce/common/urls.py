from django.urls import path

from magazinslunce.common.views import index, CatalogueView, ProductsBasketView, like_product, add_product_to_basket, \
    rate_product, create_comment_product, delete_product_from_basket, subtract_product_from_basket, order, \
    redirect_to_catalogue, ProductCommentsView, delete_product_comment, UserLikedProductsView

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('redirect-catalogue/', redirect_to_catalogue, name='redirect to catalogue'),
    path('basket/', ProductsBasketView.as_view(), name='basket'),
    path('add-to-basket/<int:pk>/', add_product_to_basket, name='add product to basket'),
    path('subtract-from-basket/<int:pk>/', subtract_product_from_basket, name='subtract from basket'),
    path('delete-from-basket/<int:pk>/', delete_product_from_basket, name='delete product from basket'),
    path('order/', order, name='order'),
    path('like/<int:pk>/', like_product, name='like product'),
    path('liked-products/', UserLikedProductsView.as_view(), name='liked products'),
    path('rate/<int:pk>/', rate_product, name='rate product'),
    path('create-comment/<int:pk>/', create_comment_product, name='create comment product'),
    path('delete-comment/<int:pk>/', delete_product_comment, name='delete comment product'),
    path('product-comments/<int:pk>/', ProductCommentsView.as_view(), name='product comments'),
)
