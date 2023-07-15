n=input()
k=n.lower()
l=[]
for i in k:
    if i not in l and i!=" ":
        l.append(i)
l.sort()
m=''.join(l)
print(m)
