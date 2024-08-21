
# First Approach

a= 54371

temp=int(a%10)
a=a/10

while a!=0:

    temp=int(temp*10)
    temp=int(temp+(a%10))
    a=int(a/10)
    
print(temp)

# Second Approach

num = 123
reverse =0

while num!=0:
    digit=num%10
    reverse = reverse*10 + digit
    num//=10

print(reverse)

# Slicing Approach

x= "Pakistan"
print(x[::-1])



