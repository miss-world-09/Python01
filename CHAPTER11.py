# ADVANCE PYTHON:-

# WALRUS OPERATOR(:=)  :  ALLOWS TO ASSIGN VALUES TO VARIABLE AS PART OF AN EXPLRESSION.IT IS OFFICIALLY CALLED ASSIGNMENT OPERATOR.
# EX:-
if(n:=len([1,2,3,4,5]))>3:
    print(f"list is too long({n},elements expected <=3")


# TYPES OF DEFINITION OF PYTHON:-
# TYPE HINTS ARE ADDED USING COLON(:) SYNATX FOR VARIABLE AND -> SUNATX FOR THE FUNCTION RETURN TYPE.
# VARIABLE TYPE HINT. EX:-
age: int=55

# FUNCTION TYPE HINTS:-
def greeting(name:str)->str:
    return f"hello {name}"
print(greeting("maya"))

# ADVANCE TYPE HINTS:- SUCH AS:-LIST,TUPLE,DICT,UNION
from typing import List,Union,Tuple
n: int=5
name:str="riya"
def sum(a:int,b:int)->int:
    return a+b

# MATCH CASE:- IT IS SIMILAR TO SWITCH STATEMENT.
def http_status(status):
    match status:
        case 200:
            return"yes"
        case 402:
            return"no"
        case 500:
            return"internal server error"
        case _:
         return"unknown status"
print(http_status(57007))
print(http_status(200))
print(http_status(402))

# DICTIONARY MERGE AND UPDATE OPERATOR:- NEW OPERATORS | AND |= ALLOW FOR THE MERGING AND UPDATING DICTIONARIES.
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
merged=dict1|dict2
print(merged)

# EXCEPTION HANDLING:- THERE ARE MANY IN-BUILT EXCEPTIONS WHEN SOMETHING GOES WRONG. 
try:
    a=int(input("ENTER A NUMBER:"))
    print(a)
except Exception as e:
    print(e)
a=int(input("ENTER A NUMBER:"))
print("THANK YOU")

# RAISING EXCEPTION:-  WE CAN CUSTOM EXCEPTION USING RAISE KEYWORD.
a=int(input("ENTER FIRST NUMBER"))
b=int(input("ENTER SECOND NUMBER"))
if(b==0):
    raise ZeroDivisionError(" HEY IT IS NOT POSSIBLE")
else:
    print(f"the division a/b is{a/b}")


# TRY WITH ELSE CLAUSE:- SYNTAX:
# try:
    # somecode
# except:
    # somecode
# else:
    # code
    # else code is only executed if try code is successfully executed.

# TRY WITH FINALLY CLAUSE:- IT ALWAYS EXECUTE ONCE IN PROGRAM REGARDLESS OF ERROR.
# try:
    # code
# except:
    # code
# finally:
    # code

# IF __NAME__=='__MAIN__' IN PYHTON
# __NAME__ EVALUATES TO THE NAME OF THE MODULE WHERE THE PROGRAM IS RAN.

# def myfunc():
#     print("Hello World!")

# if__name__== "__main__" :
# print("Here is the code")
# myfunc()
# print(__name__)

# GLOBAL KEYWORD:- "GLOBAL" KEYWORD IS USED TO MODIFY THE VARIABLE OUTSIDE OF THE CURRENT SCOPE.
a=89
def fun():
    global a
    a=4
    print(a)

fun()
print(a)

# ENUMERATE FUNCTION:- THE ENUMERATE FUNCTION ADDS COUNTER TO AN ITERABLE AND RETURN IT.
l=[3,55,87,99]
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

# LIST COMPREHENSIONS:- 
mylist=[1,2,3,4,5]
squaredlist=[i*i for i in mylist]
print(squaredlist)

