# Python-Assignment-9

# 1. What is a lambda function in Python, and how does it differ from a regular function?
# 2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use
# them?
# 3. How are lambda functions typically used in Python? Provide an example use case.
# 4. What are the advantages and limitations of lambda functions compared to regular functions in
# Python?
# 5. Are lambda functions in Python able to access variables defined outside of their own scope?
# Explain with an example.
# 6. Write a lambda function to calculate the square of a given number.
# 7. Create a lambda function to find the maximum value in a list of integers.
# 8. Implement a lambda function to filter out all the even numbers from a list of integers.
# 9. Write a lambda function to sort a list of strings in ascending order based on the length of each
# string.
# 10. Create a lambda function that takes two lists as input and returns a new list containing the
# common elements between the two lists.
# 11. Write a recursive function to calculate the factorial of a given positive integer.
# 12. Implement a recursive function to compute the nth Fibonacci number.
# 13. Create a recursive function to find the sum of all the elements in a given list.
# 14. Write a recursive function to determine whether a given string is a palindrome.
# 15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers


# 1. What is a lambda function in Python, and how does it differ from a regular function?
"""A lambda function in Python is a small, anonymous function. It is defined using the lambda keyword, and it can
only contain a single expression.

Lambda function is an Anonymous and Regular function Has a name
Lambda function has single expression and regular function has Multiple expressions
Lambda function is a local and Regular function is local and global
Lambda function is often used as arguments to other functions and Regular function is can be used as standalone functions
"""

# 2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use
# them?

'''

Yes, a lambda function in Python can have multiple arguments. The arguments are defined as a comma-separated list 
after the lambda keyword. The body of the lambda function is a single expression that uses the arguments.'''

add_and_multiply = lambda x, y: x + y * y
result = add_and_multiply(2, 3)

print(result)

# 3. How are lambda functions typically used in Python? Provide an example use case.


'''Lambda functions are typically used in Python with higher-order functions, which take one or more functions as 
arguments or return one or more functions. Some examples of higher-order functions in Python include map(), filter(), 
reduce(), and sorted().

Calculating the sum of the even numbers in a list:
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

sum_of_even_numbers = sum(even_numbers)

print(sum_of_even_numbers)

# 4. What are the advantages and limitations of lambda functions compared to regular functions in
# Python?

'''
Here are some of the advantages of lambda functions:

They are concise: Lambda functions can be defined in a single line of code, making them very easy to read and 
understand. 
They are anonymous: Lambda functions do not have a name, which can make them easier to pass around as 
arguments to other functions. 
They are efficient: Lambda functions are often more efficient than regular functions, 
as they do not need to create a new stack frame when they are called.

Here are some of the limitations of lambda functions:

They can only contain a single expression: This means that lambda functions cannot be used to define functions with multiple statements or complex control flow.
They cannot be used as class methods: Lambda functions cannot be used as class methods, as they do not have a name.
They can be difficult to debug: Lambda functions can be difficult to debug, as they are often embedded within other code.
'''

# 5. Are lambda functions in Python able to access variables defined outside of their own scope?
# Explain with an example.

'''
Yes, lambda functions in Python are able to access variables defined outside of their own scope. This is because 
lambda functions are closures. A closure is a function that remembers the values of variables that were in scope when 
the function was defined.'''

lst = [1, 2, 3, 4]

lst2 = (lambda i: [i + i for i in lst])

print(lst2(lst))

# 6. Write a lambda function to calculate the square of a given number.

square_of_lst = lambda x: x ** 2

print(square_of_lst(20))

# 7. Create a lambda function to find the maximum value in a list of integers.

lst3 = [1, 2, 5, 8, 641, 4, 48, -5, 45, -10]

max_value = lambda i: max(i)

print(max_value(lst3))

# 8. Implement a lambda function to filter out all the even numbers from a list of integers.

lst4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 3, 4, 5, 678, 2, 4]
even_num = list(filter(lambda x: x % 2 == 0, lst4))

print(even_num)

# 9. Write a lambda function to sort a list of strings in ascending order based on the length of each
# string.

strings = ["hello", "world", "this", "is", "a", "list"]

sorted_strings = sorted(strings, key=lambda x: len(x))

print(sorted_strings)

# 10. Create a lambda function that takes two lists as input and returns a new list containing the
# common elements between the two lists.

x = [4, 5, 6, 7, 8, 9, 24, 5]
y = [1, 2, 3, 4, 5, 6, 7, 6, 8, 5]

common_elements = list(filter(lambda x: x in y, x))

print(common_elements)


# 11. Write a recursive function to calculate the factorial of a given positive integer.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))


# 12. Implement a recursive function to compute the nth Fibonacci number.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4))


# 13. Create a recursive function to find the sum of all the elements in a given list.

def sum_of_list(a):
    return sum(a)


lst5 = [1, 3, 4, 5, 6, 4, 2]
print(sum_of_list(lst5))


# 14. Write a recursive function to determine whether a given string is a palindrome.

def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])


print(is_palindrome('racecar'))


# # 15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(15, 12))
