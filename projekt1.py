"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Vratislav Martin
email: abbadc@gmail.com
discord: Vratislav M (dříve: abbadc#8421)
"""


uzivatele = {"bob" : "123", "ann" : "pass123", 
    "mike" : "password123", "liz" : "pass123"}
# slovnik se seznamem uzivatelu a jejich hesel

jmeno = input("Zadejte sve jmeno: \n")
heslo = input("Zadejte sve heslo: \n")
# ziskani jmena a hesla od uzivatele

if jmeno in uzivatele and heslo == uzivatele[jmeno]:
    print("Přihlášení úspěšné!")
else:
    print("Přihlášení se nezdařilo. Zkontrolujte své údaje.")
# a zjisteni zda se nachazi v seznamu (uzivatele)
    quit()
print()
print("Máš na výběr jeden ze tří textů k analýze")

texts = {
    "1": '''
        1. Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley.
    ''',
    
    "2": '''
        2. At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick
    ''',
    
    "3": '''
        3. The monument contains 8198 acres and protects
        a portion of the largest deposit of freshwater fish
        fossils in the world. The richest fossil fish deposits
        are found in multiple limestone layers, which lie some
        100 feet below the top of the butte. The fossils
        represent several varieties of perch, as well as
        other freshwater genera and herring similar to those
        in modern oceans. Other fish such as paddlefish,
        garpike and stingray are also present.
    ''',
}
# predani uzivateli vyber textu 

# Výběr volby a výpis odpovídajícího textu
vyber_textu = input("Vyber cislo textu (1-3): ")
if vyber_textu in texts:
    print(f"Vybral jsi text {vyber_textu}:")
    print(texts[vyber_textu])
else:
    print("Spatne cislo textu.")
    quit()
# Výběr volby a výpis odpovídajícího textu