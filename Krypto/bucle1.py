for letra in 'DAVID':
    print('La letra es ' + letra)


texto = input('introduce un texto: ')

for simbolo in texto.lower():
    print(simbolo)

password = input('Introduce la contraseña: ')
if password == 'codigo':
    print('Accesso autorizado')
else:
    print('Acceso denegado')