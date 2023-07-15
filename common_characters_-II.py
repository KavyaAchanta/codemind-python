s1=input()
s2=input()
h=s1.lower()
k=s2.lower()
l="abcdefghijklmnopqrstuvwxyz"
m=[]
for i in l:
    if i in h and i in k:
        m.append(i)
print(len(m))