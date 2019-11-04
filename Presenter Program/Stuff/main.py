# This file handles the entire task for one participant.
#
# For my PSYCO 403/505 research projects
# Written By: Michael Carter, Oct. 2019




def main():
	"""Tests the Methods"""
	in_list = ["wordA", "wordB", "wordC", "wordD", "wordE", "wordF", 
               "wordG", "wordH", "wordI","wordJ", "wordK", "wordL", "wordM"]
	word_list = []
	for word in in_list:
		word_list.append(Word(word))

	test = PresentWords(4, 5, 2, word_list)