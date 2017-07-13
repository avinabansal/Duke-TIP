from __future__ import print_function
import numpy

print (" -----")
print (" |   |")
print (" |    ")
print (" |    ")
print (" |    ")
print (" |    ")
print ("-----")

word_list = ["hello"]
word = numpy.random.choice(word_list)
blanks = ""
for letter in word:
    blanks += "__ "
print (blanks)

def ask_guess():
    guess = raw_input("Guess a letter: ")
    guess = guess[0]

if guess in word:
    print (guess + " is in the word.")