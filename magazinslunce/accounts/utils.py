def get_full_name(obj):
    result = [obj.first_name, obj.last_name]
    if result[0] is not None or result[1] is not None:
        return " ".join(result)
    return None
