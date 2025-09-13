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
# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()  # call the original function
#         print("After the function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

"""Using 'issubset' to check if all characters are within a set"""
# def check(stra,strb):
#     print(set(stra).issubset(strb))
# check("aabc","abcd")

"""Capitalize every other letter in a string"""
# def uppercase(str):
#     # str_list=list(str)
#     # for index, item in enumerate(str_list):
#     #     if index%2==0:
#     #         str_list[index]=item.upper()
#     #     else:
#     #         str_list[index]=item.lower()
#     # return "".join(str_list)

#     # return "".join(c.upper() if i%2==0 else c.lower() for i,c in enumerate(str))

#     """alternative solution"""
#     result=[]
#     capital=True
#     for i in str:
#         if capital:
#             result.append(i.upper())
#         else:
#             result.append(i.lower())
#         capital=not capital #flips t/f
#     return "".join(result)

# print(uppercase("bob")) #BoB