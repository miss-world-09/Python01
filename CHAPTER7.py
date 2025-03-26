# FUNCTION:-  a function is a group of statements performing a specific task.
# When a program gets bigger in size and complexity grows, it gets difficult for a program to keep track on which which piece of code is doing what
# A function can be reused by a programmer. SYNTAX:-
# def func1():
#     print("Hello")
# Function call:- Whenever we want to call a function, we put the name of the function followed by parenthesis,
# func1() #syntax
# Function Definition
# def avg():
#     a=int(input("Enter your number:"))
#     b=int(input("Enter your number:"))
#     c=int(input("Enter your number:"))

#     average=(a+b+c)/3
#     print(average)

# avg() #Function call
# print("thank you")
# avg()
# print("thank you")
# avg()
# print("thank you")

# TYPES OF FUNCTION:- 1. BUILD-IN FUNCTION: ALREADY PRESENT IN PYTHON
# 2. USER DEFINED FUNCTION:- DEFINED BY USER
def goodday(name,ending):
    print("Good afternoon,"+name)
    print(ending)
goodday("Disha","thank you")

# Default parameter value:- we have value as default argument in a function
def greet(name="stranger"):
    # function body
    greet() #name will be "stranger" in function body(default)
    greet("disha") #name will be disha in function body(passed)
#ex:-
def goodday(name, ending="thank you"):
    print(f"good day ,{name}")
    print(ending)
goodday("disha","thanks")
goodday("riya")

# RECURSION:- recursion is a function which call itself. It is used mathematical formula as function.
# EX:- factorial(n)=n X factorial(n-1)
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n = int(input("Enter a number:"))
print(f"The factorial of this no is {factorial(n)}")