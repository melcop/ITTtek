import random

def lav_opskrift(gronsag, kod, fisk, kryderier):
    gronsag = random.choice(gronsag)
    if random.choice([True, False]):  # Vælg tilfældigt mellem fisk og kød
        protein = random.choice(fisk)
    else:
        protein = random.choice(kod)
    kryderier = random.choice(kryderier)

    opskrift = f"Opskrift: Stegt {protein} med {gronsag} og krydret med {kryderier}."
    return opskrift

# Liste med grøntsager
gronsag = ["broccoli", "gulerødder", "spinat", "tomater", "aubergine", "peberfrugt"]

# Liste med kød
kod = ["kylling", "oksekød", "svinekød", "lam"]

# Liste med fisk
fisk = ["laks", "tun", "torsk", "rødspætte"]

# Liste med krydderier
kryderier = ["oregano", "timian", "rosmarin", "karry", "kanel", "spidskommen"]

# Generer og udskriv opskrift
opskrift = lav_opskrift(gronsag, kod, fisk, kryderier)
print(opskrift)