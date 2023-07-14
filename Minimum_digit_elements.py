n=int(input())
l=list(map(int,input().split()))
max=999
for i in l:
    m=len(str(i))
    if m<max:
        max=m
c=0
for i in l:
    m=len(str(i))
    if m==max:
        c+=1
print(c)
    