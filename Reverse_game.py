def reverse(n):
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    return s
        
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    m=reverse(i)
    k.append(m)
print(*k)
    