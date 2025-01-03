# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# #First-Class Objects
#
# def calculate(cal_func, n1, n2):
#     return cal_func(n1, n2)
#
# result = calculate(multiply, 2, 3)
# #print(result)
#
# # Nested Functions
#
# def outer_function():
#     print("I'm outer")
#
#     def inner_function():
#         print("I'm inner")

#     inner_function()
#
# outer_function()

# Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def inner_function():
#         print("I'm inner")
#
#     return inner_function
#
# inner_function = outer_function()
# inner_function()

# Python Decorator
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("How are you?")

decorated = delay_decorator(say_hello)
decorated()

