from operator import add, mul


def square(x): return x * x


def identity(x): return x


def triple(x): return 3 * x


def increment(x): return x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    # s = str(x)

    # def f(i: int, prev: int) -> bool:
    #     if i == len(s):
    #         return True
    #     n = int(s[i])
    #     if n >= prev:
    #         return f(i + 1, n)
    #     return False

    def f2(num: int, prev: int) -> bool:
        if num == 0:
            return True
        if prev >= (num % 10):
            return f2(num // 10, num % 10)
        return False

    return f2(x // 10, x % 10)
    # return f(0, 0)


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    def f(num: int, k: int, last: int) -> int:
        if k == 0:
            return last
        if num < 10:
            return num
        if num // 10 % 10 < num % 10:
            return f(num // 10, k, num % 10)
        else:
            return f(num // 10, k - 1, num % 10)

    return f(n, k + 1, 0)


def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power = 1.0
    tmp = x
    if x >= 1:
        while tmp > 2:
            tmp //= 2
            power += 1
    else:
        while tmp < 2:
            tmp *= 2
            power -= 1
    if abs(2 ** (power + 1) - x) <= abs(2 ** power - x):
        return 2 ** (power + 1)
    return 2 ** power


def make_repeater(func, n):
    """Returns the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    def f(n):
        if n == 0:
            return lambda x: x
        return composer(func, f(n - 1))

    return lambda x: f(n)(x)


def composer(func1, func2):
    """Returns a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def apply_twice(func):
    """Returns a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    return composer(func, func)


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    def checker(x): return False
    i = 2
    while i < n + 1:
        if not checker(i):
            checker = (lambda f, i: lambda x: f(x) or x %
                       i == 0)(checker, i)
        i = i + 1
    return checker


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = 2
    while i < n + 1:
        if not checker(i):
            def outer(f, i):
                def inner(x):
                    return f(x) or x % i == 0
                return inner
            checker = outer(checker, i)
        i = i + 1
    return checker
