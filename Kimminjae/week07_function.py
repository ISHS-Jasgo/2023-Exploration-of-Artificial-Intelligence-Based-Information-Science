animal = 'fruitbat'


def change_and_print_global():
    global animal
    student = 'woojin'
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)
    print(locals())
    print(change_and_print_global.__name__)
    print(change_and_print_global.__doc__)


def factorial_repetition(n):
    """
    factorial function with repetition
    :param n: more than zero
    :return: n!
    """
    # with iteration
    result = 1
    for k in range(1, n + 1):
        result *= k
    return result


def factorial_recursion(n):
    """
    factorial function with recursion
    :param n: more than zero
    :return: n!
    """
    # with recursion
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


fibo = []


def fibonacci_repetition(n):
    """
    fibonacci function with repetition
    :param n: more than zero
    :return: n!
    """
    # with iteration
    fibo.append(1)
    fibo.append(1)
    for k in range(2, n):
        fibo.append(fibo[k - 1] + fibo[k - 2])
    return fibo[n - 1]


def fibonacci_recursion(n):
    """
    fibonacci function with recursion
    :param n: more than zero
    :return: n!
    """
    # with recursion
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


if __name__ == "__main__":
    number = int(input("Enter number : "))
    print(factorial_repetition(number))
    print(factorial_recursion(number))
    print(fibonacci_repetition(number))
    print(fibonacci_recursion(number))