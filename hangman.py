from __future__ import print_function
import numpy

# functions below are for creating the hangman person
# for every incorrect letter
def hook():
    print (" -----")
    print (" |   |")
    print (" |    ")
    print (" |    ")
    print (" |    ")
    print (" |    ")
    print ("-----")


def head():
    print (" -----")
    print (" |   |")
    print (" |   0")
    print (" |    ")
    print (" |    ")
    print (" |    ")
    print ("-----")


def body():
    print (" -----")
    print (" |   |")
    print (" |   0")
    print (" |   |")
    print (" |    ")
    print (" |    ")
    print ("-----")


def left_arm():
    print (" -----")
    print (" |   |")
    print (" |   0")
    print (" |  \\|")
    print (" |    ")
    print (" |    ")
    print ("-----")


def right_arm():
    print (" -----")
    print (" |   |")
    print (" |   0")
    print (" |  \\|/")
    print (" |    ")
    print (" |    ")
    print ("-----")


def left_leg():
    print (" -----")
    print (" |   |")
    print (" |   0")
    print (" |  \\|/")
    print (" |  /  ")
    print (" |    ")
    print ("-----")


def right_leg():
    print (" -----")
    print (" |   |")
    print (" |   0")
    print (" |  \\|/")
    print (" |  / \\")
    print (" |    ")
    print ("-----")

print (hook())

# list of words program will choose from
word_list = ["hello", "python", "hangman", "happy"]
blanks_list = [["_ _ _ _ _"], ["_ _ _ _ _ _"], ["_ _ _ _ _ _ _"], ["_ _ _ _ _"]]
word = numpy.random.choice(word_list)
blanks = ""
# empty list for every correct letter guessed by user
correct_letters = [""]

# test
# list = ["a, b, c, d"]
# print (list[0][0:3])
# test

# prints out blanks before user starts guessing
if word == word_list[0]:
    blanks = blanks_list[0][0]
elif word == word_list[1]:
    blanks = blanks_list[1][0]
elif word == word_list[2]:
    blanks = blanks_list[2][0]
elif word == word_list[3]:
    blanks = blanks_list[3][0]

# function used to replace blanks with correct letters
def print_blanks(word_, correct_letters_):
    solved = True
    for letter in word_:
        if letter in correct_letters_:
            print (letter + " ", end="")
        else:
            solved = False
            print ("_ ", end="")
    return solved


print (blanks)

# asks for a letter/guess
guess = raw_input("Guess a letter: ")
guess = guess[0]
# count is for every incorrect letter guessed
count = 0

# while loop to check if guess is correct
while guess != "":
    if guess in word:
        print (guess + " is in the word.")
        correct_letters.append(guess)
        print_blanks(word, correct_letters)
        guess = raw_input("Guess a letter: ")
        guess = guess[0]
# if guess is incorrect
# count variable increases by one and hangman starts printing
    else:
        print (guess + " is not in the word.")
        count += 1
        if count == 1:
            print (head())
            print (print_blanks(word, correct_letters))
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 2:
            print (body())
            print (print_blanks(word, correct_letters))
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 3:
            print (left_arm())
            print (print_blanks(word, correct_letters))
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 4:
            print (right_arm())
            print (print_blanks(word, correct_letters))
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 5:
            print (left_leg())
            print (print_blanks(word, correct_letters))
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 6:
            guess = ""
            correct_letters = [""]
            blanks = ""
            print (right_leg())
            print (print_blanks(word, correct_letters))
            print ("You lost!")
            print ("The word was " + word.upper())
# when count is 6 all of hangman is printed and loop ends