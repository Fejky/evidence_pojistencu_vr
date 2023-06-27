from databaze import Databaze
from pojisteny import Pojisteny


#Zadání hodnot pro vytvoření pojištěnce.
def vytvorPojisteneho(db):
    jmeno = input('Zadejte jméno pojištěnce: ')
    prijmeni = input('Zadejte příjmení: ')
    vek = int(input('Zadejte věk: '))
    tel_cislo = input('Zadejte telefonní číslo: ')
    pojisteny = Pojisteny(jmeno, prijmeni, vek, tel_cislo)
    db.pridatPojisteneho(pojisteny)


#Odkaz na metodu třídy Databáze pro výpis všech pojištěných.
def zobrazSeznam(db):
    db.zobrazPojistene()

#Zadání parametrů pro hledání konkrétního pojištěnce.
def vyhledejPojisteneho(db):
    jmeno = input('Zadejte jméno pojištěného: ')
    prijmeni = input('Zadejte příjmení: ')
    db.najdiPojisteneho(jmeno, prijmeni)

def hlavicka():
    print("---------------------------------")
    print("Evidence pojištěných")
    print("---------------------------------\n")

def vypisVolby():
    print("Vyberte si akci:")
    print("[1] - Přidat nového pojištěnce")
    print("[2] - Vypsat všechny pojištěnce")
    print("[3] - Vyhledat pojištěnce")
    print("[4] - Konec")



#Cyklus pro opakování volby menu
def menu():
    db = Databaze()
    hlavicka()
    vypisVolby()

    while True:
        volba = input()
        if volba == '1':
            vytvorPojisteneho(db)
            anykey = input('\nData byla uložena. Pokračujte libovolnou klávesou...\n')
            vypisVolby()
        elif volba == '2':
            zobrazSeznam(db)
            anykey = input('\nPokračujte libovolnou klávesou...\n')
            vypisVolby()
        elif volba == '3':
            vyhledejPojisteneho(db)
            anykey = input('\nPokračujte libovolnou klávesou...\n')
            vypisVolby()
        elif volba == '4':
            db.ukoncit()
            break
        else:
            print('Neplatná volba, zkuste to znovu.\n')

if __name__ == '__main__':
    menu()
