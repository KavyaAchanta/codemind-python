s1=input()
s2=input()
h=s1.lower()
k=s2.lower()
l="abcdefghijklmnopqrstuvwxyz"
for i in l:
        if i in h and i not in k:
            print(i,end="")
        if i in k and i not in h:
            print(i,end="")
    
    
