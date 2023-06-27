import sqlite3
from pojisteny import Pojisteny


#Třída reprezentující databázi
class Databaze:
    def __init__(self):
        self.conn = sqlite3.connect('pojisteni.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS pojisteni (jmeno text, prijmeni text, vek int, tel_cislo text)')


    """
    Metoda pro přidání pojištěnce.
    Předání hodnot do db.
    """
    def pridatPojisteneho(self, pojisteny):
        self.c.execute('INSERT INTO pojisteni VALUES (?, ?, ?, ?)',
                       (pojisteny.jmeno, pojisteny.prijmeni, pojisteny.vek, pojisteny.tel_cislo))
        self.conn.commit()



    #Metoda pro zobrazení všech pojištěných.
    def zobrazPojistene(self):
        self.c.execute('SELECT * FROM pojisteni')
        for row in self.c.fetchall():
            pojisteny = Pojisteny(row[0], row[1], row[2], row[3])
            print(pojisteny.vypis())


    #Metoda pro výpis konkrétního pojištěnce.
    def najdiPojisteneho(self, jmeno, prijmeni):
        self.c.execute('SELECT * FROM pojisteni WHERE jmeno = ? AND prijmeni = ?', (jmeno, prijmeni))
        row = self.c.fetchone()
        if row is None:
            print('Pojištěný nenalezen.')
        else:
            pojisteny = Pojisteny(row[0], row[1], row[2], row[3])
            print(pojisteny.vypis())


    #Metoda pro ukončení - uzavření konzole.
    def ukoncit(self):
        self.conn.close()
