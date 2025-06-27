#print("Hello World!", type('Hello World!'))
#print(10, type(10))
#print(3.14, type (3.14))
#print(True, type(True))

#jmeno = "Jakub"  #zde muzes psat komentar
#cislo = 10
#pi = 3.14
#pravda = True

#print(jmeno, type(jmeno))
#jmeno = "Pavel"
#print(jmeno)

#print('')
#print('Hello "\World"') # jak to udelat abych viděla na zvlast radku \n

#x = 5
#print(x)
'''
jmeno = input("Zadej jméno: ")
prijmeni = input("Zadej prijmeni: ")
vek = int(input("Zadej vek: ")) # jak string převést na intgr, abychom mohli počítat v budoucnu
dospely = True
print(f"jméno {jmeno}\nPříjmení: {prijmeni}\nVěk: {vek}\nDospělý: {dospely}")
print(type(vek))
'''

'''
print(f"{1 > 2 = }")
print(f"{1 < 2 = }")
print(f"{1 == 2 = }")
print(f"{1 != 2 = }")
print(f"{1 <= 2 = }")
print(f"{1 >= 2 = }")

print(f"{1 > 2 and 2 == 2 = }")
print(f"{1 > 2 or 2 == 2 = }")
'''

'''
# Vzít uživtelský vstup čísla a vypsat True pokud je číslo větší než 10 a zároveň menší než 20
cislo = int(input("Zadej číslo: "))
#print(f"Je číslo {cislo} mezi 10 a 20? \n{cislo > 10 and cislo < 20}")

if cislo > 10 and cislo < 20:
    print("Číslo je mezi 10 a 20.")
else:
    print("Číslo není mezi 10 a 20.")
    '''
'''
# použití elif
cislo = int(input("Zadej číslo: "))

if cislo > 10 and cislo < 20:
  print("Číslo je mezi 10 a 20.")

elif cislo > 30:
  print("Číslo je větší než 30")
else:
  print("Podmínka není splněna.")
  '''
'''
# Uživatel zadá věk, pomocí podmínek vypíše zda je dospělý (18+)', teenager (<18) , dite (<15)
vek = int(input("Zadej vek: "))

if vek >= 18:
 print("Dospělý")

elif vek < 18 and vek >= 15:
 print("Teenager")

else:
 print("Dítě")
 '''
'''
vek = int(input("Zadej vek: "))
pohlavi = input("Zadej m/z: ")

if vek >= 18:
   print("Dospělý")
   if pohlavi == "m":
       print("Jsi muž.")
elif pohlavi == "z":
   print("jsi žena.")

elif vek < 18 and vek >= 15:
   print("Teenager")

else:
   print("Dítě")
 '''

'''
# Listy (arrays)

list = [1, 2, "ahoj", True, [1, 2,3, 4]]
#print(list[4][2])
#print(len(list))
#print(len(list[4]))
#String se chová jako pole
nejaky_text  = "Radek"
print(nejaky_text[0])

#tohle jde od zadu
print(nejaky_text[-1])

#Hranice / range vypisu pole
nove_pole = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nove_pole[2:5])
print(nove_pole[:-3])
print(nove_pole[:-10])

nove_pole[2] = 11
print(nove_pole[2])

nove_pole[3] = -12
print(nove_pole[3])

nove_pole = nove_pole[:6]
print(nove_pole)

#přidávání položek do listu, list je třída v pathonu
nove_pole.append("Patek")
print(nove_pole)

nove_pole.insert(9, "Neděle")
print(nove_pole)

nove_pole.extend(list)
print(nove_pole)

#mazání hodnot z listu
nove_pole.remove("Neděle")
print(nove_pole)

nove_pole.remove(1)
print(nove_pole)

nove_pole.pop(6) #pole
print(nove_pole)

nejaky_text = "Radek " + "Patek"
print(nejaky_text)

nejaky_text = [0, 1, 2] + [4, 5, 6]
print(nejaky_text)

nejaky_text = [0, 1, 2] * 10
print(nejaky_text)
 '''

# pole se jménem
#pole tří lidí ve které budou tři další pole

jmeno = "Radek Patek"
print(jmeno)

lide = [
    ["Jitka", 15, 99999999],
    ["Lea", 20, 11111111],
    ["Radek", 50, 444444444444]
]
'''
print(lide)
print(lide[0][1])

#Cyklus for

for x in jmeno:
    print(x)

for x in lide:
    print(x)

for x in lide:
    print(x[0])
'''
for vek in lide:
    if vek[1] >= 18:
     print(f"Ahoj {vek[0]} jsi dospělý")
else:
    print(f"Ahoj {vek[0]} nejsi dospělý")

pole = []
for x in range(10, 100, 5):
    pole = pole + [x]
print(pole)

jmeno = "Jitka Sieklikova"
firstname = ""
secondname = ""
space = False
# udělat znovu
for x in jmeno:
    if x == " ":
       space = True
    else:
        if space == False:
            firstname = firstname + x
        else:
            secondname = secondname +x
print(firstname)
print(secondname)

    #    print(jmeno.split)
'''
i = 0
while i <= 10:
     print(i)
     i = i + 1
'''
 #While - provádí se dokud podmínka platí


konec = "Ne"
todo = []
while konec == "Ne":
    polozka = input("Zadej co chceš udělat: ")
    todo = todo + [polozka]
    konec = input("Chceš pokračovat? (Ano, Ne): ")
print(todo)

#Pokud chceme zadat další rovnici
















