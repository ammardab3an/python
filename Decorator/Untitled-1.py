from Decorators import *
import math
@decorator
def foo(name):
    return (name +" you're foo")

@timer
def wast_of_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

class TimeWaster:
        @debug
        def __init__(self, max_num):
                self.max_num = max_num

        @timer
        def waste_time(self, num_times):
                for _ in range(num_times):
                        sum([i**2 for i in range(self.max_num)])

@CountCalls
def say_whee():
    print("Whee!")

