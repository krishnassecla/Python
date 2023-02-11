# class MyTest:
#     def __init__(self, limit):
#         self.limit = limit
#         print('__init__',self)


#     def __iter__(self):
#         print('iter')
#         self.x = 5
#         return self

#     def __next__(self):
#         print('__next__')
#         x = self.x 
#         if x > self.limit:
#             raise StopIteration

#         # else

#         self.x = x + 1
#         print(x, 'this is x')
#         return self.x 


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

