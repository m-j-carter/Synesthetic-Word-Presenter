# Synesthetic-Word-Presenter
Word presentation program for assessing the effects of trained pseudo-synesthesia on serial recall.

All modules were created by Michael Carter, unless otherwise specified.


# Components:
## Presenter_Program
A program written in Python using PyGame that handles the presentation and data collection for the serial recall task.
**words.txt** contains the set of all words which can be randomly selected.
**main.py** handles the entire task by first running **presentwords.py** to present the words, then running **serialrecall.py** to provide the participant with a form in which to recall the word sequence. 
**results.py** saves a file named "resultsXYZ", where XYZ is a sequence of three randomized digits. The file includes the word list presented to the participant as well as their responses, including the response time for each word (denoted by the time of the first keypress and the time of the last keypress). 
The program utilizes Silas Gyger's [pygame_textinput module]( https://github.com/Nearoo/pygame-text-input) for the participant's inputs during the recall phase.

## Colored_Words
A set of modules including an MS Word Template and a VBA-Word script that simulates grapheme-color synesthesia by transcribing text into their synesthetic colors. 
Grapheme-color pairings are based on Witthoft, Winawer, and Eagleman's (2015) modal results from the survey of 6588 individuals with grapheme-color synesthesia.
VBA scripts are inspired by Olympia Colizoli and Nick Daems's [reading_in_color package](https://github.com/colizoli/reading_in_color)

**ColoredWords** colors the entire word according to the first letter. 
**ColoredLetters** colors each letter separately.
**ColoredLettersTraining** colors the specified 7 letters for the training task. 

## Words_Dataset 
includes everything required to create the **words.txt** file.
