import random

def load_word():
    f = open('/usr/share/dict/words', 'r')
    words_list = f.readlines()
    f.close()

    new_list = []

    for word in words_list:
        new_word = word.strip()
        new_list.append(new_word)

    words_list = new_list

    #words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(new_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

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
    print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
    print("Thank you for choosing to help our Spaceman!")
    print("Lets help the Spaceman find his way home.")
    print("You are allowed to guess 1 letter per round.")
    print("There are " + str(len(secret_word)) + " letters." )
    print("Hurry up and save the Spaceman!")
    print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––\n")

    running = True
    word_guessed = []
    num_guess = 0

    while running == True:
        print("You have " + (str(len(secret_word) - num_guess)) + " guesses left!")
        guess = ""

        while True:
            guess = input("\nPlease input a letter: ")
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("Sorry, that was invalid. Please try again!")
#TODO: Check if the guessed letter is in the secret or not and give the player feedback

        if is_guess_in_word(guess, secret_word_chars):
            print("\n–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
            print("\nNice! You are a step closer to saving our Spaceman!\n")
            word_guessed.append(guess)
        else:
            print("\n–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
            print("\nGood try! Try again\n")
            num_guess += 1

#TODO: show the guessed word so far

        print("Theses are the letters you have guessed so far: ", get_guessed_word(secret_word, word_guessed))

#TODO: check if the game has been won or lost

        if is_word_guessed(secret_word, word_guessed):
            print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
            print("\nYou have guessed the sercet word!\n")
            print("The secret word was: " + secret_word)
            print("\nThank you for helping our Spaceman return home!")
            print("\nYour skills are valuable, would you like to help another Spaceman?\n")
            function_code = input("Accept your mission? (Y/N): ")
            if function_code.upper() == "Y":
                spaceman(load_word())
            else:
                break

        if num_guess == len(secret_word):
            print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
            print("\nOh no! You weren't able to save our Spaceman!")
            print("Thank you for trying, I know the conditions were seve.\n")
            print("The secret word was: " + secret_word)
            print("Your skills are valuable, would you like to help another Spaceman?\n")
            function_code = input("Accept your mission? (Y/N): ")
            if function_code.upper() == "Y":
                spaceman(load_word())
                return True
            else:
                break

#These function calls that will start the game
secret_word = load_word()
secret_word_chars = list(secret_word)
spaceman(secret_word)
