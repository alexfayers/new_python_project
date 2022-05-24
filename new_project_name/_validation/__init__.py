"""Functions and classes to do with validation. Mainly for internal use within the package."""

from . import examples
from .validating_base import ValidatingBaseClass

__all__ = ["ValidatingBaseClass", "examples"]

__pdoc__ = {
    "ValidatingBaseClass._validate_self": True,
    "ValidatingBaseClass._validate_argument_types": True,
    "ValidatingBaseClass._validate_return_type": True,
    "ValidatingBaseClass.__getattribute__": True,
}
