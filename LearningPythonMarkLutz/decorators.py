# def is_valid_move(move_function):

# 	def wrapper(actual_x):
# 		if actual_x == 5:
# 			print("TRUEEE")
# 			# we have access to move_function by closure
# 			move_function(actual_x)
# 			# return True
		

# 	return wrapper

# @is_valid_move
# def move(x):
# 	print("THIS IS MOVE")


# move(5)


class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func  #spam == func

	# this func is called whenever an instance of tracer is called
	def __call__(self, *args):
		self.calls += 1
		print(f"call {self.calls} to {self.func.__name__}")
		self.func(*args)

@tracer
def spam(a, b, c): #spam = tracer(spam)
	print(a+b+c)   #wraps spam in a decorator object

spam(1,2,3)
spam(3,4,5)

@tracer
def greet(name):
	print("Hello", name)


greet("Prvahes")
greet("Cheems")