def shuffle(l1, l2):
    result = []
    for i in range(max(len(l1), len(l2))):
        if i < len(l1):
            result.append(l1[i])
        if i < len(l2):
            result.append(l2[i])
    return result
l=int(input("enter the number of elements in l1"))

l1=list(map(int,input("enter the list seperated by space=").strip().split()))

L=int(input("enter the number of elements in l2"))

l2=list(map(int,input("enter the list seperated by space=").strip().split()))

if  l<0 or L<0 :
    
    print("invalid input")
    
print(shuffle(l1,l2))
