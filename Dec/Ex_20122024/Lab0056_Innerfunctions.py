def outer_function():
    var1=30 #local

    def inner_function1():
        var2=90
        print(var1)


    def inner_function2():
        print(var1)

    inner_function1()
    inner_function2()
    # print(var2) inner variable cannot be used outside the function

outer_function()


