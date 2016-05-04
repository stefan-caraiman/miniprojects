from __future__ import print_function


message = 'global'

def enclosing():
	message = 'enclosing'

	def local():
		global message #we will be changing the global variable value
		#nonlocal introduces names from the enclosing namespace into the local namespace
		#nonlocal was introduced in Python3
		message = 'local'

	print('enclosing message:', message)
	local()
	print('enclosing message', message)

print('global message:', message)
enclosing()
print('global message:', message)