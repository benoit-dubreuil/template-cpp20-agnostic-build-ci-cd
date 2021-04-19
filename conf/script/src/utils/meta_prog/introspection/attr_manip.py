from typing import Optional


def get_or_create_attr(obj, attr: str, default_val: Optional = None):
    if not hasattr(obj, attr):
        attr_val = default_val
        setattr(obj, attr, default_val)
    else:
        attr_val = getattr(obj, attr)

    return attr_val
