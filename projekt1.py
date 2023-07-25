"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Vratislav Martin
email: abbadc@gmail.com
discord: Vratislav M (dříve: abbadc#8421)
"""

oddelovac = "-" * 40


# slovnik se seznamem uzivatelu a jejich hesel
uzivatele = {"bob" : "123", "ann" : "pass123", 
    "mike" : "password123", "liz" : "pass123"}

# ziskani jmena a hesla od uzivatele
jmeno = input("username:")
heslo = input("password:")
print(oddelovac)

# a zjisteni zda se nachazi v seznamu (uzivatele)
if jmeno in uzivatele and heslo == uzivatele[jmeno]:
    print(f"Welcome to the app, {jmeno}!")

else:
    print("unregistered user, terminating the program..")
    quit()
    
print("We have 3 texts to be analyzed.")
print(oddelovac)
texts = {
    "1": '''
        Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley.
    ''',
    
    "2": '''
        At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick
    ''',
    
    "3": '''
        The monument contains 8198 acres and protects
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


vyber_textu = input("Enter a number btw. 1 and 3 to select: ")


# Rozdělení slov pomocí mezer
rozdel_slova = texts[vyber_textu].split()
# pocet_slov = len(rozdel_slova)

# odstraneni diakritiky
bez_dia = []
for slovo in rozdel_slova:
    bez_dia.append(slovo.strip(".,:"))


# Zjištění délky a počtu jednotlivých slov
# Zjištění slov s velkým písmenem na začátku
# Zjištění slov složených z velkých písmen
delka_slov = {}
pocet_s_velkym = {}
pocet_velka_cela = {}

for slovo in bez_dia:
    delka = len(slovo)
    delka_slov[delka] = delka_slov.get(delka, 0) + 1

    if slovo.istitle():
        pocet_s_velkym[slovo] = pocet_s_velkym.get(slovo, 0) + 1

    if slovo.isupper() and slovo.isalpha():
        pocet_velka_cela[slovo] = pocet_velka_cela.get(slovo, 0) + 1

# zjisteni poctu slov slozenych z  malych pismen
pocet_mala = sum(1 for mala in bez_dia if mala.islower())
# zjisteni poctu cisel
pocet_cisel = sum(1 for cislo in bez_dia if cislo.isdigit())
# suma je suma
suma_cisel = sum(int(cislo) for cislo in bez_dia if cislo.isdigit())

# vypsani vysledku v textu
print(oddelovac)
print(f"There are {len(bez_dia)} words in the selected text.")
print(f"There are {len(pocet_s_velkym)} titlecase words.")
print(f"There are {len(pocet_velka_cela)} upercase words.")
print(f"There are {(pocet_mala)} lowercase words.")
print(f"There are {pocet_cisel} numberic string.")
print(f"The sum of all the numbers {suma_cisel}.")
print(oddelovac)

# Najdi nejdelší délku slova
max_delka = max(delka_slov.values())


# Výpis výsledku
slovo = "OCCURENCES"
print(f"LEN | {slovo:^{max_delka}} | NR")


print(oddelovac)
for idx, (delka, occurrences) in enumerate(sorted(delka_slov.items())):
    print(f"{delka:3} | {'*' * occurrences:{max_delka}} | {occurrences:2}")
