import time


# decorator
def time_checker(func):
    def inner(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'{func.__name__} : {end - start}s')
        return result

    return inner
