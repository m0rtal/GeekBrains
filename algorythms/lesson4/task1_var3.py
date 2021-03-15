"""
Определить, какое число в массиве встречается чаще всего.
"""

import cProfile
from random import randint


def get_number_freq(items_cnt):
    array = [randint(0, items_cnt // 2) for _ in range(items_cnt)]

    scores = {}

    for i in array:
        try:
            scores[i] += 1
        except KeyError:
            scores[i] = 1

    return sorted((count, item) for item, count in scores.items())[-1]


# task1_var3.get_number_freq(100)
# 1000 loops, best of 5: 73.7 usec per loop

# task1_var3.get_number_freq(200)
# 1000 loops, best of 5: 150 usec per loop

# task1_var3.get_number_freq(400)
# 1000 loops, best of 5: 300 usec per loop

# task1_var3.get_number_freq(800)
# 1000 loops, best of 5: 663 usec per loop


""" cProfile.run('get_number_freq(1000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
     1000    0.000    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:244(randint)
     1000    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 task1_var3.py:10(<listcomp>)
      432    0.000    0.000    0.000    0.000 task1_var3.py:20(<genexpr>)
        1    0.000    0.000    0.002    0.002 task1_var3.py:9(get_number_freq)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1026    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
"""

""" cProfile.run('get_number_freq(2000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
     2000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     2000    0.000    0.000    0.002    0.000 random.py:244(randint)
     2000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 task1_var3.py:10(<listcomp>)
      859    0.000    0.000    0.000    0.000 task1_var3.py:20(<genexpr>)
        1    0.000    0.000    0.003    0.003 task1_var3.py:9(get_number_freq)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2053    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
"""

""" cProfile.run('get_number_freq(16000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.026    0.026 <string>:1(<module>)
    16000    0.007    0.000    0.013    0.000 random.py:200(randrange)
    16000    0.004    0.000    0.016    0.000 random.py:244(randint)
    16000    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.003    0.003    0.019    0.019 task1_var3.py:10(<listcomp>)
     6948    0.001    0.000    0.001    0.000 task1_var3.py:20(<genexpr>)
        1    0.003    0.003    0.026    0.026 task1_var3.py:9(get_number_freq)
        1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
        1    0.003    0.003    0.004    0.004 {built-in method builtins.sorted}
    16000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    16387    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
"""

""" cProfile.run('get_number_freq(64000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.109    0.109 <string>:1(<module>)
    64000    0.026    0.000    0.052    0.000 random.py:200(randrange)
    64000    0.015    0.000    0.067    0.000 random.py:244(randint)
    64000    0.018    0.000    0.025    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.012    0.012    0.079    0.079 task1_var3.py:10(<listcomp>)
    27662    0.004    0.000    0.004    0.000 task1_var3.py:20(<genexpr>)
        1    0.011    0.011    0.108    0.108 task1_var3.py:9(get_number_freq)
        1    0.000    0.000    0.109    0.109 {built-in method builtins.exec}
        1    0.014    0.014    0.018    0.018 {built-in method builtins.sorted}
    64000    0.003    0.000    0.003    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    65560    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
"""
cProfile.run('get_number_freq(64000)')