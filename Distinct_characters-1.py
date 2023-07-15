n=input()
k=n.lower()
l=list(k)
c=[]
for i in l:
    if l.count(i)==1 and i!=" ":
        c.append(i)
c.sort()
m=''.join(c)
print(m)
        