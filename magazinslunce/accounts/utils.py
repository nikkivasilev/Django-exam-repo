from magazinslunce.common.models import ProductBasket


def get_full_name(obj):
    result = [obj.first_name, obj.last_name]
    if result[0] is not None or result[1] is not None:
        return " ".join(result)
    return None


def get_user_products_in_basket(pk):
    return ProductBasket.objects.filter(user_id=pk).count()
