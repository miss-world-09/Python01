# LISTS:- Containers to store the set of values of any data type. For ex:- 
friends=["apple","banana",7, False,True]
print(friends[0])
friends[0]="Grapes"    #unlike strings are mutable
print(friends[0])

# List indexing:- A list can be index just like string.
friends=["apple","banana",7, False,True,"mango"]
print(friends[1:4])

# LIST METHODS:-
# 1. sort():- sort the list
# 2. reverse():-reverse the list
# 3. appends(8):- add 8 to the end of the list
# 4. insert(3,8):- this will add 8 at index 3
# 5. pop(2):- it will delete at index 2 and return its Value.
# 6. remove(21):- it will remove 21 from the list
l1=[1,34,62,11,3,20,30]
l1.sort()
print(l1) 
l1.reverse()
print(l1)
l1.append(8)
print(l1)
l1.insert(4,77)
print(l1)
l1.remove(3)
print(l1)

# TUPLE:- A tuple is an immutable data type
# ex:- 
a=() #empty tuple
a=(1,) #tuple with 1 element need comma
a=(1,5,6,7) #tuple with more than one element
# TUPLE METHODS:- a=(1,7,2)
# a.count(1):- it will return number of time 1 occur in a
# a.index(1):- will return the index of first occurence of 1 in a.
