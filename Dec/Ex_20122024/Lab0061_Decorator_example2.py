def add_before_ui_after_ui(func):

    def wrapper():
        print("Before running the ui Tc")
        print("start the browser")
        func()
        print("after running the ui tc")
        print("stop browser")

    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print("i will test the ui")

