
# Written By: Michael Carter, Oct./Nov. 2019
# For my PSYCO 403/505 research project

import pygame


DEFAULT_FONT_COLOR = "gray"
DEFAULT_FONT_SIZE = 72
DEFAULT_FONT_NAME = 'arial'

pygame.init()

class Word:

    SYN_COLORS = {
        # Based on the modal results from Witthoft, Winawer, and Eagleman (2015)
        "A":"red",
        "B":"blue",
        "C":"yellow",
        "D":"blue",
        "E":"green",
        "F":"green",
        "G":"green",
        "H":"orange",
        "I":"white",
        "J":"orange",
        "K":"orange",
        "L":"yellow",
        "M":"red",
        "N":"orange",
        "O":"white",
        "P":"purple",
        "Q":"purple",
        "R":"red",
        "S":"yellow",
        "T":"blue",
        "U":"orange",
        "V":"purple",
        "W":"blue",
        "X":"black",
        "Y":"yellow",
        "Z":"black",
    }
    
    @classmethod
    def set_window(cls,window_from_parent):
        cls.window = window_from_parent
        
        
    def __init__(self, word):
        self.word = word
        self.color_str = DEFAULT_FONT_COLOR
        
        self.__generate_color()
        
    def __str__(self):
        return str(self.word)
    
    def __repr__(self):
        return str(self.word)    

    def __generate_color(self):
        # generates and assigns the synesthetic color to a word according to its first letter.
        # might get moved to a separate class (Synesthete), to open up more possibilities. 
        self.color_str = Word.SYN_COLORS.get(str(self.word[0]).upper())        
        
    def draw_word(self, is_colored=False):
        # draws the word to the display using modules in the uagame library.
        Word.window.set_font_name(DEFAULT_FONT_NAME)
        Word.window.set_font_size(DEFAULT_FONT_SIZE)
        if is_colored:
            Word.window.set_font_color(self.color_str)   
        else:
            Word.window.set_font_color(DEFAULT_FONT_COLOR)
        
        x = (Word.window.get_width() - Word.window.get_string_width(self.word)) // 2
        y = (Word.window.get_height() - Word.window.get_font_height()) // 2     
      
        Word.window.draw_string(self.word, x, y)
    
