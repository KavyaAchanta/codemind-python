s1=input()
s2=input()
h=s1.lower()
k=s2.lower()
l="abcdefghijklmnopqrstuvwxyz"
s=1
for i in l:
        if i in h and i in k:
            print(i,end="")
            s=0
if s==1:
     print(-1)