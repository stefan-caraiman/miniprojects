from __future__ import print_function
import os

def create_crawled_dir(directory):
	if not os.path.exists(directory):
		print('Creating project ' +  directory)
		os.makedirs(directory)
		os.removedirs(directory)

create_crawled_dir("google")