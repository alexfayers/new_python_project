Module new_project_name._validation.validating_base
===================================================
Things to do with self-validation and inheritance stuff goes in here.

Classes
-------

`ValidatingBaseClass()`
:   A class which automatically validates the inputs and outputs of specified methods.
    
    Initialises a `ValidatingBaseClass` instance.

    ### Descendants

    * new_project_name._validation.examples.ActionExample

    ### Class variables

    `required_methods: List[str]`
    :   Methods that must be implemented in any child classes

    `validated_methods: List[str]`
    :   Methods that must be validated in any child classes.
        
        The `_validate_XXX` naming scheme should be used when creating a validation function.

    ### Methods

    `__getattribute__(self, _ValidatingBaseClass__name: str) ‑> Any`
    :   Called when an attribute of the object is attempted to be accessed.
        
        Ensures that child classes are structured correctly, and that the inputs for the methods specified
        in `ValidatingBaseClass.validated_methods` are validated before a method is executed.
        
        Args:
            __name (str): The attribute which is being accessed
        
        Raises:
            NotImplementedError: Raised if a required method does not exist
        
        Returns:
            Any: The value of the attribute

    `_validate_argument_types(self, method_memo: typeguard._CallMemo) ‑> None`
    :   Validate that the arguments to a method are the correct type.
        
        Args:
            method_memo (_CallMemo): The `_CallMemo` which holds the method's typing information and arguments
        
        Raises:
            TypeError: if there is an argument type mismatch

    `_validate_return_type(self, method_memo: typeguard._CallMemo, result: Any) ‑> None`
    :   Validate that the return value of a method is the correct type.
        
        Args:
            method_memo (_CallMemo): The `_CallMemo` which holds the method's typing information and arguments
            result (Any): The actual result from the method
        
        Raises:
            TypeError: if there is a type mismatch in the return value

    `_validate_self(self) ‑> None`
    :   Validate that the class has the specified methods defined.
        
        Reads the required method from the `ValidatingBaseClass.required_methods` attribute.
        
        Raises:
            NotImplementedError: Raised if a required method is not defined.