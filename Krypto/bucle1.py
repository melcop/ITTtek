import time;
for letra in 'DAVIDS':
    print('La letra es ' + letra)


texto = input('introduce un texto: ')
print("text is: ", texto)
for simbolo in texto.lower():
    print(simbolo)
    
# password
password = input('Introduce la contraseña: ')
print(password)
specialpin = input('Special pin: ')
if password == 'codigo' and specialpin == '23':
    print('Accesso autorizado')
else:
    print('Acceso denegado')
    time.sleep(10)
    print('Go away!')