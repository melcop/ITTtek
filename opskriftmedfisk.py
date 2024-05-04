import random

def generate_recipe(vegetables, meats, fishes, spices):
    vegetable = random.choice(vegetables)
    if random.choice([True, False]):  # Vælg tilfældigt mellem fisk og kød
        protein = random.choice(fishes)
    else:
        protein = random.choice(meats)
    spice = random.choice(spices)

    recipe = f"Opskrift: Stegt {protein} med {vegetable} og krydret med {spice}."
    return recipe

# Liste med grøntsager
vegetables = ["broccoli", "gulerødder", "spinat", "tomater", "aubergine", "peberfrugt"]

# Liste med kød
meats = ["kylling", "oksekød", "svinekød", "lam"]

# Liste med fisk
fishes = ["laks", "tun", "torsk", "rødspætte"]

# Liste med krydderier
spices = ["oregano", "timian", "rosmarin", "karry", "kanel", "spidskommen"]

# Generer og udskriv opskrift
recipe = generate_recipe(vegetables, meats, fishes, spices)
print(recipe)