"""
Простые числа - Без решета Эратосфена
"""

import cProfile


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    limit = pow(n, 0.5)

    i = 2
    while i <= limit:
        if not n % i:
            return False

        i += 1

    return True


def prime(n):
    cnt = 0
    i = 2
    while cnt < n:
        if is_prime(i):
            cnt += 1
        i += 1

    return i - 1


""" cProfile.run('prime(1000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.001    0.001    0.009    0.009 task2_var2.py:27(prime)
     7918    0.006    0.000    0.008    0.000 task2_var2.py:8(is_prime)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
     7917    0.001    0.000    0.001    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

""" cProfile.run('prime(2000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.022    0.022 <string>:1(<module>)
        1    0.002    0.002    0.022    0.022 task2_var2.py:27(prime)
    17388    0.018    0.000    0.020    0.000 task2_var2.py:8(is_prime)
        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
    17387    0.002    0.000    0.002    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

""" cProfile.run('prime(4000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.060    0.060 <string>:1(<module>)
        1    0.005    0.005    0.060    0.060 task2_var2.py:27(prime)
    37812    0.050    0.000    0.055    0.000 task2_var2.py:8(is_prime)
        1    0.000    0.000    0.060    0.060 {built-in method builtins.exec}
    37811    0.005    0.000    0.005    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

""" cProfile.run('prime(8000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.163    0.163 <string>:1(<module>)
        1    0.012    0.012    0.163    0.163 task2_var2.py:27(prime)
    81798    0.141    0.000    0.151    0.000 task2_var2.py:8(is_prime)
        1    0.000    0.000    0.163    0.163 {built-in method builtins.exec}
    81797    0.011    0.000    0.011    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# task2_var2.prime(100)
# 100 loops, best of 5: 259 usec per loop

# task2_var2.prime(200)
# 100 loops, best of 5: 680 usec per loop

# task2_var2.prime(400)
# 100 loops, best of 5: 1.85 msec per loop

# task2_var2.prime(800)
# 100 loops, best of 5: 4.99 msec per loop
