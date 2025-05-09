# LOOPS:-
# TYPES OF LOOP:- WHILE LOOP AND FOR LOOP
# While loop:- the condition is checked first , if it evaluates true then loop will executed ortherwise no
# Syntax:- while(condition)
i=1
while(i<6):
    print(i)
    i+=1

# Using while loop in lists
l=[1,"disha",2,4,"riya"]
i=0
while(i<len(l)):
  print(l[i])
  i+=1

# FOR LOOP:- used to iterate through a sequence like list,tuple or string.
l=[1,7,5,4]
for item  in l:
  print(item)

#   Range function:- the range[] function is used to generate a sequence of number.
# range(start,stop,step_size) 
# step size is usually not used in range.

# FOR LOOPS WITH LISTS:- 
l= [1,4,5,3,7]
for i in l:
    print(i)  

# FOR LOOPS WITH TUPLES:-
t = (6, 231, 75, 122)
for i in t:
    print(i)

# For Loop with Strings
s = "Hello"
for i in s:
    print(i)

# EXAMPLE OF RANGE FUNCTION:-
for i in range(0,7):
  print(i) #number will be printed from 0 to 6

# FOR LOOP WITH ELSE:- an optional else can be used with a for loop if the code to be executed when the loop exhausts
l=[1,5,6,8]
for item in l:
  print(item)
else:
    print("done")  #this is printed when loop exhausts

# Break statement:- used to come out of the loop encountered it instructs the program to exits out the loop
# for i in range(0,50):
#  print(i)
#  if i==3
#   break

# for i in range(50 ):
#   if (i==36):
#     continue #skip this iteration
#   print(i)

# Pass statement:- it is null statement it instructs to do nothing
for i in range(655):
  pass

i=0
while(i<45):
  print(i)
  i+=1

