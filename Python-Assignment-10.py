# 1. What is the role of try and exception block?
# 2. What is the syntax for a basic try-except block?
# 3. What happens if an exception occurs inside a try block and there is no matching
# except block?
# 4. What is the difference between using a bare except block and specifying a specific
# exception type?
# 5. Can you have nested try-except blocks in Python? If yes, then give an example.
# 6. Can we use multiple exception blocks, if yes then give an example.
# 7. Write the reason due to which following errors are raised:
# a. EOFError
# b. FloatingPointError
# c. IndexError
# d. MemoryError
# e. OverflowError
# f. TabError
# g. ValueError
# 8. Write code for the following given scenario and add try-exception block to it.
# a. Program to divide two numbers
# b. Program to convert a string to an integer
# c. Program to access an element in a list
# d. Program to handle a specific exception
# e. Program to handle any exception


# 1. What is the role of try and exception block?

"""Try and exception block used to handle the Interpreter error and to protect code from getting error because of one
input error
Example:
"""
try:
    a = int(input("Enter First Number for 1st task "))
    b = int(input("Enter Second Number for 1st task "))
    c = a / b
    print(c)  # This code can get error because of ZeroDivisionError
except ZeroDivisionError:
    print('b should not be 0')
d = a * b
print(d)  # But our point is this code is fine as 10*0=0, so it should run, Here Exception Handling comes,
# means we can handle interpreter error


# 2. What is the syntax for a basic try-except block?

'''try:
    # code that might cause an exception
except Exception as e:
    # code that runs if an exception is raised'''

# 3. What happens if an exception occurs inside a try block and there is no matching
# except block?

'''If an exception occurs inside a try block and there is no matching except block, the exception will be unhandled. 
This means that the program will crash and the user will see an error message.'''

try:
    x = 1 / 0
except Exception as e:
    print(e)

# 4. What is the difference between using a bare except block and specifying a specific
# exception type?

'''The main difference between using a bare except block and specifying a specific exception type is that the bare 
except block will catch any exception, while specifying a specific exception type will only catch that specific 
exception.'''

try:
    x = 1 / 0
except:
    print("An exception occurred")

try:
    x = 1 / 's'
except TypeError:
    print("TypeError")

# 5. Can you have nested try-except blocks in Python? If yes, then give an example.

'''
Yes, one can have nested try-except blocks in Python. This means that one can have a try-except block inside 
another try-except block.'''

try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Division by zero")
    except Exception as e:
        print(e)
except Exception as e:
    print(e)

# 6. Can we use multiple exception blocks, if yes then give an example.

'''
Yes, we can use multiple exception blocks.
'''
while True:
    try:
        x = float(input("Enter First Number for 6th task "))
        y = float(input("Enter Second Number for 6th task "))
        z = x / y
        print(z)
        break
    except ZeroDivisionError:
        print("B should not be a zero")
    except ValueError:
        print("Only numerical values are accepted")

# 7. Write the reason due to which following errors are raised:
# a. EOFError
# b. FloatingPointError
# c. IndexError
# d. MemoryError
# e. OverflowError
# f. TabError
# g. ValueError


'''
here are the reasons due to which the following errors are raised:

EOFError is raised when the end of a file is reached unexpectedly. This can happen if you try to read from a file 
that is empty or if you reach the end of the file while you are still trying to read from it. 

FloatingPointError is raised when a floating-point operation cannot be performed because the result is out of the 
range of representable floating-point numbers. This can happen if you try to divide by zero or if you try to perform 
an operation on numbers that are too large or too small.

IndexError is raised when an index is out of range for a sequence. This can happen if you try to access an element of 
a list or a string that does not exist. 

MemoryError is raised when the Python interpreter runs out of memory. This can happen if you are trying to allocate 
too much memory or if you are creating too many objects.

OverflowError is raised when a numeric operation results in a value that is too large to be 
represented. This can happen if you try to add two very large numbers or if you try to divide by a very small number. 

TabError is raised when a tab character is encountered in a string literal that is not being used to indent the 
string. 

ValueError is raised when a built-in function or operation is passed an argument that has the correct type 
but an invalid value. This can happen if you pass a string to an operation that expects an integer or if you pass a 
number to an operation that expects a string.'''

# 8. Write code for the following given scenario and add try-exception block to it.
# a. Program to divide two numbers
# b. Program to convert a string to an integer
# c. Program to access an element in a list
# d. Program to handle a specific exception
# e. Program to handle any exception

# a. Program to divide two numbers
while True:
    try:
        x = float(input("Enter First Number for 7th(a) task "))
        y = float(input("Enter Second Number for 7th(a) task "))
        z = x / y
        print(z)
        break
    except ZeroDivisionError:
        print("B should not be a zero")
    except ValueError:
        print("Only numerical values are accepted")

# b. Program to convert a string to an integer

try:
    string = 'Syed'
    num = int(string)
except ValueError:
    print("Could not convert string to integer")
else:
    print(num)

# c. Program to access an element in a list

lst = [2, 3, 5, 6, 4, 3]
try:
    element = lst[6]
except IndexError:
    print("Index out of range")
else:
    print(element)

# d. Program to handle a specific exception

try:
    x = float(input("Enter First Number for 7th(d) task "))
    y = float(input("Enter Second Number for 7th(d) task "))
    z = x / y
    print(z)
except ZeroDivisionError:
    print("B should not be a zero")
except TypeError:
    print('Type Error')

# e. Program to handle any exception

try:
    x = float(input("Enter First Number for 7th(e) task "))
    y = float(input("Enter Second Number for 7th(e) task "))
    z = x / y
    print(z)
except Exception as e:
    print(e)
