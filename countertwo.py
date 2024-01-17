counter1 = 0
counter2 = 0

while counter1 <= 20 or counter2 <= 30:
    # Opdater summen
    total_sum = counter1 + counter2

    # Udskriv status
    print(f'Counter1: {counter1}, Counter2: {counter2}, Total Sum: {total_sum}')

    # Opdater tæller 1 (op til 20)
    if counter1 < 20:
        counter1 += 1

    # Opdater tæller 2 (op til 30)
    if counter2 < 30:
        counter2 += 1