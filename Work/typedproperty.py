""" typedproperty.py
"""
###############################################################################
# Exercise 7.7: Using Closures to Avoid Repetition
# One of the more powerful features of closures is their use in generating
# repetitive code. If you refer back to Exercise 5.7, recall the code for
# defining a property with type checking.

# class Stock:
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#     ...
#     @property
#     def shares(self):
#         return self._shares

#     @shares.setter
#     def shares(self, value):
#         if not isinstance(value, int):
#             raise TypeError('Expected int')
#         self._shares = value
#     ...

# Instead of repeatedly typing that code over and over again, you can
# automatically create it using a closure.

# Make a file typedproperty.py and put the following code in it:

# # typedproperty.py

# def typedproperty(name, expected_type):
#     private_name = '_' + name
#     @property
#     def prop(self):
#         return getattr(self, private_name)

#     @prop.setter
#     def prop(self, value):
#         if not isinstance(value, expected_type):
#             raise TypeError(f'Expected {expected_type}')
#         setattr(self, private_name, value)

#     return prop

# Now, try it out by defining a class like this:

# from typedproperty import typedproperty

# class Stock:
#     name = typedproperty('name', str)
#     shares = typedproperty('shares', int)
#     price = typedproperty('price', float)

#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price

# Try creating an instance and verifying that type-checking works.

# >>> s = Stock('IBM', 50, 91.1)
# >>> s.name
# 'IBM'
# >>> s.shares = '100'
# ... should get a TypeError ...
# >>>
#------------------------------------------------------------------------------

# from typing import Any, Callable


# def typedproperty(name: str, expected_type: type) -> Callable:
#     private_name = '_' + name

#     @property
#     def prop(self: object) -> Any:
#         return getattr(self, private_name)

#     @prop.setter
#     def prop(self: object, value: Any):
#         if not isinstance(value, expected_type):
#             raise TypeError(f'Expected {expected_type}')
#         setattr(self, private_name, value)

#     return prop


###############################################################################
# Exercise 7.8: Simplifying Function Calls
# In the above example, users might find calls such as typedproperty('shares',
# int) a bit verbose to type–especially if they’re repeated a lot. Add the
# following definitions to the typedproperty.py file:

# String = lambda name: typedproperty(name, str)
# Integer = lambda name: typedproperty(name, int)
# Float = lambda name: typedproperty(name, float)

# Now, rewrite the Stock class to use these functions instead:

# class Stock:
#     name = String('name')
#     shares = Integer('shares')
#     price = Float('price')

#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price

# Ah, that’s a bit better. The main takeaway here is that closures and lambda
# can often be used to simplify code and eliminate annoying repetition. This is
# often good.
#------------------------------------------------------------------------------

from typing import Any, Callable


def typedproperty(name: str, expected_type: type) -> Callable:
    private_name = '_' + name

    @property
    def prop(self: object) -> Any:
        return getattr(self, private_name)

    @prop.setter
    def prop(self: object, value: Any):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop


String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)


###############################################################################
###############################################################################
