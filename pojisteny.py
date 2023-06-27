class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def vypis(self):
        return f'{self.jmeno} {self.prijmeni}, {self.vek}, {self.tel_cislo}'
