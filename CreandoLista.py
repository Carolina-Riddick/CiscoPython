#Creamos una lista con n cantidad de numeros y los vamos agregando.

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))