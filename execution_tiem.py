import time
from html.parser import starttagopen

start = time.time()
s =0
for i in range(10000000):
    s = s+i
end = time.time()
print(f"total execution time: {end - start:.5f}")


start = time.perf_counter()
s =0
for i in range(10000000):
    s = s+i
end = time.perf_counter()
print(f"total time: {end - start:.5f}")


from contextlib import contextmanager

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"time taken: {end - start:.5f}")

with timer():
    s = 0
    for i in range(10000000):
        s = s+i


import time

def timer(funcs):
    start= time.perf_counter()
    funcs()
    end = time.perf_counter()
    print(f"{end-start:.5f}")


def code_block_1():
    s = 0
    for i in range(10000000):
        s += i

def code_block_2():
    s = 0
    for i in range(5000000):
        s += i

def code_block_3():
    s = 0
    for i in range(20000000):
        s += i

x = [code_block_1, code_block_2, code_block_3]
for i in x:
    timer(i)




def timeit(func):
    def inner(*args,**kwargs):
        start = time.perf_counter()
        result = func(*args,**kwargs)
        end = time.perf_counter()
        print(f"{end-start:.5f}")
        return result
    return inner



@timeit
def code_block_1():
    s = 0
    for i in range(10000000):
        s += i

@timeit
def code_block_2():
    s = 0
    for i in range(5000000):
        s += i

@timeit
def code_block_3():
    s = 0
    for i in range(20000000):
        s += i

@timeit
def greet(name, age=30):
    print(f"Hello, {name}. You are {age} years old.")



# Call the functions and they will print the time taken automatically
code_block_1()
code_block_2()
code_block_3()


# Call the function with different arguments
greet("Alice", age=25)  # Positional and keyword argument
greet("Bob")  # Only a positional 