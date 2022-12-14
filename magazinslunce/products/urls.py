from django.urls import path, include

from magazinslunce.products.views import DetailsProductView

urlpatterns = (
    path('<int:pk>/details/', DetailsProductView.as_view(), name='details product'),
)
