import sys

no_of_tries = 5
word = "kamila"

used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []
    
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("Użyte litery:", used_letters)
    print()
    
def reset_of_game():
    restart = input("Czy chcesz zagrać jeszcze raz (y/n): ")
    if restart == str("y"):
        print()
        print("Gramy jeszcze raz")
        no_of_tries = 5
        used_letters.clear()
        user_word.append("_")        
    elif restart == str("n"):
        sys.exit(0)
    else:
        print()
        restart = input("Czy chcesz zagrać jeszcze raz (y/n): ")
        if restart == str("y"):
            print()
            print("Gramy jeszcze raz")
                    
        elif restart == str("n"):
            sys.exit(0)
                    
                    
for letter in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)
    
    found_indexes = find_indexes(word, letter)
    
    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        no_of_tries -= 1
        
        if no_of_tries == 0:
            print("Koniec gry :(")
            reset_of_game()
    else:
        for index in found_indexes:
            user_word[index] = letter
        
        if "".join(user_word) == word:
            print("Brawo wygrałeś! Udało odgadnąć Ci się właściwe słowo.")
            reset_of_game()
                    
    show_state_of_game()
    