import random
MAX_MISSES = 5

def print_welcome():
    # Mensaje de Inicio e instrucciones
    print('')
    print('')
    print('')
    print('Welcome to John Long Silver Hangman Game!')
    print('Guess the word missing in the blank spaces')

def print_round_start():
    # Separador para el inicio de partida. 
    print('')
    print('---------------------------------------------------------------')

def print_round_finish(correct):
    # Recoge el input en caso de no darse las condiciones para ganar o perder el juego, para mostrar si hemos acertado o no la palabra. 

    if correct:
        print('Correct!')
    else:
        print('Shame...')
    print('---------------------------------------------------------------')
    print('')

def print_lives_left(number_of_misses):
    # Entra el input de "MAX_MISSES" menos "number_of_misses", se printea el numero de vidas restantes. 
    print(f'You have {MAX_MISSES-number_of_misses} lives left...')

def get_input(previous_guesses):
    # Mientras la lista de "previous_guesses" no tenga todas las letras de "word" el loop continua y sigue pidiendo un input ("guess") que se añade a la lista "previous_gusses". 
    # El input se transforma en minusculas para poder comparar con "word". 
    # El input solo acepta 1 letra, en caso de ser más de una, sale un aviso y no te quitan vidas.

    is_valid = False

    while(is_valid is False):
        guess = input('letter: ')
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
    # Selecciona una palabra del diccionario de piratas y la devuelve en letras minusculas. 
    words = open('dictionary.txt').read().splitlines()
    return random.choice(words).lower()

def main():
    # Funcion en loop para llamar al juego mientras no ganemos o perdamos. 

    print_welcome()

    number_of_misses = 0
    previous_guesses = []
    guessed_word = ''

    word = get_random_word()

    win_condition = False
    lose_condition = False

    while(not win_condition and not lose_condition):
        # Al asignar las variables como falsas, hasta que alguna de las dos condicioens no se cumpla, el juego continua. 
        print_round_start()
        # Printea un separador.
        print_lives_left(number_of_misses)
        # Entra el input de "MAX MISSES" menos "number_of_misses", se printea el numero de vidas restantes. 

        guessed_word = ''.join([i if i in previous_guesses else '_' for i in word])
        # Se crea una string de la lista de "previous_guesses" y espacios '_' para el resto de letras que siguen sin acertarse en la variable "word".
        print(guessed_word.capitalize())
        # Imprimimos la primera letra de "gussed_word" en mayusculas. 

        guess, previous_guesses = get_input(previous_guesses)


        if guess in word:
            # Mientras "guessed_word != word el win_condition no se printea True y el juego continua.
            is_right_guess = True
            guessed_word = ''.join([i if i in previous_guesses else '_' for i in word])
            win_condition = (guessed_word == word)

        else:
            # Mientras "lose_contidion" no sea true, loop continua y se resta una vida. 
            is_right_guess = False
            number_of_misses += 1
            lose_condition = (number_of_misses >= MAX_MISSES)

        print_round_finish(is_right_guess)
        # La ronda continua, printeando si han acertado o fallado

    if win_condition:
        print('YOU WIN!')
    else:
        print('YOU LOSE!')

main()
