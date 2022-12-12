from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic as view

from magazinslunce.common.forms import ProductRatingForm, CommentForm
from magazinslunce.common.models import ProductBasket, ProductLike
from magazinslunce.common.utils import get_product_url, GetProductsPks, user_rated_product, \
    sum_total_checkout_price
from magazinslunce.products.models import Product


def index(request):
    return render(request, 'common/home-page.html')


class CatalogueView(LoginRequiredMixin, view.ListView):
    template_name = 'common/catalogue.html'
    model = Product
    paginate_by = 4


class ProductsBasketView(LoginRequiredMixin, view.ListView):
    template_name = 'common/basket.html'
    model = ProductBasket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_basket'] = ProductBasket.objects.filter(user_id=self.request.user.pk).order_by(
                'product__name')
            context['total_sum'] = sum_total_checkout_price(self.request.user.pk)
            product_pks = GetProductsPks(self.request.user.pk)
            if product_pks:
                products = []
                for product_pk in product_pks:
                    products.append(Product.objects.filter(pk=product_pk).get())
                context['products'] = products

        return context


@login_required
def comment_product(request, pk):
    if request.method == "POST":
        product = Product.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()

        return redirect(get_product_url(request))


@login_required
def rate_product(request, pk):
    if request.method == 'POST':
        form = ProductRatingForm(request.POST)
        product = Product.objects.get(id=pk)
        already_rated = user_rated_product(pk, request.user.pk)

        if form.is_valid() and not already_rated:
            rating = form.save(commit=False)
            rating.product = product
            rating.user = request.user
            rating.save()

        return redirect(get_product_url(request))


@login_required
def like_product(request, pk):
    user_liked_products = ProductLike.objects \
        .filter(product_id=pk, user_id=request.user.pk)

    if user_liked_products:
        user_liked_products.delete()
    else:
        ProductLike.objects.create(
            product_id=pk,
            user_id=request.user.pk,
        )

    return redirect(get_product_url(request))


@login_required
def add_product_to_basket(request, pk):
    user_basket_product = ProductBasket.objects \
        .filter(product_id=pk, user_id=request.user.pk)

    if not user_basket_product:
        ProductBasket.objects.create(
            product_id=pk,
            user_id=request.user.pk,
            quantity=1
        )
    else:
        current_product = user_basket_product.get(product_id=pk)
        current_product.quantity += 1
        current_product.save()

    return redirect(get_product_url(request))


@login_required
def subtract_product_from_basket(request, pk):
    product = ProductBasket.objects \
        .filter(product_id=pk, user_id=request.user.pk).get()

    if product.quantity <= 1:
        return delete_product_from_basket(request, pk)
    product.quantity -= 1
    product.save()

    return redirect(get_product_url(request))


@login_required
def delete_product_from_basket(request, pk):
    ProductBasket.objects \
        .filter(product_id=pk, user_id=request.user.pk).delete()
    return redirect('basket')


@login_required
def order(request):
    user_basket_products = ProductBasket.objects.filter(user_id=request.user.pk)
    if user_basket_products:
        for product in user_basket_products:
            ProductBasket.objects.get(product_id=product.product_id, user_id=request.user.pk).delete()
        return render(request, 'common/order-made.html')

    return redirect('redirect to catalogue')

@login_required
def redirect_to_catalogue(request):
    if request.user.is_authenticated:
        return redirect('catalogue')
