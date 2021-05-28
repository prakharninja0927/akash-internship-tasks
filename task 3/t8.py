# find smallest number in given two numbers

num1 = int(input("enter num 1 :"))
num2 = int(input("enter num 2 :"))

if num1>num2:
    print("{} is smaller than {}".format(num2,num1))
elif num2>num1:
    print("{} is smaller than {}".format(num1,num2))
else:
    print("both numbers are equal")