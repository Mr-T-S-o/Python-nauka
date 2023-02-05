#names_list =[]
#names_list.append("Tomek")
#names_list.append('Michal')

#names_list =["Tomek", "Michal", "Przemek", "Adam", "Tomek"]
#names_list2 =["Kamil"]
#names_list3 = names_list2 + names_list

#print(names_list3)

#names_list.remove("Tomek")
#names_list.clear()
#print(names_list)

#print(names_list)
#print()
#print(names_list.pop(0))
#print()
#print(names_list)

#for name in names_list:
    #print(name)
    
#print(names_list.count("Tomek"))
#print(len(names_list))

#names_list = ("Tomek", "Michal", "Przemek")
#print(names_list)

#names_set = {"Tomek", "Michal", "Tomek"}
#names_set2  = {"Adam", "Tobiasz", "Tomek"}

#names_set3 = names_set.difference(names_set2)
#names_set3 = names_set.union(names_set2)
#names_set3 = names_set.intersection(names_set2)
#names_set3 = names_set.symmetric_difference(names_set2)

#names_list.extend(names_set2)

#print(names_list)

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_and_capitals['Czechia'] = "Prague"

#for country, capital in countries_and_capitals.items():
    #print(country + "-" + capital)
    
#print(countries_and_capitals["Poland"])
#print(countries_and_capitals.get("Poland"))

if "Poland" in countries_and_capitals:
    print("Znaleziono")
else:
    print("Nie znaleziono")

