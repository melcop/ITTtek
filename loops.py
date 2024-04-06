# Initialiserer startværdien
tal = 10

# Løkke der tæller ned med 1 og ganger med 3
while tal > 0:
    total = tal * 3
    print(total)
    if total < 10:
        print("Tjek, tal er mindre end 10")
    tal -= 1