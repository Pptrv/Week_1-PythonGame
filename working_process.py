# Hangman - Captain John Long Silver
""" First collection of words
    Main* 
        - read from file (collection of words)
        - select random word
        - Iniciar partida
        - Read input 
        - Evaluate input
        - update hangman drawing 
        - repeat select random word or end game 
"""

# Imports
import os
import random

# Read from file and select random word 

def get_random_word():
    """Reads from file and selects random word"""
    words = open('dictionary.txt').read().splitlines()
    return random.choice(words)

# Get input from player
def get_input(previous_guesses):
    guess = input('Next letter -->')
    while guess in previous_guesses:
        print("You can't repeat letters!")
        guess = input('Next letter -->')
    return guess, previous_guesses


# Game execution
def print_welcome():
    print ("Welcome to Captain John Long Silver's Hangman Game")
    print ("You must try and figure out the missing word, or you will suffer the terrible consecuences of death")
    print ("Pick a letter, but if you pick the wrong one, remember you only allowed 5 misses ")
    
MAX_MISSES = 5


# Main

def main():
    print_welcome()

    number_of_misses = 0
    previous_guesses = []
    guessed_word = ''

    word = get_random_word()
    guessed_word = ""

    while (number_of_misses <= MAX_MISSES) and (guessed_word != word):
        guessed_word = ''.join([i if i in previous_guesses else '_' for i in word])
        print(guessed_word)

        guess, previous_guesses = get_input(previous_guesses)

        previous_guesses.append(guess)

        if guess in word:  
            guessed_word = ''.join([i if i in previous_guesses else '_' for i in word])
            print("Correct!")
        else:
            number_of_misses += 1
            print("Shame...")


    # Game looser
    if (number_of_misses > MAX_MISSES):
        print "Pirate Captain Long John Silver is dead, and its your fault!"

    # Game winner 
    if (guessed_word == word):
        print "Congrats pirate, you saved Captain John Long Silver"

main()