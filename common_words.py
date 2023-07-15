s1=input()
s2=input()
h=s1.lower()
k=s2.lower()
m=h.split()
n=k.split()
l=[]
if len(s1)>len(s2):
    for i in m:
        if i in n:
            l.append(i)
    print(*l)
else:
    for i in n:
        if i in m:
            l.append(i)
    print(*l)

    
            