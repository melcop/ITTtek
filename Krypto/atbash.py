# Cifra atbash

import pyperclip

# Alfabetos mpleados
CLARO = 'abcdefghijklmnopqrstuwxyz '
CIFRADO = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '

# Almacena la forma cifrada/descifrada del texto
salida = ''

# Guarda el texto introducido
texto = input('Introduce un texto: ')

# Ejecuta el cifrado/decifrado letra por letra
for simbolo in texto.lower():
    if simbolo in CLARO:
        # Identifica la posición de cada símbolo
        indice = CLARO.index(simbolo)
        # Añade un nuevo símbolo al texto cifrado/descifrado
        salida += CIFRADO[indice]
        
# Imprime en pantalla el resultado
print (salida)

# Copia el mensaje al portapapeles
pyperclip.copy(salida)