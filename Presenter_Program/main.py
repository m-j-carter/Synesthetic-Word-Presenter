## This file includes everything to run an entire presentation and recall task

## Written By: Michael Carter, Oct./Nov. 2019
## For my PSYCO 403/505 research project


## Notes/Changelog:
##   - At some point I should merge all the duplicate methods between SerialRecall
##       and PresentWords into a single utilities module.
##   - Should also move the instructions out of the individual modules.

from time import sleep
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
	## INITIALIZE ##
	window = create_window()
	PresentWords.set_window(window) 
	
	word_library = read_words_file(WORDS_FILENAME)
	PresentWords.set_word_lib(word_library) 

	results_file = ResultsFile()    
	PresentWords.set_results_file(results_file)

	SerialRecall.set_results_file(results_file)
	SerialRecall.set_window(window)


	## SET VARIABLES ##
	num_words = 3
	present_time = 2	# seconds
	delay_time = 1		# seconds
	is_colored = True
	recall_timer = 0.5	# minutes
	
	
	## PRESENT WORDS ##
	reset_window_defaults(window)
	PresentWords(num_words, present_time, delay_time, is_colored)      
	
	# Distractor Task would go here if used.
	sleep(3)
	
	## SERIAL RECALL TASK ##
	reset_window_defaults(window)
	SerialRecall(num_words, recall_timer)		


def create_window():
	# Create a window for the game and open it.
	window = Window("Word Presenter", WINDOW_SIZE[0], WINDOW_SIZE[1])
	window.clear()
	window.update()

	return window   

def reset_window_defaults(window):
	# returns the window's colors, fonts, etc. to their defaults
	window.set_bg_color(BG_COLOR)
	window.set_font_color(DEFAULT_FONT_COLOR)
	window.set_font_size(DEFAULT_FONT_SIZE)
	window.set_font_name(DEFAULT_FONT_NAME)	
	

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
