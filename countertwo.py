counter1 = 0
counter2 = 0
counter3 = 0
while counter1 <= 20 or counter2 <= 25 or counter3 <= counter2:
    # Opdater summen
    total_sum = counter1 + counter2 + counter3

    # Udskriv status
    print(f'Counter1: {counter1}, Counter2: {counter2}, Counter3: {counter3}, Total Sum: {total_sum}')

    # Opdater tæller 1 (op til 20)
    if counter1 < 20:
        counter1 += 1

    # Opdater tæller 2 (op til 25)
    if counter2 < 25:
        counter2 += 2

    # Opdater tæller 3 (op til 25)
    if counter3 < 25:
        counter3 += 3