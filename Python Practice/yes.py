
tuple1 =(1,2,2,2,2,2,3,3,3,3,4,4,4,4)
mylist=[tuple1[0]]

for x in tuple1:
        if x not in mylist:
            mylist.append(x)

mydictionary=[]
for x in mylist:
      mydictionary[x]=tuple1.count(x)

print(mydictionary)