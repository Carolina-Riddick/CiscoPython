promedio = 0.0
calificacionBaja = 10
calificacionAlta = 0.0

for i in range(0,10):
    nota = float(input("Ingrese las 10 notas de los alumnos: "))
    promedio = promedio + nota
    if nota < calificacionBaja:
        calificacionBaja = nota
    elif nota > calificacionAlta:
        calificacionAlta = nota

promedio = promedio / 10

print(f"La nota mas baja es:{calificacionBaja} " )
print(f"La calificacion mas alta es : {calificacionAlta}")
print(f"El promedio de las notas es de: {promedio}")