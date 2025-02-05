li= [2,4,1,3,5]
n=len(li)
count=0
for i in range(n):
    for j in range(i+1,n):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
            count=count+1
print(li,count)