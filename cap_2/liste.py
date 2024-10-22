# creo una lista vuota
my_list = []

# inserisco/appendo dei valori ala fine della lista
my_list.append("Pay bills")
my_list.append("Tidy up")
my_list.append("Walk the dog")
my_list.append("Cook dinner")

# stampo la lista
print(my_list)

# stampo il primo elemento della lista
print(my_list[0])

# recupero l'elemento posizione nella lista del valore "Cook dinner" e lo stampo
i = my_list.index("Cook dinner")
print(i)

# inserisco  alla posizione i-esima dell'elemento precedente il valore "Go to the pharmacy"
my_list.insert(i,"Go to the pharmacy")

# stampo di nuovo il contenuto della lista
print(my_list)

# conto quante volte è contenuto nella lista il valore "Tidy up"
print(my_list.count("Tidy up"))

# utilizzo della slice notation
print("my_list[0:3]")
print(my_list[0:3])
print("my_list[:3]")
print(my_list[:3])
print("my_list[3:]")
print(my_list[3:])
print("my_list[:]")
print(my_list[:])
my_list[len(my_list):] = ["Mow the law", "Water plants"]
print("my_list")
print(my_list)
del my_list[5:]
print(my_list)