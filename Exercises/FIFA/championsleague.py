import random
team = " "
pot_a = ["Manchester City", "FC Barcelona","Napoli", "Bayern Munich", "Sevilla", "PSG", "Benfica", "Feyernood"]
pot_b = ["Real Madrid", "Manchester United", "Inter de Milan", "Borussia Dortmund", "Atletico de Madrid", "Leipzig", "Porto", "Arsenal"]
pot_c = ["Shaktar Donetsk", "Salzburg", "Milan", "Lazio", "Real Sociedad", "Celtic", "Newcastle", "Copenhagen"]
pot_d = ["Union Berlin", "Lens", "PSV", "Antwerp", "Braga", "Galatasaray", "Young Boys", "Crvena zvezda"]

group_1 =[]
group_2 =[]
group_3 =[]
group_4 =[]
group_5 =[]
group_6 =[]
group_7 =[]
group_8 =[]

group_list = [group_1, group_2, group_3, group_4, group_5, group_6, group_7, group_8]

sizeofgroup = len(pot_a)
                  
# initializing position
pos = 0
#Insert teams to group_list
# using insert() + loop
# to insert one list in another
#for i in range(len(pot_a)):
#    group_list.insert(i + pos, pot_a[i])

#print(group_list)

# Bland elementerne i liste A tilfældigt
random.shuffle(pot_a)

# Fordele elementerne fra A tilfældigt på de 8 lister i B
#for element in pot_a:
#    tilfældig_liste_index = random.randint(0, 7)
#    group_list[tilfældig_liste_index].append(element)

# Fordel elementerne fra A jævnt på de 8 lister i B
for i, element in enumerate(pot_a):
    liste_index = i % 8  # Brug modulus-operatoren for at få det jævne indeks
    group_list[liste_index].append(element)

# Fordel elementerne fra A jævnt på de 8 lister i B
for i, element in enumerate(pot_b):
    liste_index = i % 8  # Brug modulus-operatoren for at få det jævne indeks
    group_list[liste_index].append(element)

# Fordel elementerne fra A jævnt på de 8 lister i B
for i, element in enumerate(pot_c):
    liste_index = i % 8  # Brug modulus-operatoren for at få det jævne indeks
    group_list[liste_index].append(element)

# Fordel elementerne fra A jævnt på de 8 lister i B
for i, element in enumerate(pot_d):
    liste_index = i % 8  # Brug modulus-operatoren for at få det jævne indeks
    group_list[liste_index].append(element)

# Vis resultatet
for i, liste in enumerate(group_list):
    print(f"Group {i+1}: {liste}")


#Insert teams to group_a
#for i in pot_a:
#    a = random.randrange(0, sizeofgroup)
#    b=pot_a[a]
#    group_a.append(b)
    #print(a)

print("pot A: ", pot_a)
#print("pot B: ", pot_b)
#print("pot C: ", pot_c)
#print("pot D: ", pot_d)
print(group_list)
# function for random group maker