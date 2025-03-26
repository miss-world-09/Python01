# FILES
f=open("file.txt","r")
data=f.read()
print(data)
f.close

st="hey im here"
f=open("file.txt","w")
f.write(st)
f.close

# TYPES OF FILE:-
# 1. TEXT FILES(.txt,.c,etc)
# 2. BINARY FILES(.jpg,.dat,etc)

f=open("file.txt")
lines=f.readlines()
print(lines,type(lines))
f.close

line=f.readline()
while(line !=""):
    print(line)
    line=f.readline()
f.close()

# MODES OF FILE OPENING:
# r->open for reading
# w-> open for writing
# a->open for appending
# +->open for updating
# 'rb'->read in binary mode
# 'rt'->open for read in text mode

# WITH STATEMENT:- WAY TO OPEN AND CLOSE FILE AUTOMATICALLY
with open("file.txt") as f:
 print(f.read())