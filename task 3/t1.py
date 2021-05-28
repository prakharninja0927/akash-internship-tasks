# find average of given numbers

sum=0
for i in range(0,5):
    num = int(input("enter number {} :".format(i+1)))
    sum = sum + num
print("average of numbers :{}".format(sum/5))