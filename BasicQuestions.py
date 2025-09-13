# my_list = ['apple', 'banana', 'cherry']
# for index, value in enumerate(my_list):
#     print(f"Index: {index}, Value: {value}")

"""Write a function to hide a credit card number. Takes credit card number and replaces all digits w * except the last four. so 1122334444 would be ******4444"""
# def functiona(parameter):
#     s=str(parameter)
#     return "*" * (len(s)-4) + s[-4:]
# print(functiona(11223355554444))

"""calling functions as objects"""
# def greet():
#     print("Hello")

# def run(func):
#     func()

# run(greet)

"""calling functions in functions"""
# def outer():
#     def inner():
#         print("Hello from inner")
#     return inner
# f=outer()
# f()

"""Working with basic decorators"""
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()  # call the original function
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()