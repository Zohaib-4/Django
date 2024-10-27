
a=["apple", "banana", "cherry", "apple", "mango", "cherry"]

# First Approach

a=["apple", "banana", "cherry", "apple", "mango", "cherry"]
unique=[]
i=0

for i in range(len(a)):
    
    if  a[i] not in unique:
        unique.append(a[i])
    i+=1

print(unique)

# Second Approach

a=["apple", "banana", "cherry", "apple", "mango", "cherry"]
unique=[]

for i in a:
    
    if  i not in unique:
        unique.append(i)

print(unique)

# Using Set Approach

a=["apple", "banana", "cherry", "apple", "mango", "cherry"]

print(list(set(a)))
