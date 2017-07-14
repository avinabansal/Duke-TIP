from __future__ import print_function
import numpy


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


word_list = ["hello", "python", "hangman", "happy"]
blanks_list = [["__ __ __ __ __"], ["__ __ __ __ __ __"], ["__ __ __ __ __ __ __"], ["__ __ __ __ __"]]
word = numpy.random.choice(word_list)
blanks = ""

# test
# list = ["a, b, c, d"]
# print (list[0][0:3])
# test

if word == word_list[0]:
    blanks = blanks_list[0][0]
elif word == word_list[1]:
    blanks = blanks_list[1][0]
elif word == word_list[2]:
    blanks = blanks_list[2][0]
elif word == word_list[3]:
    blanks = blanks_list[3][0]

print (blanks)

guess = raw_input("Guess a letter: ")
guess = guess[0]
correct_letters = [""]
count = 0

while guess != "":
    if guess in word:
        print (guess + " is in the word.")
        correct_letters.append(guess)
        print(hook())
        print (blanks)
        guess = raw_input("Guess a letter: ")
        guess = guess[0]
    else:
        print (guess + " is not in the word.")
        count += 1
        if count == 1:
            print (head())
            print (blanks)
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 2:
            print (body())
            print (blanks)
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 3:
            print (left_arm())
            print (blanks)
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 4:
            print (right_arm())
            print (blanks)
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 5:
            print (left_leg())
            print (blanks)
            guess = raw_input("Guess a letter: ")
            guess = guess[0]
        elif count == 6:
            guess = ""
            correct_letters = [""]
            blanks = ""
            print (right_leg())
            print (blanks)
            print ("You lost!")
            print ("The word was " + word.upper())
