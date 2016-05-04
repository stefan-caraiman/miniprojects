from __future__ import print_function

class Trace:
	def __init__(self):
		self.enabled = True

	def __call__(self,func):
		def wrap(*args,**kwargs):
			if self.enabled:
				print("Calling".format(func))
			return func(*args,**kwargs)
		return wrap

tracer = Trace()


@tracer
def rotate_list(lst):
	return lst[1:] +[lst[0]]

l = [1,2,3,4]
for x in range(5):
	l = rotate_list(l)
	print(l)