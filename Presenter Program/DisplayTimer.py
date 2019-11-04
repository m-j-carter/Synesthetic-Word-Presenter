

# Written By: Michael Carter, Oct. 2019
# For my PSYCO 403/505 research projects

import time

class DisplayTimer:
	# This class allows the events to be timed, to make decisions as to whether or not to progress.

	def __init__(self):
		self.__time_init = time.time()      # current time in fractional seconds

	def reset(self):
		self.__time_init = time.time()

	def been_longer_than(self, check_seconds):
		time_now = time.time()
		if self.__time_init < (time_now - check_seconds):
			return True
		else:
			return False

