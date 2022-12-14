from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views

from magazinslunce.common.forms import ProductRatingForm, CommentForm
from magazinslunce.common.models import ProductLike
from magazinslunce.common.utils import get_product_likes, get_product_rating, get_product_comments, user_rated_product
from magazinslunce.products.models import Product

UserModel = get_user_model()


def user_liked_product(product_pk, user_pk):
    if ProductLike.objects.filter(product_id=product_pk, user_id=user_pk).count() >= 1:
        return True
    return False


class DetailsProductView(LoginRequiredMixin, views.DetailView):
    template_name = 'products/details.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_likes'] = get_product_likes(self.object.pk)
        context['user_liked_product'] = user_liked_product(self.object.pk, self.request.user.pk)
        context['user_rated_product'] = user_rated_product(self.object.pk, self.request.user.pk)
        context['product_rating'] = get_product_rating(self.object.pk)
        context['product_comments'] = get_product_comments(self.object)
        context['rate_form'] = ProductRatingForm()
        context['comment_form'] = CommentForm()

        return context
