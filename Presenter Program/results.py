# This module includes all the methods required to save the results to a .txt file. 
# At a later date, this could be modified to write to an online database instead of a .txt file. 

# Written By: Michael Carter, Oct./Nov. 2019
# For my PSYCO 403/505 research project

class ResultsFile:
	# This class represents one .txt file of the results of one participant's trial. 
	# The file is named "results" + 3 random digits, e.g. "results123.txt".
	
	# A file is initialized with:
	#     1. the participant number
	#     2. whether the words were colored 
	
	# For each trial, an info line must be written, signifying:
	#     1. number of words
	#     2. presentation time
	#     3. delay time
	
	
	def __init__(self):
		pass
	
	def __create_file(self):
		pass
	
	def new_trial(self, word_list, present_time, delay_time):
		# initializes a new trial, writing the info header to the file.
		# word_list is in the actual order presented.
		pass
	
	def write_result(self, entry, start_time, end_time):
		# writes one line of the participant's input to the file, along with their
		# start and end time (corresponding to the first keypress until "enter" is pressed).
		pass
	
	

	def close_file(self):
		pass