time=int(input("entre the number of slots:"))

entry=[int(input("entre the number of guests entering at a time():".format(i+1))) for i in range(time)]

exit=[int(input("entre the number of guests exiting at a time slot():".format(i+1))) for i in range(time)]

count=0
guests=[]
for i in range(len(entry)):
    count = count + entry[i] - exit[i]
    guests.append(count)

print("the maximum number of guests presnt at a time:",max(guests))
