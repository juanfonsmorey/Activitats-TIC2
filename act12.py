#Juan Fons Morey
#Phyton

"""
¿Qué está mal en este código?
"""

#Juan Fons Morey
#Phyton

print("Bienvenidos a la Ultra Trail!")
 
print("A. Banquero")
print("B. Carpintero")
print("C. Granjero")
variable = input("¿Cuál es tu profesión?: ")
if variable.upper() == "A":
    dinero = 100
elif variable.upper() == "B":
    dinero = 70
elif variable.upper() == "C":
    dinero = 50
print("Genial! empezarás el juego con", dinero, "dólares.")