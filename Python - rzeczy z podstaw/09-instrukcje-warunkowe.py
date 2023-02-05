light = input("Jakie jest światło? (red, green, yellow) ")

if light == 'red' :       #Instrukcje warunkowe w języku Python
    print("Czekaj!")
elif light == 'yellow':
    print("Przygotuj się!")
elif light == 'green':
    print("Jedź!")
else:
    print("Niewłaściwa wartość")
    
#print("Jedź!") if light == 'green' else print("Czekaj")