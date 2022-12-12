from django.urls import path, include

from magazinslunce.products.views import DetailsProductView

urlpatterns = (
    path('<int:pk>/details/', DetailsProductView.as_view(), name='details product'),

    # path('create/', CreateProductView.as_view(), name='create product'),
    # path('<int:pk>/', include([
    #     path('delete/', DeleteProductView.as_view, name='delete product'),
    #     path('edit/', EditProductView.as_view(), name='edit product'),
    #     path('details/', DetailsProductView.as_view(), name='details product'),
    # ])),

)
