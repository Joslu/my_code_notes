"""'Classes:
Class names should follow the UpperCaseCamelCase convention
Python's built-in classes, however are typically lowercase words
Exception classes should end with (suffix) “Exception”
"""


class PyramidGiza:
    pass


class InputException:  # Exception
    pass


"""Instance Variables:
- Instance variable names should be all lower case
- Words in an instance variable name should be separated by an underscore
- Protected instance variables should begin with a single underscore
- Private instance variables should begin with two underscores
"""
pyramid_giza = "pyramid of giza"  # Public
_pyramid_giza = "pyramid of giza"  # Protected
__pyramid_giza = "pyramid of giza"  # Private


"""Methods:
- Method names should be all lower case
- Words in an method name should be separated by an underscore
- Protected method should begin with a single underscore
- Private method should begin with two underscores underscore
"""


def pyramid_giza():  # Public
    pass


def _pyramid_giza():  # Protected
    pass


def __pyramid_giza():  # Private
    pass
