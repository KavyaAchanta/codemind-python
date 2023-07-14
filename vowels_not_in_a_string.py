n=input()
l=n.lower()
k="aeiou"
m=[]
for i in k:
    if i not in l:
       m.append(i)
if len(m)>0:
    print(*m)
else:
    print(0)
    