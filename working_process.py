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

#Read from file and select random word 

def get_random_word():
"Reads from file and selects random word"
    words = open('dictionary.txt').read().splitlines()
    return random.choice(words)

# Get input from player
def get_input(previous_guesses):
    guess = input ('Next letter -->')
    while guess in previous_guesses:
        print("You can´t repeat letters!")
        guess = input ('Next letter -->')
    return(guess)


#Game execution
def print_welcome():
    print ("Welcome to Captain John Long Silver´s Hangman")
    print (" instrucciones del juego")
    
    
MAX_MISSES = 5

# Main

def main():
    print_welcome()

    number_of_misses = 0
    previous_guesses = []

    word = get_random_word()
    guessed_word = ""

    while (number_of_misses < MAX_MISSES) and (guessed_word != word):
        guess = get_input(previous_guesses)

        previous_guesses.append(guess)

            if guess in word: 
                guessed_word = "" #hay que construir una palabra con los espacios que nos se hayan definido. 
                print("Correct!")
            else:
                number_of_misses += 1
                print("Shame...")

#Evaluate Guess