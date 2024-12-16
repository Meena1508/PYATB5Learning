# write a program to return the letter grade for numerical score
from multiprocessing.heap import Arena

# A:90-100
# B:80-89
# C:70-79
# D:60-69
# F:0-59

# logic building formula

# user input ->score or marks ->int
# o/p ->string ->A,B,C

score = int(input("enter the score \n"))

# score >=90 and score<=100 ->A
# score >=80 and score<=89 ->B

if 90 <= score <= 100:
    print("your grade is", "A")
elif score >=80 and score<=89:
    print("your garde is", "B")
elif score >=70 and score<=79:
    print("your garde is", "C")
elif score >=60 and score<=69:
    print("your garde is", "D")
elif score>=100 and score<=-1:
    print("your are a superman , u cant get a grade!00")
else:
    print("your grade is""F")


# edge cases
# characters are entered
# negative numbers and numbers greater than 100

