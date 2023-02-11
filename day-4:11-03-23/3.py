l=list(map(int,input("entre the list=").strip().split()))
s=sorted (l)
L= []
for i in l:
    L.append (s.index (i))
print (L)
