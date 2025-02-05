"""n = int(input("enter the num:"))
for i in range(0,n):
    n+=i
print(n)"""
"""
list -indexed values
set-unordered ,no repetation
tuple-immutable
"""
"""
functions
syntax
def funcname():
  state
return value
function only return one value in pyhton


RECURCIVE FUNCTION

def fact(n):
 if n==1 or n==0;
 return 1
 else:
 return n*fact(n-1)


 LAMBDA FUNC
 add=lambda a,b:a+b

"""
"""a=int(input("enter the num of  elements to be rotated"))
li=[1,2,3,4,5,6]
lis=[]
list=[]
lis.append(li[:a])
list.append(li[a:])
list.append(lis)
print(list)"""
 

for i in range (0,5,1):
    print("\n")
    for j in range(0,(5-i)):
        print("  ",end=" ")
    for k in range (0,(2*i-1)):
        print("*",end=" ")
for i in range (5,0,-1):
    print("\n")
    for j in range(0,(5-i)):
        print("  ",end=" ")
    for k in range (0,(2*i-1)):
        print("*",end="  ")