#Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement 

num = int(input("enter number"))

if num!=0:
    if num<0:
        print("{} is -ve",format(num))
    else:
        print("{} is +ve".format(num))
else:
    print("number is zero")