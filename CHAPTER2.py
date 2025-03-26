# STRINGS:-
# String is a data type, string is the sequence of character enclosed in quotes
a='disha'
b="disha"
c='''disha'''

# string slicing
# string start from 0 to -1. Syntax of slice string:- 
# sl=name[ind_start:ind_end]. For example sl[0:3]returns dis->char from 0 to 3
name="Disha"
nameshort=name[0:3]
print(nameshort)
character1=name[1]
print(character1)

# SLICING WITH SKIP VALUE:- we can skip value while slicing
word="beautiful"
print(word[1:6:2]) 

name="disha"
print(len(name))
print(name.endswith("a"))
print(name.startswith("d"))
print(name.capitalize())

# Escape sequence with character:-
# \n->new line, \t->tab, \->single quote, \\->double backslash

