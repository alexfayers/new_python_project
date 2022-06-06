"""Things to do with self-validation and inheritance stuff goes in here."""

import logging
from functools import wraps
from typing import Any, List

from typeguard import (
    _CallMemo,
    check_argument_types,
    check_return_type,
    function_name,
    qualified_name,
)

logger = logging.getLogger(__name__)


class ValidatingBaseClass:
    """A class which automatically validates itself.

    The inputs and outputs of specified methods are validated through the use of the `validated_methods` class variable,
    and any methods are are required to be implemented in child classes are defined within the `required_methods`
    class variable.

    Example usage can be seen in `new_project_name.validation.examples`.
    """

    required_methods: List[str] = []
    """Methods that must be implemented in any child classes"""
    validated_methods: List[str] = []
    """Methods that must be validated in any child classes.

    The `validate_XXX` naming scheme should be used when creating a validation function.
    All `validate_XXX` methods should accept a single argument, which is a `_CallMemo` object.
    """

    _self_validated = False

    def __init__(self) -> None:
        """Initialises a `ValidatingBaseClass` instance."""
        self._validate_self()

    def _validate_self(self) -> None:
        """Validate that the class has the specified methods defined.

        Reads the required method from the `ValidatingBaseClass.required_methods` attribute.

        Raises:
            NotImplementedError: Raised if a required method is not defined.
        """
        logger.debug(f"Validating methods of '{qualified_name(self)}'")
        for required_method in self.required_methods:
            method = getattr(self, required_method, None)
            if not callable(method):
                raise NotImplementedError(
                    f"The {required_method} method must be defined."
                )
        self._self_validated = True
        logger.debug(f"-> Methods of '{qualified_name(self)}' are ok")

    def _validate_argument_types(self, method_memo: _CallMemo) -> None:
        """Validate that the arguments to a method are the correct type.

        Args:
            method_memo (_CallMemo): The `_CallMemo` which holds the method's typing information and arguments

        Raises:
            TypeError: if there is an argument type mismatch
        """
        logger.debug(f"Validating arguments for '{method_memo.func_name}'")
        check_argument_types(method_memo)
        logger.debug(f"-> Arguments for '{method_memo.func_name}' are ok")

    def _validate_return_type(self, method_memo: _CallMemo, result: Any) -> None:
        """Validate that the return value of a method is the correct type.

        Args:
            method_memo (_CallMemo): The `_CallMemo` which holds the method's typing information and arguments
            result (Any): The actual result from the method

        Raises:
            TypeError: if there is a type mismatch in the return value
        """
        logger.debug(f"Validating return type of '{method_memo.func_name}'")
        check_return_type(result, method_memo)
        logger.debug(f"-> Return type of '{method_memo.func_name}' is ok")

    def __getattribute__(self, __name: str) -> Any:
        """Called when an attribute of the object is attempted to be accessed.

        Ensures that child classes are structured correctly, and that the inputs for the methods specified
        in `ValidatingBaseClass.validated_methods` are validated before a method is executed.

        Args:
            __name (str): The attribute which is being accessed

        Raises:
            NotImplementedError: Raised if a required method does not exist

        Returns:
            Any: The value of the attribute
        """
        method = super().__getattribute__(__name)

        if (
            callable(method)
            and self._self_validated
            and __name in self.validated_methods
        ):
            validator_name = f"validate_{__name}"
            validator = super().__getattribute__(validator_name)
            if not validator:
                raise NotImplementedError(
                    f"The {__name} method does not have a validator ({validator_name})"
                )

            @wraps(method)
            def _validated(*args: Any, **kwargs: Any) -> Any:
                """Decorator that runs the specified validator before the decorated method.

                Returns:
                    Any: The return value of the method
                """
                method_memo = _CallMemo(method, args=args, kwargs=kwargs)
                self._validate_argument_types(method_memo)

                logger.debug(
                    f"Validating inputs for '{function_name(method)}' using '{function_name(validator)}'"
                )
                validator(method_memo)
                logger.debug(f"-> Inputs for '{function_name(method)}' are ok")
                result = method(*args, **kwargs)
                self._validate_return_type(method_memo, result)
                return result

            return _validated
        else:
            return method
