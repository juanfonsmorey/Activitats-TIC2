#Juan Fons Morey
#Phyton

"""
Este código que comprueba si x es un valor positivo. Hay dos cosas mal en él. Una impide que se ejecute, 
la otra es más sutil. Asegúrate de que la sentencia if funciona independientemente del valor que tome x.
Identifícalas.
"""

variable = float(input("Escriu un nombre positiu o negatiu:"))
if variable > 0:
    print("El nombre és positiu.")
else:
    print("El nombre no positiu.")