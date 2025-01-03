import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("total time taken by function is -->", end_time - start_time)

    return wrapper()


def print_logs(func):
    def wraper():
        print("starting logs")
        func()
        print("ending logs")

    return wraper()


@time_decorator
@print_logs
def test_ui_1():
    print("add a function, time taken by function1")
    time.sleep(2)


@time_decorator
@print_logs
def test_ui_2():
    print("add a function, time taken by function2")
    time.sleep(5)
