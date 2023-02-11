# class MyTest:
#     def __init__(self, limit):
#         self.limit = limit
#         print("__init__", self)

#     def __iter__(self):
#         print("iter")
#         self.x = 5
#         return self

#     def __next__(self):
#         print("__next__")
#         x = self.x
#         if x > self.limit:
#             raise StopIteration

#         # else

#         self.x = x + 1
#         print(x, "this is x")
#         return x


# for i in MyTest(10):
#     print(i)


# names = ['pravesh', 'cheems', 'a', 'c', 'b']
# print(names)
# iter_names = iter(names)
# # print(dir(iter_names))
# # print(iter_names.__repr__())

# for index, value in enumerate(iter_names):
#     print(index, value)

# print("without enumare")
# for val in names:
#     print(val, end='----')


# 1. Write a Python program to create an iterator from several iterables in a sequence and display the type and elements of the new iterator.


# iterables = [{'s', 'e', 't'}, 123, "hello",]
# iter_iterables = iter(iterables)
# for iterable in iterables:
#     print(type(iterable), iterable)

# Write a Python program to generate the running product of the elements of an given iterable


# for num in ints:
#     product =


# class RunningProduct:
#     def __init__(self, nums: "iterable") -> None:
#         self.nums = nums
#         print(nums)

#     def __iter__(self):
#         print(self.nums)
#         return self

#     def __next__(self):
#         print("next", self.nums)


# nums = [1, 2, 3, 4, 5, 6, 7]

# for r in RunningProduct(nums):
#     print(r)


import socket

socks = socket.socket()
socks.connect(("data.pre4.org", 80))
cmd = "GET data.pre4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
socks.send(cmd)

while True:
    data = socks.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

socks.close()
