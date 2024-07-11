import random

def generate_recipe(vegetables, meats, spices):
    vegetable = random.choice(vegetables)
    meat = random.choice(meats)
    spice = random.choice(spices)

    recipe = f"Opskrift: Stegt {meat} med {vegetable} og krydret med {spice}."
    return recipe

# Liste med grøntsager
vegetables = ["broccoli", "gulerødder", "løg", "spinat", "tomater", "aubergine", "peberfrugt"]

# Liste med kød
meats = ["kylling", "oksekød", "svinekød", "lam", "laks", "tun"]

# Liste med krydderier
spices = ["oregano", "timian", "rosmarin", "karry", "kanel", "spidskommen"]

# Generer og udskriv opskrift
recipe = generate_recipe(vegetables, meats, spices)
print(recipe)