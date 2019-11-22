
## Written By: Michael Carter, Oct./Nov. 2019
## For my PSYCO 403/505 research project

## Notes/Changelog: 
##   - changing so that individual letters are colored, as opposed to the entire word
##     being colored by the first letter.  


import pygame

DEFAULT_FONT_COLOR = 'white'
DEFAULT_FONT_SIZE = 72
DEFAULT_FONT_NAME = 'arial'

pygame.init()

class Word:
    """ Represents a Word object, where each letter is assigned a corresponding colour,
        as stated in SYN_COLORS. draw_word() can be called with the boolean attribute
        is_colored, which draws it with either those colors or the DEFAULT_FONT_COLOR.
    """

    """
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
    """    

    SYN_COLORS = {
        "A":"red",
        "B":"blue",
        "E":"green",
        "G":"green",
        "L":"yellow",
        "N":"orange",
        "Y":"yellow"
    }

    @classmethod
    def set_window(cls,window_from_parent):
        cls.window = window_from_parent


    def __init__(self, word):
        self.word = word
        self.letter_colors = [DEFAULT_FONT_COLOR] * len(word)
        self.__generate_color()

    def __str__(self):
        return str(self.word)

    def __repr__(self):
        return str(self.word)    

    def __generate_color(self):
        # generates and assigns the synesthetic color for each letter in the word.
        for i in range(len(self.word)):
            temp = Word.SYN_COLORS.get(str(self.word[i]).upper())
            if temp:
                self.letter_colors[i] = Word.SYN_COLORS.get(str(self.word[i]).upper())     


    def draw_word(self, is_colored=False):
        # draws the word to the display using modules in the uagame library.
        Word.window.set_font_name(DEFAULT_FONT_NAME)
        Word.window.set_font_size(DEFAULT_FONT_SIZE)


        y = (Word.window.get_height() - Word.window.get_font_height()) // 2     
        for i in range(len(self.word)):
            x = (Word.window.get_width() - Word.window.get_string_width(self.word)) // 2 + Word.window.get_string_width(self.word[:i])
            self.__draw_indexed_letter(i, x, y, is_colored)


    def __draw_indexed_letter(self, index, x, y, is_colored):
        # draws either a colored or uncolored letter, depending on is_colored.
        if is_colored:
            Word.window.set_font_color(self.letter_colors[index])   
        else:
            Word.window.set_font_color(DEFAULT_FONT_COLOR)   

        Word.window.draw_string(self.word[index], x, y)

