#vytvor class Auto. Zvlast do souboru
#parametry: Značky, barvu, max_rychlost, aktualni_rychlost
#metody: pridej(init), zastav(), zaboc(str)
#pridej(int) - nemůže překročit maximální rychlost

class Auto:
    def __init__ (self,znacka, barva, max_rychlost, aktualni_rychlost = 0):
        self.znacka = znacka
        self.barva = barva
        self.max_rychlost = max_rychlost
        self.aktualni_rychlost = aktualni_rychlost

    def pridej(self, rychlost: int):
        self.aktualni_rychlost += rychlost
        if self.aktualni_rychlost > self.max_rychlost:
            self.aktualni_rychlost = self.max_rychlost
            print(f"pridej. Tvá aktuální rychlost je {self.aktualni_rychlost}")

    def zastav(self):
            self.aktualni_rychlost = 0
            print(f"Zastav. Tvá aktuální rychlost je {self.aktualni_rychlost}.")

    def zaboc(self, smer: str):
        print(f"Zaboc {smer}.")

#auto = Auto("audi", "černá", 180, 200)
#auto.pridej(50)
#auto.zastav()
#auto.zaboc("levo")
#print(auto.aktualni_rychlost)


