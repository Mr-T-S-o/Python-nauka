countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_and_capitals['Czechia'] = "Prague"

try:
    print(2 / 0)
    print(countries_and_capitals['USA'])
except KeyError:
    print("Klucz nie został znaleziony")
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
finally:
    print("To wykona się zawsze")