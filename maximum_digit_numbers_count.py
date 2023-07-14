n=int(input())
l=list(map(int,input().split()))
max=0
for i in l:
    m=len(str(abs(i)))
    if m>max:
        max=m
for i in l:
    m=len(str(abs(i)))
    if m==max:
        print(i,end=" ")
    
    