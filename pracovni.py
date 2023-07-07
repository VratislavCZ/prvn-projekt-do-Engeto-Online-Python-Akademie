table = []
for i in range(1, 12):
    occurrences = get_word_occurrences(i, words)
    table.append((i, '*' * occurrences))

# Výpis tabulky
print("LEN| OCCURRENCES | NR.")
print("----------------------------------------")
for row in table:
    print("{:2d} |{}| {}".format(row[0], row[1].ljust(12), len(row[1])))



# Výpis výsledku
print("LEN | OCCURENCES | NR")
for length, occurrences in delka_slov.items():
    print(f"{length:2} | {'*' * occurrences:11} | {occurrences:2}")


# Výpis výsledku
for length in sorted(delka_slov):
    occurrences = delka_slov[length]
    print(f"{length:2} | {'*' * occurrences:11} | {occurrences:2}")


pocet_mala = {}

# Zjištění počtu slov složených z malých písmen
for slovo in rozdel_slova:
    if slovo.islower() and slovo.isalpha():
        if slovo in pocet_mala:
            pocet_mala[slovo] += 1
        else:
            pocet_mala[slovo] = 1

print(f"There are {len(pocet_mala)} lowercase words.")

# Vypsání jednotlivých slov a jejich počtu výskytů
for slovo, pocet in pocet_mala.items():
    print(f"Word: {slovo}, Count: {pocet}")
# TODO Predelat nefunguje 


pocet_mala = {}

# Zjištění počtu slov složených z malých písmen
for slovo in rozdel_slova:
    if slovo.islower() and slovo.isalpha():
        pocet_mala[slovo] = pocet_mala.get(slovo, 0) + 1

print(f"There are {len(pocet_mala)} lowercase words.")

# Vypsání jednotlivých slov a jejich počtu výskytů
for slovo, pocet in pocet_mala.items():
    print(f"Word: {slovo}, Count: {pocet}")