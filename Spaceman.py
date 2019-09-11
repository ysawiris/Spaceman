import random

num_guess = 8

def load_word():
    f = open('/usr/share/dict/words', 'r')
    words_list = f.readlines()
    f.close()

    #words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    return secret_word == letters_guessed

def get_guessed_word(secret_word, letters_guessed):
    word_guessed = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_guessed += (letter + " ")
        else:
            word_guessed += ("_ ")
    return word_guessed

def is_guess_in_word(guess, secret_word):
    return guess in secret_word

def spaceman(secret_word):
    print("Thank you for choosing to help our Spaceman!")
    print("Lets help the Spaceman find his way home.")
    print("You are allowed to guess 1 letter per round.")
    print("There are " + str(len(secret_word)) + " letters." )
    print("Hurry up and save the Spaceman!")

    running = True
    word_guessed = []
    num_guess = 0

    while running == True:
        print("You have " + (str(7 - num_guess)) + " guesses left!")
        guess = ""

        while True:
            guess = input("Please input a letter: ")
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("Sorry, that was invalid. Please try again!")
#TODO: Check if the guessed letter is in the secret or not and give the player feedback

        if is_guess_in_word(guess, secret_word_chars):
            print("Nice! You are a step closer to saving our Spaceman!")
            word_guessed.append(guess)
        else:
            print("Good try! Try again")
            num_guess += 1

#TODO: show the guessed word so far

        print("Theses are the letters you have guessed so far: ", get_guessed_word(secret_word, word_guessed))

#TODO: check if the game has been won or lost

        if is_word_guessed(secret_word_chars, word_guessed):
            print("You have guessed the sercet word!")
            print("Thank you for helping our Spaceman return home!")
            print("\nYour skills are valuable, would you like to help another Spaceman?\n")
            function_code = input("Accept your mission? (Y/N): ")
            if function_code.upper() == "Y":
                spaceman(load_word)
            else:
                break

        if num_guess == 7:
            print("Oh no! You weren't able to save our Spaceman!")
            print("Thank you for trying, I know the conditions were sereve.")
            print("The secret word was: " + secret_word)
            print("\nYour skills are valuable, would you like to help another Spaceman?\n")
            function_code = input("Accept your mission? (Y/N): ")
            if function_code.upper() == "Y":
                spaceman(load_word)
                return True
            else:
                break




#These function calls that will start the game
secret_word = load_word()
secret_word_chars = list(secret_word)
spaceman(secret_word)
