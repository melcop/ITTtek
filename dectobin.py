def decimal_to_binary(decimal):
    binary_representation = bin(decimal)[2:]
    return binary_representation

# Indtast decimaltallet fra brugeren
decimal_input = int(input("Indtast et decimaltal: "))

# Konverter decimaltallet til binært
binary_result = decimal_to_binary(decimal_input)

# Vis resultatet
print(f"{decimal_input} i binært er: {binary_result}")
