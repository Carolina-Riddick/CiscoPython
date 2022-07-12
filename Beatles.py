
# Armamos una lista con nombre Beatles. Pasar al VS
Beatles = []

# Agregamos sus nombres:
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

# Mostramos resultados
print("Paso 1:", Beatles)

# Pedimos al usuario el resto de los nombres y mostramos resultados:
for i in range(2):
    Beatles.append(input("Ingrese el resto de los nombres de los Beatles aqui: "))

print(Beatles)
print(len(Beatles))

# Funcion del para Eliminar e imprimimos resultados
# del Beatles [-1]
# del Beatles [-1]

del Beatles[3]
del Beatles[3]

# del Beatles [-1]
# del Beatles [-1]

# del Beatles[3:5] que queden 3 de 5
print(Beatles)
print(len(Beatles))

# Incorporamos a Ringo en la Primera posicion.
Beatles.insert(0, "Ringo Starr")

print(Beatles)
print(len(Beatles))

