from magazinslunce.common.models import ProductLike, ProductRating, ProductComment, ProductBasket


def get_product_likes(pk):
    total_likes = ProductLike.objects.filter(product_id=pk).count()
    return total_likes


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


def GetProductsPks(user_id):
    basket = ProductBasket.objects.filter(user_id=user_id).all()
    products = [obj.product_id for obj in basket]
    if products:
        return products

    return []


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
