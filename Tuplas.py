# La tupla es similar a una lista pero no es modificable
frutas = ('Naranja','Platano','Guayaba')
print(len(frutas))
print(frutas[0])
# para modificar una tupla se debe pasar primero a una lista y voler
frutaLista = list(frutas)
frutaLista[0] = 'Pera'
fruta = tuple(frutaLista)
print(fruta)
# Eliminar tupla
del fruta