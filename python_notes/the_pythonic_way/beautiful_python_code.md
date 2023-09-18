# How to write beautiful python code

## Pep8
* This is a document that provides guidelines and best practices to write Python code. 
* The primary focus of PEP 8 is to improve the redability and consistncy of Python code.
  

### Why we need PEP8?

> "Redability counts"
>            
> -The zen of Python.

As Guido van Rossum said, **“Code is read much more often than it is written.”** You may spend a few minutes, or a whole day, writing a piece of code to process user authentication. Once you’ve written it, you’re never going to write it again. But you’ll definitely have to read it again. That piece of code might remain part of a project you’re working on. Every time you go back to that file, you’ll have to remember what that code does and why you wrote it, so readability matters.

## Naming Conventions

>"Explicit is better than implicit"
>
>-The zen of Python.

### Naming styles


| Type     | Naming convention                                                                                                              | Examples                                  |
| -------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| Function | Use a lowercase word or words. Separate words by underscores to improve readability.                                           | *function, my_function*                   |
| Variable | Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.                         | *x, var, my_variable*                     |
| Class    | Start each word with a capital letter. Do not separate words with underscores. This style is called camel case or pascal case. | *Model, MyClass*                          |
| Method   | Use a lowercase word or words. Separate words with underscores to improve readability.                                         | *class_method, method*                    |
| Constant | Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.                        | *CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT* |
| Module   | Use a short, lowercase word or words. Separate words with underscores to improve readability.                                  | *module.py, my_module.py*                 |
| Package  | Use a short, lowercase word or words. Do not separate words with underscores.                                                  | *package, mypackage*                      |


## Code Layout

> "Beautiful is better than ugly"
>
> -The zen of Python


### Blank Lines

Vertical whitespace, or blank lines, can greatly improve the readability of your code. Code that’s bunched up together can be overwhelming and hard to read. Similarly, too many blank lines in your code makes it look very sparse, and the reader might need to scroll more than necessary. Below are three key guidelines on how to use vertical whitespace.

**1. Surround top-level functions and classes with two blank lines.**

```Python
class MyFirstClass:
    pass
# blank line
# blank line
class MySecondClass:
    pass
# blank line
# blank line
def top_level_function():
    return None
```


**2. Surround method definitions inside classes with a single blank line.**
```Python
class MyClass:
    def first_method(self):
        return None
    # blank line
    def second_method(self):
        return None
```

**3. Use blank lines sparingly inside functions to show clear steps.** Sometimes, a complicated function has to complete several steps before the return statement. To help the reader understand the logic inside the function, it can be helpful to leave a blank line between each step.


```Python
def calculate_variance(number_list):
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number
    mean = sum_list / len(number_list)
    # blank line
    sum_squares = 0
    for number in number_list:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(number_list)
    # blank line
    return mean_squares - mean**2
```

### Maximum Line Length and Line Breaking
PEP 8 suggests lines should be limited to **79 characters.** This is because it allows you to have multiple files open next to one another, while also avoiding line wrapping.

Python will assume line continuation if code is contained within parentheses, brackets, or braces:

```Python
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
```
If it is impossible to use implied continuation, then you can use backslashes to break lines instead:

```Python
from mypkg import example1, \
    example2, example3
```

```Python
# Recommended
total = (first_variable
         + second_variable
         - third_variable)
```

```Python
# Not Recommended
total = (first_variable +
         second_variable -
         third_variable)
```

## Indentation

> “There should be one—and preferably only one—obvious way to do it.”
>
>— The Zen of Python

Indentation, or leading whitespace, **is extremely important in Python.** The indentation level of lines of code in Python determines how statements are grouped together.

```Python
x = 3
if x > 5:
    print('x is larger than 5')
```

The indented print statement lets Python know that it should only be executed if the if statement returns True. The same indentation applies to tell Python what code to execute when a function is called or what code belongs to a given class.

The key indentation rules laid out by PEP 8 are the following:

- Use 4 consecutive spaces to indicate indentation.
- Prefer spaces over tabs.

## Comments
>“If the implementation is hard to explain, it’s a bad idea.”
>
>— The Zen of Python

You should use comments to document code as it’s written. It is important to document your code so that you, and any collaborators, can understand it.

Here are some key points to remember when adding comments to your code:

- Limit the line length of comments and docstrings to 72 characters.
- Use complete sentences, starting with a capital letter.
- Make sure to update comments if you change your code.

### Block comments

```Python
for i in range(0, 10):
    # Loop over i ten times and print out the value of i, followed by a
    # new line character
    print(i, '\n')
```

### Inline Comments
Inline comments explain a **single statement** in a piece of code. They are useful to remind you, or explain to others, why a certain line of code is necessary. Here’s what PEP 8 has to say about them:

- Use inline comments sparingly.
- Write inline comments on the same line as the statement they refer to.
- Separate inline comments by two or more spaces from the statement.
- Start inline comments with a # and a single space, like block comments.
- Don’t use them to explain the obvious.

```Python
x = 5  # This is an inline comment
```

```Python
empty_list = []  # Initialize empty list

x = 5
x = x * 5  # Multiply x by 5
```

### Documentation Strings
Documentation strings, or docstrings, are strings enclosed in **double (""") or single (''') quotation marks** that appear on the first line of any function, class, method, or module. You can use them to explain and document a specific block of code.

- Surround docstrings with three double quotes on either side, as in """This is a docstring""".

- Write them for all public modules, functions, classes, and methods.

- Put the """ that ends a multiline docstring on a line by itself:

```Python
def quadratic(a, b, c, x):
    """Solve quadratic equation via the quadratic formula.

    A quadratic equation has the following form:
    ax**2 + bx + c = 0

    There always two solutions to a quadratic equation: x_1 & x_2.
    """
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)

    return x_1, x_2
```
- For one-line docstrings, keep the """ on the same line:

```Python
def quadratic(a, b, c, x):
    """Use the quadratic formula"""
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)

    return x_1, x_2
```
## Whitespace in Expressions and Statements

>“Sparse is better than dense.”
>
>— The Zen of Python

Whitespace can be very helpful in expressions and statements when used properly. If there is not enough whitespace, then code can be difficult to read, as it’s all bunched together. If there’s too much whitespace, then it can be difficult to visually combine related terms in a statement.

### Whitespace Around Binary Operators
- Assignment operators (=, +=, -=, and so forth)

- Comparisons (==, !=, >, <. >=, <=) and (is, is not, in, not in)

- Booleans (and, not, or)

**Note**: When = is used to assign a default value to a function argument, do not surround it with spaces.


```Python
# Recommended
def function(default_parameter=5):
    # ...

# Not recommended
def function(default_parameter = 5):
    # ...
```

```Python
# Recommended
y = x**2 + 5
z = (x+y) * (x-y)

# Not Recommended
y = x ** 2 + 5
z = (x + y) * (x - y)

# Definitely do not do this!
if x >5 and x% 2== 0:
    print('x is larger than 5 and divisible by 2!')

# Not recommended
if x > 5 and x % 2 == 0:
    print('x is larger than 5 and divisible by 2!')

# Recommended
if x>5 and x%2==0:
    print('x is larger than 5 and divisible by 2!')
```
### When to Avoid Adding Whitespace
In some cases, adding whitespace can make code harder to read. Too much whitespace can make code overly sparse and difficult to follow. PEP 8 outlines very clear examples where whitespace is inappropriate.

The most important place to avoid adding whitespace is at the end of a line. This is known as **trailing whitespace**. It is invisible and can produce errors that are difficult to trace.

The following list outlines some cases where you should avoid adding whitespace:

**Immediately inside parentheses, brackets, or braces:**
```Python
# Recommended
my_list = [1, 2, 3]

# Not recommended
my_list = [ 1, 2, 3, ]
```
**Before a comma, semicolon, or colon:**
```Python
x = 5
y = 6

# Recommended
print(x, y)

# Not recommended
print(x , y)
```
**Before the open parenthesis that starts the argument list of a function call:**
```Python
def double(x):
    return x * 2

# Recommended
double(3)

# Not recommended
double (3)
```

**Before the open bracket that starts an index or slice:**
```Python
# Recommended
list[3]

# Not recommended
list [3]
```
**Between a trailing comma and a closing parenthesis:**
```Python
# Recommended
tuple = (1,)

# Not recommended
tuple = (1, )
```

**To align assignment operators:**

```Python
# Recommended
var1 = 5
var2 = 6
some_long_var = 7

# Not recommended
var1          = 5
var2          = 6
some_long_var = 7
```

## Programming Recommendations
>“Simple is better than complex.”
>
>— The Zen of Python

You will often find that there are several ways to perform a similar action in Python (and any other programming language for that matter). In this section, you’ll see some of the suggestions PEP 8 provides to remove that ambiguity and preserve consistency.

**Don’t compare Boolean values to True or False using the equivalence operator.**

```Python
# Not recommended
my_bool = 6 > 5
if my_bool == True:
    return '6 is bigger than 5'

# Recommended
if my_bool:
    return '6 is bigger than 5'
```

**Use the fact that empty sequences are falsy in if statements.**

```Python
# Not recommended
my_list = []
if not len(my_list):
    print('List is empty!')

# Recommended
my_list = []
if not my_list:
    print('List is empty!')
```

**Use is not rather than not ... is in if statements.**

If you are trying to check whether a variable has a defined value, there are two options. The first is to evaluate an if statement with x is not None, as in the example below, a second option would be to evaluate x is None and then have an if statement based on not the outcome:

```Python
# Recommended
if x is not None:
    return 'x exists!'

# Not recommended
if not x is None:
    return 'x exists!'
```

**Don’t use if x: when you mean if x is not None**

```Python
# Not Recommended
if arg:
    # Do something with arg... 

# Recommended
if arg is not None:
    # Do something with arg...
```

## References

For more information see: [_How to Write Beautiful Python Code With PEP 8_](https://realpython.com/python-pep8/#comments)