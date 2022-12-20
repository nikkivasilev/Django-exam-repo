from magazinslunce.common.models import ProductLike, ProductRating, ProductComment, ProductBasket
from magazinslunce.products.models import Product


def get_product_likes(pk):
    return ProductLike.objects.filter(product_id=pk).count()


def get_product_rating(pk):
    all_ratings = [product.rating for product in ProductRating.objects.filter(product_id=pk).all()]
    if all_ratings:
        rating = sum(all_ratings) / len(all_ratings)
    else:
        rating = 0
    return f'{rating:.2f}'


def get_product_url(request):
    return request.META['HTTP_REFERER']


def get_product_comments(pk):
    return ProductComment.objects.filter(product_id=pk).all()


def get_products_pks(user, objs):
    objects = objs.objects.filter(user_id=user.id).all()
    products_pks = [obj.product_id for obj in objects]
    return products_pks


def get_user_products(user, objs):
    product_pks = get_products_pks(user, objs)
    products = []
    for product_pk in product_pks:
        products.append(Product.objects.filter(pk=product_pk).get())
    return products


def user_liked_product(product_pk, user_pk):
    if ProductLike.objects.filter(product_id=product_pk, user_id=user_pk).count() >= 1:
        return True
    return False


def user_rated_product(product_pk, user_pk):
    obj = ProductRating.objects.filter(product_id=product_pk, user_id=user_pk)
    if obj:
        return obj
    return False


def sum_total_checkout_price(user_pk):
    user_basket = ProductBasket.objects.filter(user_id=user_pk)
    total = 0
    for product in user_basket:
        total += product.quantity * product.product.price
    return total
