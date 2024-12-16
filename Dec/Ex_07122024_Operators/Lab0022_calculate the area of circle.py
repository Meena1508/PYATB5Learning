# write a python programme to calculate the area of a circle
# formula = pi *r ^2(take pi as 3.14)


# ||step 1||
# Figure out inputs and outputs
# input = r >data type =float
# pi=3.14
# power ->pow or **-> any
# o/p -> float -area, print area

# ||step 2||
# rough logic ->area =3.14*pow(r,2)

# ||step 3||
radius = float(input("Enter the radius of the circle\n"))
print(radius)
area=3.14987654*(radius**2)
print("area of the circle is ->", area)
print(f"area of the circle is ((Area)): {area:.2f}")

import math
print(math.pi)
print(math.pow(radius,2))

area = math.pi*math.pow(radius,2)
print(f"area of the circle is {area:.2f}")

# one line code * donot use single line code

print(3.14*(float(input("Enter radius of the circle\n"))**2))