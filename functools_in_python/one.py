import functools


@functools.cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


print(factorial(10))
print(factorial(12))
print(factorial.cache_info())
