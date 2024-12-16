for i in range(0,10, 1): # 0 to 9 , times ->10
    if i==6 or i==5:
        print(i)
    else:
        pass # pass is placeholder statement that does nothing
        # it is used when the statement is syntactically needed no action

# |i| condition o/p
# |0| 0==6 -> false -> no o/p is printed
# |1| 1==6 -> false -> no o/p is printed
# |2| 2==6 -> false -> no o/p is printed
# |3| 3==6 -> false -> no o/p is printed
# |5| 0==6 5==5-> true -> o/p = 5
# |6| 6==6 5==5-> true -> o/p = 6
# |7| 7==6 -> false -> no o/p is printed
# |8| 8==6 -> false -> no o/p is printed
# |10| 10==6 -> false -> loop exit
