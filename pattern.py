print("pattern printing-inverted right angle triangle")
for i in range (5,0,-1):
    print("\n")
    for k in range(0,5-i):
        print(" ",end=" ")
    for j in range(1,i):
        print("*",end=" ")

print("\npattern printing-hollow square")
for i in range(0,4):
    print("\n")
    for j in range(0,4):
        if ((i==1 and (j==1 or j==2 )) or (i==2 and (j==2 or j==1))):
            print(" ",end="   ")
        else:
            print("*",end="   ")


print("\nunique elements in list")
li=[1,1,2,2,3,3,4,5,5,6,6]
for i in li:
    counts= li.count(i)
    if counts==1:
        print("\n",i)
    