# find factorial of given number

num = int(input("enter number:"))
fact = 1
for i in range(num,1,-1):
    fact = fact * i
print("factorial of {} is {}".format(num,fact))