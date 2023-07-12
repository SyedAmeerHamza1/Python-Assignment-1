# 1. What is the role of the 'else' block in a try-except statement? Provide an example
# scenario where it would be useful.
# 2. Can a try-except block be nested inside another try-except block? Explain with an
# example.
# 3. How can you create a custom exception class in Python? Provide an example that
# demonstrates its usage.
# 4. What are some common exceptions that are built-in to Python?
# 5. What is logging in Python, and why is it important in software development?
# 6. Explain the purpose of log levels in Python logging and provide examples of when
# each log level would be appropriate.
# 7. What are log formatters in Python logging, and how can you customise the log
# message format using formatters?
# 8. How can you set up logging to capture log messages from multiple modules or
# classes in a Python application?
# 9. What is the difference between the logging and print statements in Python? When
# should you use logging over print statements in a real-world application?
# 10. Write a Python program that logs a message to a file named "app.log" with the
# following requirements:
# ● The log message should be "Hello, World!"
# ● The log level should be set to "INFO."
# ● The log file should append new log entries without overwriting previous ones.
# 11. Create a Python program that logs an error message to the console and a file named
# "errors.log" if an exception occurs during the program's execution. The error
# message should include the exception type and a timestamp


# 1. What is the role of the 'else' block in a try-except statement? Provide an example
# scenario where it would be useful.

"""
The role of else block is to run the code when there is no exception
"""

try:
    a = float(input("first number"))
    b = float(input("Second number"))
    c = a / b
    print(c)
except Exception as e:
    print(e)
else:  # This will run when the previous code run
    print("Python rocks")

# 2. Can a try-except block be nested inside another try-except block? Explain with an
# example.

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


# 3. How can you create a custom exception class in Python? Provide an example that
# demonstrates its usage.

class wrong_age(Exception):
    pass


age = 18
try:
    input_age = int(input("Enter your age: "))
    if input_age < age:
        raise wrong_age
    else:
        print("You can work")
except wrong_age:
    print("You are not allowed to work")

# 4. What are some common exceptions that are built-in to Python?

'''
Some of the most common types of exceptions are:
ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.

TypeError: Raised when an operation or function is applied to an object of inappropriate type.

ValueError: Raised when a built-in operation or function receives an argument that has the right type but an 
inappropriate value.

IndexError: Raised when a sequence subscript is out of range.

KeyError: Raised when a dictionary key is not found.

FileNotFoundError: Raised when a file or directory is requested but does’t exist.

IOError: Raised when an I/O operation (such as a print statement, the built-in open() function or a method of a file 
object) fails for an I/O-related reason.

ImportError: Raised when an import statement fails to find the module definition or when a from ... import fails to 
find a name that is to be imported.

MemoryError: Raised when an operation runs out of memory.

OverflowError: Raised when the result of an arithmetic operation is too large to be expressed by the normal number 
format.

AttributeError: Raised when an attribute reference or assignment fails.

SyntaxError: Raised when the parser encounters a syntax error.

IndentationError: Raised when there is incorrect indentation.

NameError: Raised when a local or global name is not found.
'''

# 5. What is logging in Python, and why is it important in software development?

'''logging in python is use to store a result of a code and store in a particulate file, it is important in software 
development to store the data, work on debugs, get the logging file from a client logging is crucial.'''

# 6. Explain the purpose of log levels in Python logging and provide examples of when
# each log level would be appropriate.

'''There are 5 log levels in python they are: 
debug, info, warning, error, critical. 

It works on level base, if we select debug level we can utilize all other levels, if we select info level we can 
utilize all levels except debug, if we select warning level we can utilize warning, error and critical but not debug and 
info, if we select error we can utilize error and critical and if we select critical we can only utilize critical.

DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or may happen in the future (e.g. ‘disk space low’). The 
software is still working as expected.
ERROR: More serious problem that prevented the software from performing a function.
CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.
'''

# 6. Explain the purpose of log levels in Python logging and provide examples of when
# each log level would be appropriate.

'''here is an explanation of the purpose of log levels in Python logging and some examples of when each log level 
would be appropriate:

DEBUG level is used to log messages that are useful for debugging your code. This level should be used sparingly, 
as it can generate a lot of output.

INFO level is used to log messages that are informative but not necessarily important. This level is a good choice 
for logging the progress of your program or the values of variables.

WARNING level is used to log messages that indicate a potential problem. This level is a good choice for logging 
errors that do not prevent your program from continuing to run.

ERROR level is used to log messages that indicate a serious error that has caused your program to stop running. This 
level is a good choice for logging errors that you need to investigate and fix.

CRITICAL level is used to log messages that indicate a fatal error that has caused your program to crash. This level 
is a good choice for logging errors that you need to fix immediately.


You would use the DEBUG level to log the values of variables as you are debugging your code.
You would use the INFO level to log the progress of your program as it is running.
You would use the WARNING level to log errors that do not prevent your program from continuing to run, such as a file 
not being found.
You would use the ERROR level to log errors that cause your program to stop running, such as a division by zero.
You would use the CRITICAL level to log fatal errors that cause your program to crash, such as a memory error.

'''

# 8. How can you set up logging to capture log messages from multiple modules or
# classes in a Python application?

import logging

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(levelname)s %(asctime)s %(name)s %(message)s')

try:
    logging.info("i am trying to read a file ")
    with open('Assignment_11.pdf', 'r'):
        logging.info("successfully it has read the file ")
except Exception as e:
    logging.critical("This file can create a situation for us")
    logging.error(e)
    logging.exception(e)

# 9. What is the difference between the logging and print statements in Python? When
# should you use logging over print statements in a real-world application?

'''
Print statements are used to print messages to the console. They are a simple way to output information, but they are not very flexible. Print statements are also not very well-suited for logging, as they cannot be easily filtered or turned off.

Logging is a more sophisticated way to output messages. It allows you to control the level of detail of the messages, and it allows you to filter and turn off messages. Logging is also more portable than print statements, as it can be used in different environments.

Here are some reasons why you should use logging over print statements in a real-world application:

Logging is more flexible: You can control the level of detail of the messages, and you can filter and turn off messages.
Logging is more portable: Logging can be used in different environments.
Logging is more efficient: Logging messages are only printed when they are needed, which can improve the performance of your program.
Logging is more useful for debugging: Logging messages can be used to track down errors in your program.
'''

# 10. Write a Python program that logs a message to a file named "app.log" with the
# following requirements:
# ● The log message should be "Hello, World!"
# ● The log level should be set to "INFO."
# ● The log file should append new log entries without overwriting previous ones.

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Hello, World')

# 11. Create a Python program that logs an error message to the console and a file named
# "errors.log" if an exception occurs during the program's execution. The error
# message should include the exception type and a timestamp

logging.basicConfig(filename="errors.log", level=logging.ERROR, format='%(levelname)s %(asctime)s %(message)s $(name)s')

try:
    a = 10
    b = 'Python'
    c = a + b
except Exception as e:
    logging.error(e)
