# Sacar la raiz cuadrada de un numero:
import math

num = int(input("Ingrese un numero: "))
while num < 0 or num > 100:
    print("Error -> El numero ingresado es incorrecto. Ingrese otro numero")
    num = int(input("Ingrese un numero: "))
    
print(f"\nLa raiz cuadrada del numero es : {(math.sqrt(num)):.2f}")