from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from magazinslunce.accounts.forms import CreateUserForm
from magazinslunce.common.models import ProductBasket

UserModel = get_user_model()


def get_full_name(obj):
    result = [obj.first_name, obj.last_name]
    if result[0] is not None or result[1] is not None:
        return " ".join(result)
    return None


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class LogInUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    model = UserModel


class LogOutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class DetailsUserView(views.DetailView):
    template_name = 'accounts/details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fullname'] = get_full_name(self.object)
        context['products_in_basket'] = ProductBasket.objects.filter(user_id=self.request.user.pk).count()
        return context


class DeleteUserView(views.DeleteView):
    template_name = 'accounts/delete.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def post(self, *args, **kwargs):
        response = super().post(*args, **kwargs)

        return response

class EditUserView(views.UpdateView):
    template_name = 'accounts/edit.html'
    model = UserModel
    fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response

# USERNAME: NikolaUser
# PASSWORD: Parola@123
