import sys
import random
import string

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left
    global password_length
    
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znaków spoza przedziału 0,", password_length)
        reset = str(input("Potwierdź otrzymanie wiadomości (y/n) i zresetuj aplikacje: "))
        if reset == "y":
            sys.exit(0)
        else:
            reset2 = str(input("Potwierdź otrzymanie wiadomości (y/n) i zresetuj aplikacje: "))
            if reset2 == "y":
                sys.exit(0)
            else:
                sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Pozostało znaków:", characters_left)
        
def creating_password():
    global password_length
    global lowercase_letters
    global uppercase_letters
    global special_characters
    global digits
    
    print()
    print("Długość hasła:", password_length)
    print("Małe litery:", lowercase_letters)
    print("Duże litery:", uppercase_letters)
    print("Znaki specjalne:", special_characters)
    print("Cyfry:", digits)

    for _ in range(password_length):
        if lowercase_letters > 0:
            password.append(random.choice(string.ascii_lowercase))
            lowercase_letters -= 1
        if uppercase_letters > 0:
            password.append(random.choice(string.ascii_uppercase))
            uppercase_letters -= 1
        if special_characters > 0:
            password.append(random.choice(string.punctuation))
            special_characters -= 1
        if digits > 0:
            password.append(random.choice(string.digits))
            digits -= 1
            
    random.shuffle(password)
    print("Wygenerowane hasło:", "".join(password))
    confirm = str(input("Czy odebrałeś hasło?(y/n) "))

    if confirm == "y":
        sys.exit(0)
    elif confirm == "n":
        confirm2 = str(input("Kiedy odbierzesz hasło naciśnij klawisz y: "))
        if confirm2 == "y":
            sys.exit(0)
        else:
            print("Błędny klawisz! Potwierdź jeszcze raz")
            confirm1 = str(input("Kiedy odbierzesz hasło naciśnij klawisz y: "))
            if confirm1 == "y":
                sys.exit(0)
            
    else:
        print("Błędny klawisz")
        confirm3 = str(input("Kiedy odbierzesz hasło naciśnij klawisz y: "))
        if confirm3 == "y":
            sys.exit(0)
        else:
            print("Błędny klawisz! Potwierdź jeszcze raz")
        

password_length = int(input("Jak długie ma być hasło? "))

if password_length < 4:
    print("Hasło jest za krótkie, musi mieć co najmniej 4 znaki!")
    password_length = int(input("Jak długie ma być hasło? "))
else:
    characters_left = password_length
    
characters_left = password_length
    
lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
update_characters_left(lowercase_letters)


uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))
update_characters_left(special_characters)


digits = int(input("Ile cyfr ma mieć hasło? "))
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszstkie znaki zostały wykorzystane. Hasło zostanie uzupełnione małymi literami")
    lowercase_letters += characters_left
    
creating_password()