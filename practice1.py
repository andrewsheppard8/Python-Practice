# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: 
# Consider use range(#begin, #end) method

# def div(x):
#     z=x%7
#     a=x%5
#     if z == 0:
#         print('divisible by 7')
#         if a == 0:
#             print('divisible by 5')
#         else:
#             print("Not divisible by 5")
#     else:
#         print("Not divisible by 7")

# div(35)

# def check(x,y):
#     for x in range(x,y):
#         a=x%5
#         if a != 0:
#             b=x%7
#             if b == 0:
#                 print(x)

# check(2000,3200)

# def check(x,y):
#     result=[]
#     for num in range (x,y+1):
#         if num%7==0 and num%5 != 0:
#             result.append(str(num))
#     print(",".join(result))
# check(2000,3200)

# def join(lst):
#     x=" ".join(lst)
#     print(x)

# join(["a","b","c"])

# def replace(str):
#     text=str.replace("a","A")
#     print(text)
# replace("aabb")

# def split(str):
#     x=str[4:]
#     print(x)
# split("Thailand")

print("Practicing changes in VSCode")