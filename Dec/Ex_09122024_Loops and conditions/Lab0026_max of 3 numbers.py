# programme to find the max out of three numbers

# logic building
# user input -num1, num2 and num3 ->int
# o/p->int ot string with max number

# Logic -> else if condition

# syntax
# if condition 1:
#     print("do 1")
# else if condition 2:
#     print("do 2")
# else if condition 3:
#     print("do 3")
# else
#     print("do for else")


num1= int(input('enter num1\n'))
num2= int(input('enter num2\n'))
num3= int(input('enter num3\n'))


if num1>num2 and num1>num3:
    print("max is",num1)
elif num2>num1 and num2>num3:
    print("max is", num2)
else:
    print("max is", num3)


