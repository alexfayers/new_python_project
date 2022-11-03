"""Useful decorators."""

from functools import wraps
from typing import Any, Callable


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
    def _singleton(*args: Any, **kwargs: Any) -> Any:
        cls_info = (
            str(cls) + str(args) + str(kwargs)
        )  # is there a better way to do this?
        if cls_info not in instances:
            instances[cls_info] = cls(*args, **kwargs)
        return instances[cls_info]

    return _singleton
