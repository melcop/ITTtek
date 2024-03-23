import random

pot_a = ["Manchester City", "FC Barcelona","Napoli", "Bayern Munich", "Sevilla", "PSG", "Benfica", "Feyernood"]
pot_b = ["Real Madrid", "Manchester United", "Inter de Milan", "Borussia Dortmund", "Atletico de Madrid", "Leipzig", "Porto", "Arsenal"]
pot_c = ["Shaktar Donetsk", "Salzburg", "Milan", "Lazio", "Real Sociedad", "Celtic", "Newcastle", "Copenhagen"]
pot_d = ["Union Berlin", "Lens", "PSV", "Antwerp", "Braga", "Galatasaray", "Young Boys", "Crvena zvezda"]

# Shuffle each pot
for pot in [pot_a, pot_b, pot_c, pot_d]:
    random.shuffle(pot)

# Create group lists
group_list = [[] for _ in range(8)]

# Distribute teams evenly across groups
for pot in [pot_a, pot_b, pot_c, pot_d]:
    for i, team in enumerate(pot):
        group_list[i % 8].append(team)

# Print the result
for i, group in enumerate(group_list):
    print(f"Group {i+1}: {group}")