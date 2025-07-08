# funkce
def pozdrav(jmeno: str, prijmeni: str, vek: int = 1):
    print(f"Hello {jmeno} {prijmeni}. Je ti {vek}!!!")
# pridani promennych nebo parametru do f-ce

pozdrav("Jakub", "1", "50") #volani f-ce
pozdrav("Marie", "2", "5")
pozdrav("Tomáš", "3", "4")
pozdrav(prijmeni="Bla", jmeno="Atom")

# Zadání: Vytvořte f-ci, která vezme list jako parametr a vypíše každou položku.
ovoce = ["jablko", "Hruška", "jahody"]
zelenina = ["rajčata", "okurek", "květák", "kedpubna"]
pecivo = ["rohliky", "Chleba", "pizza"]

print("Nakup:")

def vypis_list(list):

    for i in ovoce:
        print(i)
    for b in zelenina:
        print(b)
    for c in pecivo:
        print(c)

vypis_list(list)

#f-ce, které vrací hodnotu
def vynasob(a, b):
    return a * b
vysledek = vynasob(5, 3)
print(f"{vysledek =}")
print(vynasob(9, 9))

#Zadání: Vypočítej obvod obdélníku

def obvodObdelniku(a, b):
    print(f"Vypočet obdelníku o =2*(a+b) se stranami a = {a} a b = {b}.")
    return 2 * (a + b)
print(f"o = {obvodObdelniku(5, 4)}.")



