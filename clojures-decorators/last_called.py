#coding=utf-8
import time
def make_timer():
	last_called = None
	def elapsed():
		#nonlocal last_called
		now = time.time()
		if last_called is None:
			last_called = now
			return None
		result = now - last_called
		last_called = now
		return result
	return elapsed

def escape_unicode(func):
	def wrap(*args,**kwargs):
		x = func(*args,**kwargs)
		return ascii(x)
	return wrap

@escape_unicode
def northern_city():
	return 'Gjøvik' 
