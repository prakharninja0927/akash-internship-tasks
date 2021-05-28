#Take 3 numbers and find greatest number using nested IF….ELSE statement.

# input three integer numbers 
a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))

# conditions to find largest 
if a>b:
    if a>c:
        largest=a
    else:
        largest=c
else:
    if b>c:
        largest=b
    else:
        largest=c

# print the largest number 
print("Greater  = ",largest)
