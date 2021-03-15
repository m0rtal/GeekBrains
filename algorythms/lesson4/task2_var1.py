"""
Простые числа - Решето Эратосфена
"""

import cProfile


def sieve(n):
    if n < 2:
        return None

    limit = pow(n, 2)
    sieve_ = [True] * limit
    sieve_[0] = False
    sieve_[1] = False

    i = 4
    while i < limit:
        if sieve_[i] and i % 2 == 0:
            sieve_[i] = False
        elif sieve_[i]:
            j = i * 2
            while j < limit:
                sieve_[j] = False
                j += i

        i += 1

    return [i for i, f in enumerate(sieve_) if f][n]


""" cProfile.run('sieve(1000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.243    0.243 <string>:1(<module>)
        1    0.031    0.031    0.031    0.031 task2_var1.py:29(<listcomp>)
        1    0.209    0.209    0.241    0.241 task2_var1.py:8(sieve)
        1    0.000    0.000    0.243    0.243 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

""" cProfile.run('sieve(2000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.007    0.007    1.205    1.205 <string>:1(<module>)
        1    0.116    0.116    0.116    0.116 task2_var1.py:29(<listcomp>)
        1    1.082    1.082    1.198    1.198 task2_var1.py:8(sieve)
        1    0.000    0.000    1.205    1.205 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

""" cProfile.run('sieve(4000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.028    0.028    5.207    5.207 <string>:1(<module>)
        1    0.463    0.463    0.463    0.463 task2_var1.py:29(<listcomp>)
        1    4.716    4.716    5.178    5.178 task2_var1.py:8(sieve)
        1    0.000    0.000    5.207    5.207 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

""" cProfile.run('sieve(8000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.113    0.113   21.733   21.733 <string>:1(<module>)
        1    1.837    1.837    1.837    1.837 task2_var1.py:29(<listcomp>)
        1   19.782   19.782   21.620   21.620 task2_var1.py:8(sieve)
        1    0.000    0.000   21.733   21.733 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# task2_var1.sieve(100)
# 100 loops, best of 5: 1.78 msec per loop

# task2_var1.sieve(200)
# 100 loops, best of 5: 7.43 msec per loop

# task2_var1.sieve(400)
# 100 loops, best of 5: 31.4 msec per loop

# task2_var1.sieve(800)
# 100 loops, best of 5: 137 msec per loop
