#write a programme to take the user age and
# decide if he/she can go to club

# step 1
# user i/p -> data type ->int
# or o/p-> string he can go to club or not

# Step 2 rough logic
# age>21 print can go
# age<21 print cannot go

# step 3 write the logic

age= int(input("Enter your age\n"))

if age>=21:
    print("can go to club")
else:
    print("can't go with this age")

# step 4 -> check for edge cases
# negative ages or extremely high values ->programme will break
# non -numeric input
# Age which is valid


#step 5 ->optimize the code
# Handling the edge cases
