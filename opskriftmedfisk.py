import random
import datetime

def generate_recipe(vegetables, meats, fishes, spices):
    vegetable = random.choice(vegetables)
    protein = choose_protein()
    spice = random.choice(spices)

    recipe = f"Opskrift: Stegt {protein} med {vegetable} og krydret med {spice}."
    return recipe

def choose_protein():
    # Få ugedagen som et tal (mandag=0, tirsdag=1, ..., søndag=6)
    weekday = datetime.datetime.today().weekday()
    
    # Hvis det er mandag til torsdag, vælg kød
    if weekday < 4:  # Mandag til torsdag
        return random.choice(meats)
    else:  # Fredag til søndag
        return random.choice(fishes)

# Liste med grøntsager
vegetables = ["broccoli", "gulerødder", "squash", "spinat", "tomater", "aubergine", "peberfrugt"]

# Liste med kød
meats = ["kylling", "oksekød", "svinekød", "lam"]

# Liste med fisk
fishes = ["laks", "tun", "torsk", "rødspætte"]

# Liste med krydderier
spices = ["oregano", "timian", "rosmarin", "karry", "kanel", "koriander", "spidskommen"]

# Generer og udskriv opskrift
recipe = generate_recipe(vegetables, meats, fishes, spices)
print(recipe)
