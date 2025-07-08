class Person:
    # inicializace
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

      #f-ce pro vypsani jmena a prijmeni
    def vypis_jmeno(self):
        print(self.jmeno, self.prijmeni)

class Student(Person):
    def __init__(self, jmeno, prijmeni, obor):
        Person.__init__(self, jmeno, prijmeni)#dědim jmeno a prijmeni v person
        self.obor = obor

person = Person("Jakub", "Dvorsky")
person.vypis_jmeno()
student = Student("Tima", "Ne", "Truhlář")
student.vypis_jmeno()
print(student.obor)
