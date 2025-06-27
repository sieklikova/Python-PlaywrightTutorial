class Osoba:
    jmeno = ""
    prijmeni = ""
    vek: int = ""
    #každá třída by měla mít svou f-ci, která funguje pro inicializaci
    def __init__(self, jmeno, prijmeni, vek = 3):
        self.jmeno = jmeno #inicializace
        self.__prijmeni = prijmeni
        #proměnná která nejde změnit (ochrana dat)
        self.__vek = vek
    #přidání metod do třídy, Metody jsou f-ce akorát uvnitř třídy.
    def vypis_info(self):
        print(f"Jmenuji se {self.jmeno} {self.__prijmeni} a je mi {self.__vek} .")
    #funkce pro vypsání proměnné, která se nedá měnit jako napr. __vek
    def vypis_vek(self):
        return self.__vek
""" #uděláme si instanci třídy
osoba = Osoba("Lenka", "Kašpárková", 5)
osoba2 = Osoba("Lidie", "Nová")
print(osoba.jmeno)
print(osoba.prijmeni)
osoba.jmeno = "Tomáš"
print(osoba2.vypis_info())
print(osoba.vypis_info())
print(osoba.vypis_vek())"""

