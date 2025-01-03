def add_security(func):

    def wrapper():
        print("Before the function is called")
        print("Add helmet,dashcash, gloves, knee guards, license")
        func()
        print("After the function is called")
        print("Secure driving , leaving all the items")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("ola")

@add_security
def driving_scooty():
    print("Normal function")