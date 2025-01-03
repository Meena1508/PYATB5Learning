# 1.They cannot return anything

def say_hello():
 print("hello")

say_hello()

# 2. no return type with argument/parameter

def greet_by_name(name):
    print("Hello,",name)

greet_by_name("Meena")

# 3. no return type with defualt argument

def say_hello_default_arg(name="Meena"):
    print("Hello,",name.upper())

say_hello_default_arg()
say_hello_default_arg("Pramod")


def multiple_args(name1="meena",name2="Ayush"):
    print("Multi->", name1, name2)

multiple_args()
multiple_args(name1="akki")
multiple_args(name1="anu",name2="james")
multiple_args(name2="prafs")
multiple_args("Lakshmi")


# 4.argument + return type function

def sum_of_two(a,b):
    return a +b

result=sum_of_two(4,5)
print(result)



def sum_of_two_with_default(a=20,b=21):
    return a +b

result=sum_of_two_with_default(12,5)
print(result)

result=sum_of_two_with_default()
print(result)






