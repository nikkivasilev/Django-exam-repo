from django.urls import path, include

from magazinslunce.accounts.views import RegisterUserView, LogInUserView, LogOutUserView, DetailsUserView, EditUserView, \
    DeleteUserView

urlpatterns = (
    path('login/', LogInUserView.as_view(), name='login user'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('logout/', LogOutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', DetailsUserView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', DeleteUserView.as_view(), name='delete user'),
    ])),
)
