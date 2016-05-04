from __future__ import print_function
import functools

def noop(func):
	@functools.wraps(func)
	def noop_wrapper():
		return func()
	return noop_wrapper

@noop
def hello():
	"It will print a hello message."
	print("Hello there!")

print(hello.__name__)
print(hello.__doc__)

def check_positive(index):
	def validator(func):
		def wrap(*args):
			if args[index] < 0:
				raise ValueError("Argument {} isn't positive".format(index))
			return func(*args)
		return wrap
	return validator

@check_positive(1)
def create_list(value,size):
	return [value] * size

print(create_list("some_val",5))