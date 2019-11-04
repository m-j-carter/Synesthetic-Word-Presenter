# This program is designed to present a set word list at set timed intervals
# For my PSYCO 403/505 research projects
# Written By: Michael Carter, Oct. 2019

import PresentWords as *
import Word as *


def main():
   	# input_list = read_words("words.txt")
	word_list = []
	for wd in read_words("words.txt"):
		word_list.append(Word(wd))

	
	ten_word_five_sec = PresentWords(10,5,2,word_list)		# parameters: (num_words, present_time, delay_time, word_list)
	


def read_words(filename):
	# Read in the list of words,
	# Returns a list of the words.
	
	try:		
		with open(filename,'r') as file:
			word_list = file.readlines()

	except FileNotFoundError as e:
		print('Error: File not found! %s' % (e.strerror))
		return 
	
	else:		
		return word_list


if __name__ == "__main__":
	main()