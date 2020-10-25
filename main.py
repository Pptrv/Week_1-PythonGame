import random
MAX_MISSES = 5

def print_welcome():
    print('Welcome to Hangman!')

def print_round_start():
    print('')
    print('------------')

def print_round_finish(correct):
    if correct:
        print('Correct!')
    else:
        print('Shame...')
    print('------------')
    print('')

def print_lives_left(number_of_misses):
    print(f'You have {MAX_MISSES-number_of_misses} lives left...')

def get_input(previous_guesses):
    is_valid = False

    while(is_valid is False):
        guess = input('--> ')
        guess = guess.lower()

        if guess in previous_guesses:
            print("You can't repeat letters!")
        elif len(guess) > 1:
            print("Your guess must be 1 character long!")
        else:
            is_valid = True

    previous_guesses.append(guess)
    return guess, previous_guesses

def get_random_word():
    words = open('dictionary.txt').read().splitlines()
    return random.choice(words).lower()

def main():
    print_welcome()

    number_of_misses = 0
    previous_guesses = []
    guessed_word = ''

    word = get_random_word()

    win_condition = False
    lose_condition = False

    while(not win_condition and not lose_condition):
        print_round_start()
        print_lives_left(number_of_misses)

        guessed_word = ''.join([i if i in previous_guesses else '_' for i in word])
        print(guessed_word.capitalize())

        guess, previous_guesses = get_input(previous_guesses)

        if guess in word:
            is_right_guess = True
            guessed_word = ''.join([i if i in previous_guesses else '_' for i in word])
            win_condition = (guessed_word == word)

        else:
            is_right_guess = False
            number_of_misses += 1
            lose_condition = (number_of_misses >= MAX_MISSES)

        print_round_finish(is_right_guess)

    if win_condition:
        print('YOU WIN!')
    else:
        print('YOU LOSE!')

main()
