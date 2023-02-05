name = "tomek"

print(len(name)) #Jaka jest ilość znaków w zmiennej name
print(name.capitalize()) #Zmiana pierwszej litery na wielką 
print(name.upper()) #Zmiana wszytkich liter na wilkie
print(name.lower()) #Zmiana wsztskich liter na małe

print(name[-3:]) #Wydrukowanie 3 ostatnich liter

channel = "Jestem chory i uczę się Pythona"
print(channel.split(" ")) #Wydrukowanie wszystkich wyrazów osobno

join_string = " "
print(join_string.join(['Jestem', 'chory', 'i', 'programuje'])) #Połaczenie wszystkich wyrazów w jedno zdanie

print(name.endswith("k")) #Czy wyraz kończy się na małą literę k
print(name.startswith("K")) #Czy wyraz zaczyna się od wielkiej litery K

#print(name.strip())

first_name = "Tomek"
sur_name = "Sobala"

print(first_name + " " + sur_name) #Wydrukowanie obu wyrazów razem

join_string = " "
print(join_string.join([first_name, sur_name])) #Wydrukowanie obu wyrazóww razem tylko innym sposobem

#james_bond = 7
#print(str(james_bond).zfill(3))



