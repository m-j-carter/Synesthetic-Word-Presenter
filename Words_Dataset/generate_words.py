## Used to create the words list

## Created by: Michael Carter, Nov. 2019
## For PSYCO 403/505


def main():

    words_in_range = []
    words_zero_syn = []
    words_one_syn = []
    words_two_syn = []
    words_three_syn = []    
    word_list = read_words_file('concrete_nouns.txt')
    for word in word_list:
        if 7 <= len(word) <= 9 and not ' ' in word:
            words_in_range.append(word)
    for word in words_in_range:
        i=0
        ltrs = []        
        # count how many synesthetic letters are in the word
        for ch in word:
            if ch.upper() in ('A','B','E','G','L','N','Y'):
                i+=1    
                #ltrs.append(ch)
        if i==0:
            words_zero_syn.append(word)
        elif i==1:
            words_one_syn.append(word)
        elif i==2:
            words_two_syn.append(word)
        elif i==3:
            #print(word, i, ltrs)
            words_three_syn.append(word)
        else:
            # exclude any words with > 3 syn. letters
            words_in_range.remove(word)

    #save_as('cn_7-9_letters.txt', words_in_range)
    save_as('words.txt', words_in_range)
    save_as('words_0_syn.txt', words_zero_syn)
    save_as('words_1_syn.txt', words_one_syn)
    save_as('words_2_syn.txt', words_two_syn)
    save_as('words_3_syn.txt', words_three_syn)



def save_as(filename, word_list):
    # saves to file, writing from the first line (will overwrite data). 
    try:		
        with open(filename,'w') as file:
            for word in word_list:
                file.write(word + "\n")
        assert len(word_list) > 0, "word list cannot be empty"
    except FileNotFoundError as e:
        print('Error: File not found! %s' % (e.strerror))
        return
    else:		
        return word_list

def read_words_file(filename):
    # Read in the list of possible words.
    # Returns a list of objects of the Word class.
    try:		
        with open(filename,'r') as file:
            word_list = file.read().splitlines()
            assert len(word_list) > 0, "word list cannot be empty"
    except FileNotFoundError as e:
        print('Error: File not found! %s' % (e.strerror))
        return
    else:		
        return word_list



main()
