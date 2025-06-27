class Vozidlo:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    def vypis_info(self):
        print(f"Značka: {self.znacka}")
        print(f"Model: {self.model}")

    def hybej_se(self):
        print("jeď")

class Auto(Vozidlo):
    pass

class Lod(Vozidlo):
    def hybej_se(self):
        print("pluj")

auto = Auto("Ford", "Mustang")
lod = Lod("Ibiza", "10")
Auto.vypis_info(auto)
Lod.vypis_info(lod)