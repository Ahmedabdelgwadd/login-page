import random
import string
from colorama import Fore

words = ["Messi", "Cristiano", "Xavi", "Iniesta", "Ibrahimovic", "Pirlo", "Aguero","abotrukia", "Salah", "test test", "test-test"]

def random_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def guess_the_word():
    word = random_word()
    word_letters = list(word)
    user_input = []
    alphabet = set(string.ascii_uppercase)

    while len(word_letters) > 0:
        print(f"{Fore.CYAN}#-#-#-#-#-#-#-#-#-#-#-#-#-")
        print("Guess a foot ball player name!")
        dashs = [letter if letter in user_input else '-' for letter in word]
        print("Guessed word: ", " ".join(dashs))
        print("Letters you have used: ", " ".join(user_input))
        user_input_letter = input("Guess a letter: ").upper()

        if user_input_letter in alphabet:
            if user_input_letter in word_letters:
                letter_counter = word_letters.count(user_input_letter)
                if letter_counter > 1:
                    for i in range(letter_counter):
                        user_input.append(user_input_letter)
                        word_letters.remove(user_input_letter)
                else:
                    user_input.append(user_input_letter)
                    word_letters.remove(user_input_letter)
            else:
                print("#-#-#-#-#-#-#-#-#-#-#-#-#-")
                print(f"{Fore.RED}WRONG! , Guess another letter")
                user_input.append(user_input_letter)
                continue
        else:
            print("#-#-#-#-#-#-#-#-#-#-#-#-#-")
            print(f"{Fore.RED}Only English letters are allowed!!")


    print(Fore.GREEN + f"you won!, the player name is {word}")
    print('''
            ▓██   ██▓ ▒█████   █    ██     █     █░ ▒█████   ███▄    █
             ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▒██▒  ██▒ ██ ▀█   █
              ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██░  ██▒▓██  ▀█ ██▒
              ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ▒██   ██░▓██▒  ▐▌██▒
              ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░ ████▓▒░▒██░   ▓██░
               ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒
             ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░    ░ ▒ ▒░ ░ ░░   ░ ▒░
             ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░  ░ ░ ░ ▒     ░   ░ ░
             ░ ░         ░ ░     ░            ░        ░ ░           ░
             ░ ░
            ''')


guess_the_word()
