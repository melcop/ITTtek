import random
team = " "
pot_a = ["Manchester City", "FC Barcelona","Napoli", "Bayern Munich", "Sevilla", "PSG", "Benfica", "Feyernood"]
pot_b = ["Real Madrid", "Manchester United", "Inter de Milan", "Borussia Dortmund", "Atletico de Madrid", "Leipzig", "Porto", "Arsenal"]
pot_c = ["Shaktar Donetsk", "Salzburg", "Milan", "Lazio", "Red Star",]
pot_d = ["Berlin Union", "Lens"]

group_a =[]
group_b =[]
group_c =[]
group_d =[]
group_e =[]
group_f =[]
group_g =[]
group_h =[]

sizeofgroup = len(pot_a)

for i in pot_a:
    a = random.randrange(0, sizeofgroup)
    print(pot_a[a])
    #print(a)

#print(pot_a)

# function for random group maker