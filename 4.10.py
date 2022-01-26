#Juan Fons Morey
#Phyton

"
Escribe un programa para jugar a piedra, tijera, papel: (4 pts)
Crea un programa que imprima aleatoriamente 0, 1, o 2.
Usando sentencias if, expande el programa de manera que ahora imprima al azar piedra, papel o tijera. No hagas la selección desde una lista, tal como hemos visto en el capítulo.
Añade al programa la opción de que primero le pregunte al usuario qué es lo que elige.
(Sería más fácil darle a escoger entre las opciones 1, 2, o 3.)
Añade una declaración condicional para determinar quién gana.
"

import random
x=random.randrange(0,3)
"""
Pedra=0
Paper=1
Tissores=2
"""
print(x)
y=int(input("introdueix Pedra=0 o Paper=1 o Tissores=2: "))
if x == 0 and y == 1 or x == 1 and y == 2 or x == 2 and y == 0:
    print("Has guanyat")
elif x == 0 and y == 0 or x == 1 and y == 1 or x == 2 and y == 2:
    print("Has empatat")
else:
    print("Has perdut")
