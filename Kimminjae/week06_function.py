# week06_function.py
# before decorator
import time
def factorial(n):
    """
    factorial function
    :param n: more than zero
    :return: n!
    """
    s = time.time()
    # with iteration
    result = 1
    for k in range(1, n+1):
        result *= k
    e = time.time()
    print("iteration time : ", e-s)
    return result


print(factorial(10000))

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





