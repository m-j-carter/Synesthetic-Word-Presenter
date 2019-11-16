## This file contains the classes PresentWords and Word, as used in the main timed word presenter program
## Word is its own class (instead of a list of strings) to allow for easy modifications 

## Written By: Michael Carter, Oct./Nov. 2019
## For my PSYCO 403/505 research project


## Notes/Changelog:
##   - Still kinda want a countdown timer displayed.
##   - Still having issues with the text input. 
##       Works fine until you try to return to a previous input box, 
##       then it starts to fall apart.
##   - At some point I should merge all the duplicate methods between SerialRecall
##       and PresentWords into a single utilities module.
##   - Should also move the instructions out of the individual modules.

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
LINE_SPACING = 5
HEADER_SPACING = 25
LINE_COLOR = (55,55,55)


class SerialRecall:
	""" This class represents the serial recall sheet.
	        Utilizes Nearoo's pygame text input module: 
	        https://github.com/Nearoo/pygame-text-input
	"""

	@classmethod
	def set_window(cls, window_from_parent):
		cls.window = window_from_parent
	@classmethod
	def set_results_file(cls, results_file):
		cls.results = results_file    


	def __init__(self, num_words, timer_mins):
		self.__clock = pg.time.Clock()
		self.__num_words = num_words
		self.__window = SerialRecall.window
		self.__results = SerialRecall.results
		self.__text_inputs_list = []
		self.__row_index = 0
		self.__first_row_index = 0
		self.__last_row_index = 8
		self.__current_input = None
		self.__quit = False
		self.__finished = False
		
		self.__timer_mins = timer_mins			# in minutes
		self.__time_limit = None 			# in seconds (Epoch time)
		self.__initial_time = None		
		self.__start_times = [None] * num_words		# Initialize as a list of null values
		self.__end_times = [None] * num_words
		
		self.__window.set_auto_update(False)
		self.__create_text_inputs()
		self.__run()

	def __create_text_inputs(self):
		for i in range(0, self.__num_words):
			self.__text_inputs_list.append(
			                pygame_textinput.TextInput(
			                        initial_string="",
			                        font_family=DEFAULT_FONT_NAME,
			                        font_size=math.floor(DEFAULT_FONT_SIZE*1.0),
			                        text_color=(255, 255, 255),
			                        cursor_color=(200, 200, 200),
			                        repeat_keys_initial_ms=300,
			                        repeat_keys_interval_ms=50))
		self.__current_input = self.__text_inputs_list[self.__row_index]

	
	def __run(self):
		# handles one entire iteration of the SerialRecall class.
		self.__initialize_window()
		self.__display_instructions()
		
		self.__initial_time = time.time()
		self.__time_limit = self.__initial_time + (self.__timer_mins * 60) 
		
		while not self.__quit and not self.__finished:
			self.__window.clear()									
			self.__check_events()
			self.__update_current_input()
			self.__draw_window()
			self.__window.update()
			self.__clock.tick(30)		
			
			if not self.__is_time_remaining():
				self.__finished = True
				self.__display_times_up()

		self.__write_results()

	def __initialize_window(self):
		# sets all the window's parameters to the ones relevant to the class.
		self.__clock.tick(30)
		self.__window.set_bg_color(BG_COLOR)
		self.__window.set_font_color(DEFAULT_FONT_COLOR)
		self.__window.clear()
		self.__window.update()

	def __write_results(self):
		# writes the results (entry, start_time, end_time) for each word
		#   to the results file.
		self.__results.new_results_header(self.__timer_mins)
		for i in range(self.__num_words):
			try:
				# try to write the human-readable times 
				self.__results.write_result(
				                self.__text_inputs_list[i].get_text(),
				                self.__start_times[i] - self.__initial_time,
				                self.__end_times[i] - self.__initial_time)
			except TypeError:
				# but if they're NoneTypes, just print "None"
				self.__results.write_result(
				                self.__text_inputs_list[i].get_text(),
				                self.__start_times[i],
				                self.__end_times[i])				

	def __update_current_input(self):
		self.__current_input = self.__text_inputs_list[self.__row_index]
		self.__current_input.update(self.__events)        # feed textinput any events




	def __draw_window(self):
		# draw the window by drawing the header, then dynamically 
		#   displaying the list of words so it can be scrolled through.
		
		self.__window.draw_string("Words remaining: %d"%(self.__count_remaining_words()), 10, 0)
		
		# draw the scroll arrows
		if self.__first_row_index > 0:
			self.__window.draw_string("^ ^ ^", 50, DEFAULT_FONT_SIZE)
		if self.__last_row_index < self.__num_words - 1:
			y = (DEFAULT_FONT_SIZE + LINE_SPACING) * (self.__num_words + 1) + HEADER_SPACING
			self.__window.draw_string("v v v", 50, y)
			
		# draw the rows
		for i in range(self.__first_row_index, self.__last_row_index):
			if i < self.__num_words:
				y = (DEFAULT_FONT_SIZE + LINE_SPACING) * (i+1) + HEADER_SPACING		
				# draw the index number
				self.__window.draw_string("%d:"%(i+1), 5, y)
				# draw the text
				self.__draw_text_line(i, 50, y)	
	
	def __draw_text_line(self, i, x_pos, y_pos):		
		# draw a single line of text.		
		if self.__row_index == i:
			# draw the text as currently being entered
			self.__window.get_surface().blit(
			        self.__current_input.get_surface(), 
			        (x_pos, y_pos))
		else:
			# draw the entered text
			self.__window.draw_string(self.__text_inputs_list[i].get_text(), x_pos, y_pos)	


	def __check_events(self): 
		# handle user inputs
		self.__events = pg.event.get()
		for event in self.__events:
			if event.type == QUIT:
				self.__handle_quit()
			if event.type == KEYUP:
				#self.__update_current_input()	
				self.__handle_keypress(event.key)
				if event.key in range(pg.K_a, pg.K_z): 
					self.__update_timer()	
				if event.key == pg.K_SPACE:
					self.__space_pressed = True
				else: 
					self.__space_pressed = False        # "flip the switch" back				
	
	
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
		self.__update_current_input()

	def __handle_key_down(self):
		# advance to the next row or end input
		if self.__row_index < self.__num_words - 1:
			self.__row_index += 1
			self.__update_current_input()
	
	def __count_remaining_words(self):
		# returns an integer of the number of words for which the value is null
		words_remaining = self.__num_words
		i = 0
		while i < self.__num_words:
			word = self.__text_inputs_list[i].get_text()
			if len(word) > 0: 
				words_remaining -= 1
			i += 1
		return words_remaining

	def __update_timer(self):
		# Update the current row's end-timer. 
		# If the row is new, set its start-timer as well.
		# Called every time a letter from A-Z is entered.
		if self.__start_times[self.__row_index] == None:
			self.__start_times[self.__row_index] = time.time()
		else:
			self.__end_times[self.__row_index] = time.time()
		
	
	def __is_time_remaining(self):
		# returns True if there is still time remaining, false if not. 
		return time.time() < self.__time_limit
	

	def __display_instructions(self):
		# Draws each line of each page to the display. 
		# Pages are advanced by a spacebar press.
		self.__window.set_font_color(DEFAULT_FONT_COLOR)
		self.__window.set_font_size(DEFAULT_FONT_SIZE)
		print("Displaying Recall Instructions")

		instructions = [ 
		        # Page 1
		        ["You will have %.1f minute(s) to recall" % (self.__timer_mins),
		         "as many words as possible.",
		         " ", "Press Space to Continue"],
		        # Page 2
		        ["Try to list the words in the same",
		         "order as presented, leaving rows",
		         "blank if necessary.",
		         " ", "Press Space to Continue"],
		        # Page 3
		        ["Use the Up/Down arrow keys to change",
		         "rows, then press Enter when complete.",
		         " ", "Press Space to Start"] ]

		for i, page in enumerate(instructions):
			self.__space_pressed = False
			while not self.__space_pressed:
				# draw the page counter
				counter = "%d/%d" % (i+1, len(instructions))
				self.__window.draw_string(counter, 
				                          self.__window.get_width() - self.__window.get_string_width(counter),
				                          self.__window.get_height() - self.__window.get_font_height())
				# draw each line
				for j, line in enumerate(page):
					x, y = self.__find_string_x_y(line, j, len(page))
					self.__window.draw_string(line, x, y)

				self.__check_events() 
				self.__window.update()
			self.__window.clear()     	

	def __display_times_up(self):
		self.__window.set_font_color(DEFAULT_FONT_COLOR)
		self.__window.set_font_size(DEFAULT_FONT_SIZE)
		print("Displaying Time's Up")
	
		page = [ "Time's Up!",
		         "Press any key to exit" ]
	
		while True:
			self.__events = pg.event.get()			
			for event in self.__events:
				if event.type == QUIT:
					self.__handle_quit()
				if event.type == KEYUP:
					return
			
			# draw each line
			for j, line in enumerate(page):
				x, y = self.__find_string_x_y(line, j, len(page))
				self.__window.draw_string(line, x, y)

			self.__window.update()
			self.__window.clear()     	
		
		
		
		

def main():
	"""Tests the Methods"""

	window = create_window()
	SerialRecall.set_window(window)	

	test_results = ResultsFile()
	SerialRecall.set_results_file(test_results)

	SerialRecall(5, 0.5)

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
