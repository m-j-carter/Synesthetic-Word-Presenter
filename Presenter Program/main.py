# This file includes everything to run an entire instance

# Written By: Michael Carter, Oct./Nov. 2019
# For my PSYCO 403/505 research project


import pygame as pg
from pygame.locals import *

from uagame import Window
from word import Word
from serialrecall import SerialRecall
from presentwords import PresentWords
from results import ResultsFile


## INPUT PARAMETERS ##
WORDS_FILENAME = 'words.txt'
WINDOW_SIZE = (700, 500)
DEFAULT_FONT_COLOR = "gray"
DEFAULT_FONT_SIZE = 36
DEFAULT_FONT_NAME = "Arial"
BG_COLOR = "gray50"



def main():
	
	window = create_window()

	word_library = read_words_file(WORDS_FILENAME)
	PresentWords.set_word_lib(word_library) 
	PresentWords.set_window(window) 

	#results_file = ResultsFile()    
	#PresentWords.set_results_file(results_file)

	#SerialRecall.set_results_file(results_file)
	SerialRecall.set_window(window)


	# Present Words
	test_1 = PresentWords(4, 5, 2, False)      # (num_words, present_time, delay_time, is_colored (bool))
	# Distractor Task?

	# Serial Recall Task


	test_2 = PresentWords(5, 3, 1, True)    




def create_window():
	# Create a window for the game and open it.
	window = Window("Word Presenter", WINDOW_SIZE[0], WINDOW_SIZE[1])
	#clock.tick(60)
	window.set_bg_color(BG_COLOR)
	window.set_font_color(DEFAULT_FONT_COLOR)
	window.set_font_size(DEFAULT_FONT_SIZE)
	window.set_font_name(DEFAULT_FONT_NAME)
	window.clear()
	window.update()

	return window   


def read_words_file(filename):
	# Read in the list of possible words.
	# Returns a list of objects of the Word class.
	word_list = []
	try:		
		with open(filename,'r') as file:
			for input_word in file.readlines():
				word_list.append(Word(input_word.strip('\n\r')))
		assert len(word_list) > 0, "word list cannot be empty"
	except FileNotFoundError as e:
		print('Error: File not found! %s' % (e.strerror))
		return
	else:		
		return word_list


if __name__ == "__main__":
	main()
