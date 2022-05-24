Module new_project_name._validation.examples
============================================

Functions
---------

    
`run_example() ‑> None`
:   An example usage of the `new_project_name._validation.validating_base.ValidatingBaseClass` class.
    
    Simply executes two different methods using the same automatic type validation.

Classes
-------

`ActionExample()`
:   Shows an example usage of the `new_project_name._validation.validating_base.ValidatingBaseClass` class.
    
    Initialises a `ValidatingBaseClass` instance.

    ### Ancestors (in MRO)

    * new_project_name._validation.validating_base.ValidatingBaseClass

    ### Descendants

    * new_project_name._validation.examples.AdderExample
    * new_project_name._validation.examples.MultiplyerExample

    ### Methods

    `_validate_action(self, method_memo: typeguard._CallMemo) ‑> None`
    :   Validate that the data to be processed is in the correct format.
        
        Args:
            method_memo (_CallMemo): The `_CallMemo` which holds the method's typing information and arguments
        
        Raises:
            TypeError: Raised if the data is not the correct type
            ValueError: Raised if the types are correct, but there is an issue in the formatting

`AdderExample()`
:   A class that adds things.
    
    Initialises a `ValidatingBaseClass` instance.

    ### Ancestors (in MRO)

    * new_project_name._validation.examples.ActionExample
    * new_project_name._validation.validating_base.ValidatingBaseClass

    ### Methods

    `action(self, number_list: List[int]) ‑> int`
    :   Take a list of ints and sum all of the elements.
        
        The validation method in this case is `ActionExample._validate_action`.
        
        Args:
            number_list (List[int]): The list of ints
        
        Returns:
            int: The sum of all elements in the list

`MultiplyerExample()`
:   A class that multiplies things.
    
    Initialises a `ValidatingBaseClass` instance.

    ### Ancestors (in MRO)

    * new_project_name._validation.examples.ActionExample
    * new_project_name._validation.validating_base.ValidatingBaseClass

    ### Methods

    `action(self, number_list: List[int]) ‑> int`
    :   Take a list of ints and multiply all of the elements.
        
        The validation method in this case is `ActionExample._validate_action`.
        
        Args:
            number_list (List[int]): The list of ints
        
        Returns:
            int: The multiply of all elements in the list