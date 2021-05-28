# Take starting number and ending number from the user and print following series.

num = int(input("enter num:"))

for i in range(num,-1,-1):
    print(i,end=',')