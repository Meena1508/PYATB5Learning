# create a program to sum 3 numbers by user input
# if user doesnt enter the number , use default 100, 200,300


num1=int(input("enter num1\n"))
num2=int(input("enter num2\n"))
num3=int(input("enter num3\n"))

def sum_three(n1=100,n2=200,n3=300):
    return n1+n2+n3

Result=sum_three(num1,num2,num3)

print("Result=",Result)

Result2=sum_three()

print("Result2",Result2)




