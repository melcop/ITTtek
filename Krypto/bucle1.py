import time;
for letra in 'DAVID':
    print('La letra es ' + letra)


texto = input('introduce un texto: ')

for simbolo in texto.lower():
    print(simbolo)
    
# password
password = input('Introduce la contraseña: ')
if password == 'codigo':
    print('Accesso autorizado')
else:
    print('Acceso denegado')
    time.sleep(5)
    print('Go away!')
