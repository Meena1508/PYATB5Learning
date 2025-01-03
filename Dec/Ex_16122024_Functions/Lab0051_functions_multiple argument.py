# print unlimited number of arguments


def print_mul_arguments(*args):
    for i in args:
        print(i)

print_mul_arguments("Meena")
print_mul_arguments("Meena","ayush","shreya","vihan")
print_mul_arguments("Meena","ayush","shreya","vihan",10,"ammu")