Module new_project_name._helpers.decorators
===========================================

Functions
---------

    
`singleton(cls: Callable) ‑> Callable`
:   A decorator which prevents new instances of a class from being created.
    
    If an instance of the class already exists, it is returned instead.
    
    Args:
        cls (Callable): The class to wrap
    
    Returns:
        Callable: The new or existing instance of the class