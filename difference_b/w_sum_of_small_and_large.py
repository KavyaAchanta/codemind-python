n=input()
k=n.split()
maxs=0
mins=0
for i in k:
    maxs+=ord(max(i))
    mins+=ord(min(i))
print(maxs-mins)