# INHERITANCE IN OOPS:- INHERITANCE IS A WAY OF CREATING NEW CLASS FROM AN EXISTING CLASS.
# SYNTAX:- CLASS EMPLOYEE:
#            CODE
#          CLASS PROGRAMMER(EMPLOYEE):(DERIVED OR CHILD CLASS)
#            CODE

# TYPES OF INHERITANCE:-
# 1. SINGLE INHERITANCE: OCCURS WHEN CHILD CLASS INHERITS FROM SINGLE PARENT CLASS
# 2. MULTIPLE INHERITANCE: OCCURS WHEN CHILD CLASS INHERITS FROM MORE THAN ONE PARENT CLASS.
class employee:
    company="google"
    name="disha"
    def show(self):
        print(f"the name of employee is{self.name} and the company is {self.company}")

class Coder:
        language="python"
        def printlanguage(self):
            print(f"out of all the languages here is your language{self.language}")
    
class programmer(employee, Coder):
        company="microsoft"
        def showlanguage(self):
            print(f"the name is {self.company}and he is good with{self.language} and the name of programmer is {self.name}")

a=employee()
b=programmer()
b.show()
b.printlanguage()
b.showlanguage()

# MULTILEVEL INHERITANCE:- WHEN A CHILD CLASS BECOME THE PARENT OF ANOTHER CHILD CLASS.
class employee:
     a=1
class programmer(employee):
     b=2
class manager(programmer):
     c=3
o=employee()
print(o.a)
o=programmer()
print(o.a,o.b)
o=manager()
print(o.a,o.b,o.c)

# SUPER() METHOD:- USED TO ACCESS THE METHODS OF SUPER CLASS IN THE DERIVED CLASS.
class employee:
     def __init__(self):
          print("the constructor of employee")
     a=1
class programmer(employee):
     def __init__(self):
          print("constructor of programmer")
     b=2
class manager(programmer):
     def __init__(self):
          super().__init__()
          print("constructor of manager")
     c=3
# o = Employee()
# print(o.a) # Prints the a attribute 

# o = Programmer()
# print(o.a, o.b)

o=manager()
print(o.a,o.b,o.c)
# BY USING SUPER() METHOD WE CAN CALL ALL THE THREE CONSTRUCTOR TOGETHER

# CLASS METHOD:- METHOD WHICH IS BOUND TO THE CLASS AND NOT TO THE OBJECT OF CLASS.
class employee:
     a=1
     @classmethod
     def show(cls):
          print(f"the class attribute of a is {cls.a}")
e=employee()
e.a=45
e.show()

# PROPERTY DECORATORS:- 
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "riya"
print(e.fname, e.lname)

e.show()

# OPERATOR OVERLOADING:- 

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)

