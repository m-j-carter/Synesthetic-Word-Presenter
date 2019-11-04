# This file contains the classes PresentWords and Word, as used in the main timed word presenter program
# Word is its own class (instead of a list of strings) to allow for easy modifications 

# Written By: Michael Carter, Oct. 2019
# For my PSYCO 403/505 research project


from numpy import random
import pygame as pg
from pygame.locals import *
from uagame import Window
from Word import *
from DisplayTimer import *




WORDS_FILENAME = 'words.txt'

WINDOW_SIZE = (700, 500)

DEFAULT_FONT_COLOR = "white"
DEFAULT_FONT_SIZE = 36
BG_COLOR = "gray50"



class PresentWords:
    # This class includes everything required for the word presentation task.
    # word_list is a list of objects of class Word

    @classmethod
    def set_word_lib(cls, word_lib):
        cls.word_lib = word_lib


    def __init__(self, num_words, present_time, delay_time):
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
            
        self.run()



    def run(self):
        # runs the presenter for one word list
        self.__create_window()
        
        self.__display_instructions()     
        self.__display_countdown()
        
        for word in self.__word_list:        
            next = False
            while not self.__quit and not next:
                self.__check_events()
                next = self.__display_next(word)
                self.__window.update()
                

    def __create_window(self):
        # Create a window for the game and open it.
        self.__window = Window("Word Presenter", WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.__clock.tick(60)
        self.__window.set_bg_color(BG_COLOR)
        self.__window.set_font_color(DEFAULT_FONT_COLOR)
        self.__window.clear()
        self.__window.update()
  
        
    def __check_events(self): 
        # handle user inputs
        for event in pg.event.get():
            if event.type == QUIT:
                print("Quitting")
                self.__handle_quit()
            
            if event.type == KEYUP:
                if event.key == pygame.K_SPACE:
                    self.__space_pressed = True
                else: 
                    self.__space_pressed = False        # "flip the switch" back
                    

    def __handle_quit(self):
        self.__quit = True
        #self.__window.close()
        
       
    def generate_rand_word_list(self):
        # Generates the word_list by randomly picking num_words from word_lib.
        for i in range(self.__num_words+1):
            self.__word_list.append(random.choice(PresentWords.word_lib, replace=False))
    
 
 
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
        print("Displaying Blank")
        self.__window.clear()

    def __display_word(self,word):
        print("Displaying Word:",word)
        word.set_window(self.__window)
        word.draw_word()
        
    def __display_instructions(self):
        # Draws each line of each page to the display. 
        # Pages are advanced by a spacebar press.
        self.__window.set_font_color(DEFAULT_FONT_COLOR)
        self.__window.set_font_size(DEFAULT_FONT_SIZE)
        print("Displaying Instructions")
        
        instructions = [ 
            # Page 1
            ["This is a test of word memory.", " ",         
             "%d nouns will be presented for %d seconds at a time,"%(self.__num_words, self.__present_time), 
             "with %d seconds in between."%(self.__delay_time),
             " ", "Press Space to Continue"],
        
            # Page 2
            ["This is page 2 of the instructions display", 
             " ", "Press Space to Continue"],
            
            # Page 3
            ["This is page 3 of the instructions display",      
            " ", "Press Space to Start"] ]
 
 
 
 
        for page in instructions:
            self.__space_pressed = False
            while not self.__space_pressed:
                
                # print each line
                for i, line in enumerate(page):
                    x, y = self.__find_string_x_y(line, i)
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

    def __find_string_x_y(self, print_string, line_no):
        # returns a tuple of the (x,y) position to draw the string at.
        x = (self.__window.get_width() - self.__window.get_string_width(print_string)) // 2
        y = (self.__window.get_height() - self.__window.get_font_height()) // 2 + (self.__window.get_font_height() * line_no)
        
        return (x,y)


class SaveData:
    # represents the modules required to save the results to a .txt file.
    # each trial should be saved as a separate file.
    
    def __init__(self, filename):
        self.__filename = filename
        
        
    def create_file(self):
        pass
        
        
        
    def get_filename(self):
        return self.__filename
    


def main():
    """Tests the Methods"""
    
    word_library = read_words_file(WORDS_FILENAME)
        
    PresentWords.set_word_lib(word_library)
        
    test_1 = PresentWords(4, 5, 2)      # num_words, present_time, delay_time
    
    
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
    