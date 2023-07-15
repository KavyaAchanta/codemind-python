n=input()
k=list(n)
l=[]
for i in k:
    if i not in l:
        l.append(i)
if len(l)==len(k):
    print("True")
else:
    print("False")