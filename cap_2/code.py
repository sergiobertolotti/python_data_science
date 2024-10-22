from collections import deque

# creo una lista vuota
my_list = []

# inserisco/appendo dei valori ala fine della lista
my_list.append("Pay bills")
my_list.append("Tidy up")
my_list.append("Walk the dog")
my_list.append("Go to the pharmacy")
my_list.append("Cook dinner")
print("lista iniziale")
print(my_list)

# creo la coda
queue = deque(my_list)
queue.append("Wash the car")
print(queue.popleft(), " - Done!")

my_list_upd = list(queue)
print(my_list_upd)