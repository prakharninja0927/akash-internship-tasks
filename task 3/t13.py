#Take 3 numbers and find smallest number using nested IF….ELSE statement.

# input three integer numbers 
a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))

# conditions to find smallest 
if a<b:
    if a<c:
        smallest=a
    else:
        smallest=c
else:
    if b<c:
        smallest=b
    else:
        smallest=c

# print the largest number 
print("smallest  = ",smallest)
