a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
m=[]
n=[]
c=0
for i in l1:
    if i not in m:
        m.append(i)
        
for i in l2:
    if i not in n:
        n.append(i)
for i in m:
    if i in n:
        print(i,end=" ")
