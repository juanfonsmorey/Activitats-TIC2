#Juan Fons Morey
#Phyton

print("Introdueix una paraula qualsevol: ")
paraula = input()
j=len(paraula)-1
capicua=True
for i in paraula:
    if i != paraula[j]:
        capicua=False
    j-=1
if capicua:
    print("És capicua")
else:
    print("No és capicua")