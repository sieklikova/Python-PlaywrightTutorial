import math
#Kvadraticka rovnice
konec = "ANO"
while konec.upper() != "NE":
    a = int(input("Zadej reálné číslo 'a': "))
    b = int(input("Zadej reálné číslo 'b': "))
    c = int(input("Zadej reálné číslo 'c': "))

    #výpočet diskriminantu
    diskriminant = (b**2) - (4 * a * c)

    if diskriminant < 0 and a != 0:
        print(f"Diskriminant = {diskriminant}")
        print("Pokud je diskriminanat záporný, pak rovnice nemá v oboru reálných čísel žádné řešení." )

    elif diskriminant == 0 and a != 0:
        diskriminantB = math.sqrt((b**2) - (4 * a * c))
        print(f"Diskriminant = {diskriminantB}")
        vypocet = (-b/(2 * a))
        print(f"Kvadratická rovnice má jedno řešení: \n x = {vypocet}")

    elif diskriminant > 0 and a != 0:
        diskriminantB = math.sqrt((b**2) - (4 * a * c))
        (f"Diskriminant = {diskriminantB}")
        vypocet1 = (-b + (diskriminantB))/(2 * a)
        vypocet2 = (-b + (diskriminantB))/(2 * a)
        print(f"Kvadratická rovnice má dvě řešení: \n x1 = {vypocet1}, \n x2 = {vypocet2}")

    else:
        print("Tahle rovnice není kvadratická, ale lineární." )

    konec = input("Chete pokračovat ve výpočtu další kvadratické rovnici? (Ano/Ne)")

print()
print("Děkujeme za použití našeho progamu a přejeme pěkný den.")








