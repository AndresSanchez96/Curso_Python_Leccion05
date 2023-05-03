# Diccionario (key y valor) no tiene indices

diccionario = {
    'IDE':'Integrated Develoment Enviroment',
    'OOP':'Objet Oriented Programing',
    'DBMS':'Database Management System'
}
print(diccionario)
print(len(diccionario))
# acceder a un elemento (key)
print(diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# Modificando elementos
diccionario['IDE'] = 'integrated develoment enviroment'
print(diccionario)
# Recorrer los elementos
for termino, valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(diccionario)

# Comprobar existencia de algun elemento

print('IDE' in diccionario)

# Agrega un elemnot
diccionario['PK'] = 'Primary Key'
print(diccionario)

# removor un elemnto
diccionario.pop('DBMS')
print(diccionario)
#limpiar
diccionario.clear()
print(diccionario)
#eliminar diccionario
del diccionario
print(diccionario)