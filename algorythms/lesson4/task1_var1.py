"""
Определить, какое число в массиве встречается чаще всего.
"""

import cProfile
from random import randint


def get_number_freq(items_cnt):
    array = [randint(0, items_cnt // 2) for _ in range(items_cnt)]

    size = len(array)
    max_cnt = 1
    item = array[0]

    for i in range(size - 1):
        cnt = 1
        for j in range(i + 1, size):
            if array[i] == array[j]:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
            item = array[i]

    return item, items_cnt


# task1_var1.get_number_freq(100)
# 1000 loops, best of 5: 286 usec per loop

# task1_var1.get_number_freq(200)
# 1000 loops, best of 5: 991 usec per loop

# task1_var1.get_number_freq(400)
# 1000 loops, best of 5: 4.1 msec per loop

# task1_var1.get_number_freq(800)
# 1000 loops, best of 5: 17.1 msec per loop


""" cProfile.run('get_number_freq(1000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.030    0.030 <string>:1(<module>)
     1000    0.000    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:244(randint)
     1000    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 task1_var1.py:10(<listcomp>)
        1    0.029    0.029    0.030    0.030 task1_var1.py:9(get_number_freq)
        1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1026    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

""" cProfile.run('get_number_freq(2000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.108    0.108 <string>:1(<module>)
     2000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     2000    0.000    0.000    0.002    0.000 random.py:244(randint)
     2000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 task1_var1.py:10(<listcomp>)
        1    0.106    0.106    0.108    0.108 task1_var1.py:9(get_number_freq)
        1    0.000    0.000    0.108    0.108 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     2056    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

""" cProfile.run('get_number_freq(4000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.418    0.418 <string>:1(<module>)
     4000    0.002    0.000    0.003    0.000 random.py:200(randrange)
     4000    0.001    0.000    0.004    0.000 random.py:244(randint)
     4000    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.001    0.001    0.005    0.005 task1_var1.py:10(<listcomp>)
        1    0.413    0.413    0.418    0.418 task1_var1.py:9(get_number_freq)
        1    0.000    0.000    0.418    0.418 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     4000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     4078    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

""" cProfile.run('get_number_freq(8000)')
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.681    1.681 <string>:1(<module>)
     8000    0.003    0.000    0.006    0.000 random.py:200(randrange)
     8000    0.002    0.000    0.008    0.000 random.py:244(randint)
     8000    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.001    0.001    0.010    0.010 task1_var1.py:10(<listcomp>)
        1    1.672    1.672    1.681    1.681 task1_var1.py:9(get_number_freq)
        1    0.000    0.000    1.681    1.681 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     8000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     8179    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
cProfile.run('get_number_freq(64000)')