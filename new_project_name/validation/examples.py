"""Example usages for the `new_project_name.validation.ValidatingBaseClass` class."""

from typing import List

from typeguard import _CallMemo

from .validating_base import ValidatingBaseClass


class ActionExample(ValidatingBaseClass):
    """Shows an example usage of the `new_project_name.validation.ValidatingBaseClass` class."""

    required_methods: List[str] = ["action"]
    validated_methods: List[str] = ["action"]

    def validate_action(self, method_memo: _CallMemo) -> None:
        """Validate that the data to be processed is in the correct format.

        Args:
            method_memo (_CallMemo): The `_CallMemo` which holds the method's typing information and arguments

        Raises:
            TypeError: Raised if the data is not the correct type
            ValueError: Raised if the types are correct, but there is an issue in the formatting
        """
        for number in method_memo.arguments["number_list"]:
            if not isinstance(number, int):
                raise TypeError(f"{number} is not an integer")


class AdderExample(ActionExample):
    """A class that adds things."""

    def action(self, number_list: List[int]) -> int:
        """Take a list of ints and sum all of the elements.

        The validation method in this case is `ActionExample.validate_action`.

        Args:
            number_list (List[int]): The list of ints

        Returns:
            int: The sum of all elements in the list
        """
        total = 0
        for number in number_list:
            total = total + number

        return total


class MultiplyerExample(ActionExample):
    """A class that multiplies things."""

    def action(self, number_list: List[int]) -> int:
        """Take a list of ints and multiply all of the elements.

        The validation method in this case is `ActionExample.validate_action`.

        Args:
            number_list (List[int]): The list of ints

        Returns:
            int: The multiply of all elements in the list
        """
        total = 1
        for number in number_list:
            total = total * number

        return total


def run_example() -> None:
    """An example usage of the `new_project_name.validation.ValidatingBaseClass` class.

    Simply executes two different methods using the same automatic type validation.
    """
    classes = [AdderExample, MultiplyerExample]

    for _class in classes:
        _object = _class()
        total = _object.action([1, 2, 3, 4, 5])
        print(total)
