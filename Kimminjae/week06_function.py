# week06_function.py
# before decorator
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


@time_checker
def factorial(n):
    """
    factorial function
    :param n: more than zero
    :return: n!
    """
    # with iteration
    result = 1
    for k in range(1, n + 1):
        result *= k
    return result


@time_checker
def power(x, n):
    """
    power function
    :param x: base
    :param n: exponent
    :return: x^n
    """
    result = 1
    for _ in range(n):
        result *= x
    return result


# get time of factorial function
fac_time = time_checker(factorial)
print(fac_time(10000))

# get time of power function
pow_time = time_checker(power)
print(pow_time(2, 10000))
