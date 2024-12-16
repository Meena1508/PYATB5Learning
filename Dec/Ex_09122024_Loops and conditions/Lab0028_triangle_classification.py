# write a program that calssifies a triangle based on its side legth
# given 3 input
# equilateral ->all sides are equal
# isosceles-> two sides are equal
# scalene ->no sides are equal


# int -> s1, s2, s3
#o/p

s1=int(input("enter the length of s1\n"))
s2=int(input("enter the length of s2\n"))
s3=int(input("enter the length of s3\n"))

if s1==s2 and s2==s3:
    print("It is a equilateral triangle")
elif s1==s2:
    print("It is a isosceles triangle")
else:
    print("It is a scalene triangle")

# edge cases not handeled




