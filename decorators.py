# def outer():
#     x = 5

#     def inner():
#         print(5)

#     inner()


# outer()


# @uppercase_decorator
# def say_hi():
#     return "hello there"


# print(say_hi())

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase

#     return wrapper

# def split_str(function):
#     def wrapper():
#         func = function()
#         splitted_str = func.split()
#         return splitted_str

#     return wrapper

# @split_str
# @uppercase_decorator
# def say_hi():
#     return "Hey there"

# say_hi()


def decorator_function(msg):
    print("I am inside the decorator_funciton.")
    # a common pattern is using *args and **kwargs in the wrapper function
    def wrapper_function(*args, **kwargs):
        # i can edit this function without hassle
        print("this is wrapper")
        return msg(*args, **kwargs)

    return wrapper_function


# classes as decorators
class decorator_class(object):
    def __init__(self, msg):
        self.original_function = msg

    def __call__(self, *args: any, **kwds: any) -> any:
        print("call method executed thhis  ")


# def msg():
#     print("this is a message")


# decorated_msg = decorator_function(msg)
# decorated_msg()
# print(decorator_function.__name__)


# but if i write
@decorator_function
def msg():
    print("this is a msg")


msg()


@decorator_function
def display_info(name, age):
    print("display info ran with arguments ({} ,{})".format(name, age))


display_info("praevsh", 19)

# msg()
# this is same as writing
# msg = decorator_function(msg)
# here msg function is decorated and decorator_function is the decorator


import sys

print("Python version")
print(sys.version)

print("Version info.")
print(sys.version_info)


def test():
    print("test")


print(dir(test))
test.__call__()
