# CLASSES AND OBJECTS:-
# CLASS:- A CLASS IS A BLUEPRINT FOR CREATING OBJECTS
# OBJECT:- AN OBJECT IS INSTANTIATION OF A CLASS. WHEN CLASS IS DEFINED, A TEMPLATE IS DEFINED 
# CLASS ATTRIBUTE:- AN ATTRIBUTE THAT BELONGS TO A CLASS RATHER THAN A PARTICULAR OBJECT
# INSTANCE ATTRIBUTE:- ATTRIBUTE THAT BELONGS TO INSTANCE(OBJECT). INSTANCE ATTRIBUTE TAKE PREFERENCE OVER CLASS ATTRIBUTE
class employee:
    language="c++" #this is class attribute
    salary="1200000"
riya=employee()
riya.name="riya"  #this is instance attribute
print(riya.language, riya.salary)
rahul=employee()
rahul.name="rahul"
print(rahul.salary,rahul.name,rahul.language)

# INSTANCE VS CLASS ATTRIBUTE
class employee:
    language="c+" #class attribute 
    salary="1200000"
tiya=employee()
tiya.language="js" #instance attribute
print(tiya.language,tiya.salary)

# SELF PARAMETER:- IT IS AUTOMATICALLY PASSED WITH A FUNCTION CALL FROM AN OBJECT.

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    
    def greet(self):
        print("Good morning")


jiya = Employee()
# harry.language = "JavaScript" # This is an instance attribute
jiya.greet()
jiya.getInfo() 
# Employee.getInfo(harry)

# STATIC METHOD:- FUNCTION THAT DOES NOT CONTAIN SELF PARAMETER. EX:-
class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


jiya = Employee()
# harry.language = "JavaScript" # This is an instance attribute
jiya.greet()
jiya.getInfo() 

# CONSTRUCTORS:- _INIT_() #DUNDER METHOD WHICH IS AUTOMATICALLY CALLED
class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee("Harry", 1300000, "JavaScript") 
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

 