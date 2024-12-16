# problem to find the max of 2 numbers

# Logic building formula

# 1.User inout ->2 integers
# o/p -> int value which is maximum of both the numbers it will return
# 31.4 or 45.35 -> float

num1= float(input("enter the num1\n"))
num2= float(input("enter the num2\n"))

if num1>=num2:
    print("max number ", num1)
else:
    print("max number ", num2)

# edge cases
# num1 =num2
#number entered as a string
# negative values 