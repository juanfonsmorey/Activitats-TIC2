#Juan Fons Morey
#Phyton
"""
Escribe un programa que reciba un número del usuario e imprima si es positivo, negativo o cero.
Utiliza la cadena if/elif/else apropiada, no vayas a emplear tres if consecutivos.
"""

numero = int(input("Escriu un numero: "))
if numero > 0:
    print("És positiu")
elif numero < 0:
    print("És negatiu")
else:
    print("És zero")