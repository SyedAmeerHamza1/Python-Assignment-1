# Python Assignment 8

"""
1. In Python, what is the difference between a built-in function and a user-defined function? Provide an
example of each.
2. How can you pass arguments to a function in Python? Explain the difference between positional
arguments and keyword arguments.
3. What is the purpose of the return statement in a function? Can a function have multiple return
statements? Explain with an example.
4. What are lambda functions in Python? How are they different from regular functions? Provide an
example where a lambda function can be useful.
5. How does the concept of "scope" apply to functions in Python? Explain the difference between local
scope and global scope.
6. How can you use the "return" statement in a Python function to return multiple values?
7. What is the difference between the "pass by value" and "pass by reference" concepts when it
comes to function arguments in Python?
8. Create a function that can intake integer or decimal value and do following operations:
a. Logarithmic function (log x)
b. Exponential function (exp(x))
c. Power function with base 2 (2x)
d. Square root
9. Create a function that takes a full name as an argument and returns first name and last name
"""

# 1. In Python, what is the difference between a built-in function and a user-defined function? Provide an example of
# each.


'''The difference between a built-in function and user-defined function
built-in function has already defined by some other and stored in a package
user-defined function is the function which we have defined as per our need'''
# Eg:
a = [1, 2, 3]
a.append(4)  # append() is a built-in function
print(a)


def factorial(n):  # user-defined function
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# 2. How can you pass arguments to a function in Python? Explain the difference between positional arguments and
# keyword arguments.

'''

In Python, you can pass arguments to a function in two ways: positional arguments and keyword arguments.

Positional arguments are the most common way to pass arguments to a function. They are specified in the order they 
are defined in the function definition. For example, the following function takes two positional arguments:'''


# Positional arguments
def add(a, b):
    return a + b


print(add(5, 6))  # 11
print(add(b=6, a=5))  # 11

'''Keyword arguments are a way to pass arguments to a function by name. This can be useful if you want to pass 
arguments in a different order than they are defined in the function definition, or if you want to pass a large 
number of arguments. For example, the following function takes two keyword arguments:'''


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


print(greet(name="Syed", age=24))
print(greet(age=24, name="Syed"))

# 3. What is the purpose of the return statement in a function? Can a function have multiple return
# statements? Explain with an example.


'''
The return statement in a function is used to exit the function and return a value. The value that is returned can be 
any Python object, such as a number, a string, a list, or a function.

A function can have multiple return statements, but only one of them will be executed. The first return statement 
that is executed will cause the function to exit and return the value that is associated with that statement.'''


def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)


print(factorial(0))
print(factorial(20))
'''As you can see, the first return statement is executed when n is 0, and the second return statement is executed 
when n is not 0.'''

# 4. What are lambda functions in Python? How are they different from regular functions? Provide an
# example where a lambda function can be useful.


'''
Lambda functions are anonymous functions in Python. They are defined using the lambda keyword, and they can only 
contain a single expression.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

# 5. How does the concept of "scope" apply to functions in Python? Explain the difference between local
# scope and global scope.

'''In Python, the scope of a variable refers to the part of the program where the variable is accessible. There are 
three different scopes in Python:

Local scope: The local scope of a variable is the part of the program where the variable is defined. Variables 
defined inside a function have a local scope. Global scope: The global scope of a variable is the entire program. 
Variables defined outside of any function have a global scope. Built-in scope: The built-in scope of a variable is 
the set of variables that are built into Python. These variables are always accessible, regardless of the scope of 
the program.'''

# 6. How can you use the "return" statement in a Python function to return multiple values?

'''
There are two ways to use the return statement in a Python function to return multiple values:
Using a tuple: You can return a tuple of values. A tuple is a sequence of values that can be any type, 
including int, strings, lists, and other tuples. For example, the following function returns the square and cube 
of a number:'''


def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube


result = square_and_cube(5)
print(result)

'''Using a list: You can also return a list of values. A list is a sequence of values that can be any type, 
including int, strings, tuples, and other list. For example, the following function returns the first and last 
name of a person:'''


def get_name(name):
    first_name, last_name = name.split(" ")
    return first_name, last_name


result = get_name("Syed Ameer")
print(result)  # ("Bard", "Singh")

# 7. What is the difference between the "pass by value" and "pass by reference" concepts when it comes to function
# arguments in Python?

'''Pass by value means that a copy of the value is passed to the function. Any changes made to the copy inside the 
function do not affect the original value. Pass by reference means that the address of the value is passed to the 
function. Any changes made to the value inside the function affect the original value.'''

# 8. Create a function that can intake integer or decimal value and do following operations:
# a. Logarithmic function (log x)
# b. Exponential function (exp(x))
# c. Power function with base 2 (2x)

import math


def cal(n):
    return math.log(n), math.exp(n), (n ** 2)


print(cal(10))


# 9. Create a function that takes a full name as an argument and returns first name and last name


def get_name(name):
    first_name, last_name = name.split(" ")
    return f'First Name is {first_name} and last name is {last_name}'


print(get_name('Syed Ameer'))
