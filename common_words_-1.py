s1=input()
s2=input()
m=s1.lower()
n=s2.lower()
h=m.split()
k=n.split()
c=0
if len(s1)>len(s2):
    for i in h:
        if i in k:
            c+=1
else:
    for i in k:
        if i in h:
            c+=1
print(c)
