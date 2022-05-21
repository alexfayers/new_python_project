from functools import wraps
from typing import Callable


def singleton(cls: Callable) -> Callable:
    """A decorator which prevents new instances of a class from being created.

    If an instance of the class already exists, it is returned instead.

    Args:
        cls (Callable): The class to wrap

    Returns:
        Callable: The new or existing instance of the class
    """
    instances = {}

    @wraps(cls)
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton
