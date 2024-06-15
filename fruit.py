import random

# Opret en liste med 10 forskellige frugter
frugter = ["æble", "tomat", "banan", "appelsin", "jordbær", "kiwi", "ananas", "mango", "drue", "pære", "fersken"]

# Vælg en tilfældig frugt fra listen
tilfældig_frugt = random.choice(frugter)

# Udskriv den valgte frugt
print("Den tilfældigt valgte frugt er:", tilfældig_frugt)

# Håndtering af tilfældet hvor index er større end 6
if frugter.index(tilfældig_frugt) > 6:
    print("Større end index")

# Gange frugtens navn med 2 (eksempelvis)
tilfældig_frugt_ny = tilfældig_frugt * 2
print("Frugtens navn gange 2:", tilfældig_frugt_ny)