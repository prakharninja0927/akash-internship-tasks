#Take a number check if a number is less than 100 or not. 
# If it is less than 100 then check if it is odd or even.

num = int(input("enter number :"))
if num<100:
    if num%2==0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
else:
    print("{} is grater than 100".format(num))