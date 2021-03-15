"""
Определить, какое число в массиве встречается чаще всего.
"""

import cProfile
from random import randint


def get_number_freq(items_cnt):
    array = [randint(0, items_cnt // 2) for _ in range(items_cnt)]

    return sorted(((i, array.count(i)) for i in set(array)))[-1]


# task1_var2.get_number_freq(100)
# 1000 loops, best of 5: 107 usec per loop

# task1_var2.get_number_freq(200)
# 1000 loops, best of 5: 299 usec per loop

# task1_var2.get_number_freq(400)
# 1000 loops, best of 5: 947 usec per loop

# task1_var2.get_number_freq(800)
# 1000 loops, best of 5: 3.37 msec per loop

""" cProfile.run('get_number_freq(1000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
     1000    0.000    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:244(randint)
     1000    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 task1_var2.py:10(<listcomp>)
      430    0.000    0.000    0.005    0.000 task1_var2.py:12(<genexpr>)
        1    0.000    0.000    0.006    0.006 task1_var2.py:9(get_number_freq)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        1    0.000    0.000    0.005    0.005 {built-in method builtins.sorted}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
      429    0.005    0.000    0.005    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1014    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

""" cProfile.run('get_number_freq(2000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.022    0.022 <string>:1(<module>)
     2000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     2000    0.000    0.000    0.002    0.000 random.py:244(randint)
     2000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 task1_var2.py:10(<listcomp>)
      877    0.000    0.000    0.020    0.000 task1_var2.py:12(<genexpr>)
        1    0.000    0.000    0.022    0.022 task1_var2.py:9(get_number_freq)
        1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
        1    0.000    0.000    0.020    0.020 {built-in method builtins.sorted}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
      876    0.019    0.000    0.019    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2040    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

""" cProfile.run('get_number_freq(4000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.084    0.084 <string>:1(<module>)
     4000    0.002    0.000    0.003    0.000 random.py:200(randrange)
     4000    0.001    0.000    0.004    0.000 random.py:244(randint)
     4000    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.001    0.001    0.005    0.005 task1_var2.py:10(<listcomp>)
     1742    0.001    0.000    0.079    0.000 task1_var2.py:12(<genexpr>)
        1    0.000    0.000    0.084    0.084 task1_var2.py:9(get_number_freq)
        1    0.000    0.000    0.084    0.084 {built-in method builtins.exec}
        1    0.000    0.000    0.079    0.079 {built-in method builtins.sorted}
     4000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
     1741    0.078    0.000    0.078    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     4101    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

""" cProfile.run('get_number_freq(8000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.341    0.341 <string>:1(<module>)
     8000    0.003    0.000    0.007    0.000 random.py:200(randrange)
     8000    0.002    0.000    0.009    0.000 random.py:244(randint)
     8000    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.001    0.001    0.010    0.010 task1_var2.py:10(<listcomp>)
     3438    0.002    0.000    0.330    0.000 task1_var2.py:12(<genexpr>)
        1    0.000    0.000    0.341    0.341 task1_var2.py:9(get_number_freq)
        1    0.000    0.000    0.341    0.341 {built-in method builtins.exec}
        1    0.000    0.000    0.331    0.331 {built-in method builtins.sorted}
     8000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
     3437    0.329    0.000    0.329    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     8196    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
