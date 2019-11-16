## This file contains the class PresentWords, as used in the main timed word presenter program.
## Word is its own class (instead of a list of strings) to allow for easy modifications 

## Written By: Michael Carter, Oct./Nov. 2019
## For my PSYCO 403/505 research project


from numpy import random
import pygame as pg
from pygame.locals import *

from uagame import Window
from word import Word
import time
from results import ResultsFile


## TEST PARAMETERS ##
WORDS_FILENAME = 'testwords.txt'
WINDOW_SIZE = (700, 500)
DEFAULT_FONT_COLOR = "gray"
DEFAULT_FONT_SIZE = 36
DEFAULT_FONT_NAME = "Arial"
BG_COLOR = "gray50"


class PresentWords:
    """
    This class includes everything required for a single word presentation task.
    word_list is a list of objects of class Word.
    """
    @classmethod
    def set_word_lib(cls, word_lib):
        cls.word_lib = word_lib    
    @classmethod
    def set_window(cls, window_from_parent):
        cls.window = window_from_parent
    @classmethod
    def set_results_file(cls, results_file):
        cls.results = results_file

    def __init__(self, num_words, present_time, delay_time, is_colored=False):
        self.__is_colored = is_colored
        self.__present_time = present_time
        self.__delay_time = delay_time
        self.__num_words = num_words
        
        self.__word_list = []
        self.__quit = False
        self.__space_pressed = False
        
        self.__clock = pg.time.Clock()
        self.__timer_wd = DisplayTimer()
        self.__timer_bl = DisplayTimer()

        self.generate_rand_word_list()
        self.__window = PresentWords.window
        
        self.__write_to_results()            
        self.run()

    def run(self):
        # runs the presenter for one word list
        self.__initialize_window()
        self.__display_instructions()     
        self.__display_countdown()
        
        self.__timer_bl.reset()
        self.__timer_wd.reset()
        
        for word in self.__word_list:        
            next = False
            while not self.__quit and not next:
                self.__check_events()
                next = self.__display_next(word)
                self.__window.update()
                self.__clock.tick(30)

    def __initialize_window(self):
        # sets all the window's parameters to the ones relevant to the class.
        self.__clock.tick(30)
        self.__window.set_bg_color(BG_COLOR)
        self.__window.set_font_color(DEFAULT_FONT_COLOR)
        self.__window.clear()
        self.__window.update()
  
    def __write_to_results(self):
        # writes the info to the header of the results file
        PresentWords.results.new_trial_header(self.__word_list, 
                                              self.__present_time, 
                                              self.__delay_time, 
                                              self.__is_colored)
  
    def __check_events(self): 
        # handle user inputs
        for event in pg.event.get():
            if event.type == QUIT:
                self.__handle_quit()
            
            if event.type == KEYUP:
                if event.key == pg.K_SPACE:
                    self.__space_pressed = True
                else: 
                    self.__space_pressed = False        # "flip the switch" back

    def __handle_quit(self):
        self.__quit = True
        
        #self.__window.close()
       
    def generate_rand_word_list(self):
        # Generates the word_list by randomly picking num_words from word_lib.
        try:
            for i in range(self.__num_words):
                r = random.randint(0, len(PresentWords.word_lib))
                self.__word_list.append(PresentWords.word_lib.pop(r))
                #self.__word_list.append(random.choice(PresentWords.word_lib, replace=False)) 
        except ValueError:
            print("Value Error: Insufficient words given") 
 
    def __display_next(self,word):
        # displays the next word for present_time, followed by a blank screen for delay_time 
        if not self.__timer_wd.been_longer_than(self.__present_time):
            self.__display_word(word)
            self.__timer_bl.reset()
        else:
            self.__display_blank()  
            if self.__timer_bl.been_longer_than(self.__delay_time):
                self.__timer_wd.reset()
                return True
        return False

    def __display_blank(self):
        self.__window.clear()

    def __display_word(self,word):
        word.set_window(self.__window)
        word.draw_word(self.__is_colored)
        
    def __display_instructions(self):
        # Draws each line of each page to the display. 
        # Pages are advanced by a spacebar press.
        self.__window.set_font_color(DEFAULT_FONT_COLOR)
        self.__window.set_font_size(DEFAULT_FONT_SIZE)
        print("Displaying Presentation Instructions")
        
        instructions = [ 
            # Page 1
            ["This is a test of word memory.", " ",         
             "%d concrete nouns will be presented" % (self.__num_words), 
             "for %d second(s) at a time," % (self.__present_time),
             "with %d second(s) in between." % (self.__delay_time),
             " ", "Press Space to Continue"],
            # Page 2
            ["Afterwards, you will be prompted",
             "to recall the words in order.", 
             " ", "Press Space to Continue"],
            # Page 3
            ["Press Space to Start"] ]
 
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
            self.__window.clear()                

    def __display_countdown(self):
        # currently just uses the time.sleep() method for the delay, 
        # since it's not that big of a deal.
        countdown = ["3...","2...","1..."]
        for count_str in countdown:
            x,y = self.__find_string_x_y(count_str, 0)
            self.__window.draw_string(count_str, x, y)
            time.sleep(1)
            self.__window.clear()

    def __find_string_x_y(self, print_string, line_no, total_lines=1):
        # returns a tuple of the (x,y) position to draw the string at.
        x = (self.__window.get_width() - self.__window.get_string_width(print_string)) // 2
        y = ((self.__window.get_height() - (self.__window.get_font_height() * total_lines+1))  // 2) + (self.__window.get_font_height() * line_no)
        return (x,y)
    
class DisplayTimer:
    """ 
    This class allows the events to be timed,
    to make decisions as to whether or not to progress.
    """ 
    def __init__(self):
        self.__time_init = time.time()      # current time in fractional seconds

    def reset(self):
        self.__time_init = time.time()

    def been_longer_than(self, check_seconds):
        # returns true if the timer has exceeded the check time.
        time_now = time.time()
        if self.__time_init < (time_now - check_seconds):
            return True
        else:
            return False 

def main():
    """Tests the Methods"""
    
    window = create_window()
    
    word_library = read_words_file(WORDS_FILENAME)
    PresentWords.set_word_lib(word_library) 
    PresentWords.set_window(window) 
    
    results_file = ResultsFile()    
    PresentWords.set_results_file(results_file)
    
    # Present Words
    #test_1 = PresentWords(4, 5, 2, False)      # (num_words, present_time, delay_time, is_colored (bool))
    test_2 = PresentWords(5, 3, 1, True)    
    
def create_window():
    # Create a window for the game and open it.
    window = Window("Word Presenter", WINDOW_SIZE[0], WINDOW_SIZE[1])
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
    