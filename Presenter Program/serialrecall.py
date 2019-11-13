## This file contains the classes PresentWords and Word, as used in the main timed word presenter program
## Word is its own class (instead of a list of strings) to allow for easy modifications 

## Written By: Michael Carter, Oct./Nov. 2019
## For my PSYCO 403/505 research project


# Notes/Changelog:
#   - Still needs timer stuff
#   - Needs 


import math
import time
import pygame as pg
from pygame.locals import *
import pygame_textinput

from uagame import Window
from results import ResultsFile


## TEST PARAMETERS ##
WINDOW_SIZE = (700, 500)
DEFAULT_FONT_COLOR = "gray"
DEFAULT_FONT_SIZE = 36
DEFAULT_FONT_NAME = "Arial"
BG_COLOR = "gray50"


class SerialRecall:
	# This class represents the serial recall sheet.
	# Utilizes Nearoo's pygame text input module: 
	#    https://github.com/Nearoo/pygame-text-input

	@classmethod
	def set_window(cls, window_from_parent):
		cls.window = window_from_parent
	@classmethod
	def set_results_file(cls, results_file):
		cls.results = results_file    


	def __init__(self, num_words):
		self.__clock = pg.time.Clock()
		self.__num_words = num_words
		self.__window = SerialRecall.window
		self.__results = SerialRecall.results
		self.__text_inputs_list = []
		self.__row_index = 0
		self.__current_input = None
		self.__quit = False
		self.__finished = False
		self.__time_last = None
		
		self.__window.set_auto_update(False)
		self.__create_text_inputs()
		self.__run()


	def __create_text_inputs(self):
		self.__words_strings = [""] * self.__num_words
		for i in range(0, self.__num_words):
			self.__text_inputs_list.append(pygame_textinput.TextInput(
			                                                        initial_string=self.__words_strings[i],
			                                                        font_family=DEFAULT_FONT_NAME,
			                                                        font_size=math.floor(DEFAULT_FONT_SIZE*1.0),
			                                                        text_color=(255, 255, 255),
			                                                        cursor_color=(200, 200, 200)))

		self.__current_input = self.__text_inputs_list[self.__row_index]
		
			
	def __run(self):
		# handles one entire iteration of the SerialRecall class.
		while not self.__quit and not self.__finished:
			self.__window.clear()									
			self.__check_events()
			self.__update_current_input()			
			self.__draw_window()
			self.__window.update()
			self.__update_words_list()
			self.__clock.tick(60)		
			
		self.__print_results()
		return False       # end of the task

	def __print_results(self):
		for i in range(self.__num_words):
			print(self.__text_inputs_list[i].get_text())
			
	def __update_words_list(self):
		# required to save progress
		for i in range(self.__num_words):
			self.__words_strings[i] = self.__text_inputs_list[i].get_text()


	def __draw_window(self):
		surface = self.__window.get_surface()
		window_height = self.__window.get_height()
		font_height = self.__window.get_font_height()

		self.__window.draw_string("Words remaining: %d"%(self.__count_remaining_words()), 10, 0)
		
		for i in range(self.__num_words):
			if self.__row_index == i:
				# draw the text as currently being entered
				surface.blit(self.__current_input.get_surface(), (10, DEFAULT_FONT_SIZE * (i+1)))
			
			else:
				# draw the entered text
				self.__window.draw_string(self.__text_inputs_list[i].get_text(),
			                                                  10, (DEFAULT_FONT_SIZE * (i+1)))


	def __check_events(self): 
		# handle user inputs
		self.__events = pg.event.get()
		for event in self.__events:
			if event.type == QUIT:
				self.__handle_quit()			
			
			if event.type == KEYUP:
				self.__handle_keypress(event.key)
				
	def __handle_keypress(self, key):
		# record the start time as the time of first keypress,
		#   and the end time as the time at which return is pressed.
		if key == K_DOWN:           
			self.__handle_key_down()
		if key == K_UP:
			self.__handle_key_up()
		if key == K_RETURN: 
			if self.__row_index >= self.__num_words - 1:
				self.__confirm_finished()	
			else:
				self.__handle_key_down()	# just treat it as a down arrow key

	def __handle_quit(self):
		self.__quit = True
		
	def __confirm_finished(self):
		# prompts the user to press enter to confirm their answers,
		#   or press any key to return.
		confirm_text = ["Press Enter to confirm your answers,", "or any key to return"]
		
		block_width = max(self.__window.get_string_width(text) for text in confirm_text) + 10
		block_height = len(confirm_text) * self.__window.get_font_height() + 10
		top = (self.__window.get_height() - block_height) // 2
		left  = (self.__window.get_width() - block_width) // 2
	
		block = pg.Rect(left, top, block_width, block_height)
		surface = self.__window.get_surface()
		pg.draw.rect(surface, (128,128,128), block, 1)
		
		for i, line in enumerate(confirm_text):
			x, y = self.__find_string_x_y(line, i, len(confirm_text))
			self.__window.draw_string(line, x, y)
		
		self.__window.update()
				
		while True:
			event = pg.event.poll()
			if event.type == QUIT:
				self.__handle_quit()			
			if event.type == KEYUP:
				if event.key == K_RETURN:
					self.__finished = True	
					return
				else:
					return
		
	
	
	
	def __find_string_x_y(self, print_string, line_no, total_lines=1):
		# returns a tuple of the (x,y) position to draw the string at.
		x = (self.__window.get_width() - self.__window.get_string_width(print_string)) // 2
		y = ((self.__window.get_height() - (self.__window.get_font_height() * total_lines+1))  // 2) + (self.__window.get_font_height() * line_no)

		return (x,y)
	
		
	def __handle_key_up(self):
		# TODO
		# pause timer and restart previous timer?
		self.__row_index -= 1 if self.__row_index > 0 else 0	
		#self.__update_current_input()
		
	def __handle_key_down(self):
		# TODO
		# record the time
		
		# advance to the next row or end input
		if self.__row_index < self.__num_words - 1:
			self.__row_index += 1
			#self.__update_current_input()

	def __update_current_input(self):
		self.__current_input = self.__text_inputs_list[self.__row_index]
		self.__current_input.update(self.__events)        # feed textinput any events
		
	def __count_remaining_words(self):
		# returns an integer of the number of words for which the value is null
		words_remaining = self.__num_words
		for word in self.__words_strings:
			if len(word) > 0: 
				words_remaining -= 1
		
		return words_remaining



def main():
	"""Tests the Methods"""

	window = create_window()

	results_file = ResultsFile()
	SerialRecall.set_results_file(results_file)
	SerialRecall.set_window(window)

	SerialRecall(5)
	
	


def create_window():
	# Create a window for the game and open it.
	window = Window("Serial Recall Test", WINDOW_SIZE[0], WINDOW_SIZE[1])
	window.set_bg_color(BG_COLOR)
	window.set_font_color(DEFAULT_FONT_COLOR)
	window.set_font_size(DEFAULT_FONT_SIZE)
	window.set_font_name(DEFAULT_FONT_NAME)
	window.clear()
	window.update()

	return window   

if __name__ == "__main__":
	main()
