#Definir lista de tip str
nombres = ['Juan','Karla','Ricardo','Maria']
#Imprimir la lista de nombres
print(nombres)
#Acceder a elementos de la lista
print(nombres[0])
print(nombres[1])
print(nombres[-1])

#rango
print(nombres[0:2])# sin incluir 2
#ir del inicio al indice sin incluirlo
print(nombres[:3])
#desde el indice inicial hasta el final
print(nombres[1:])
#Cambiar un valor de la lista
nombres[3] = 'Ivone'
print(nombres)
#iterar nuestra lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

# Preguntar el largo de una lista
print(len(nombres))
# agregar un elemento
nombres.append('Lorenzo')
print(nombres)
#insertar un elemento en un indice especifico
nombres.insert(1,'Octavio')
print(nombres)
#remover un elemento
nombres.remove('Octavio')
print(nombres)
#Remover el ultimo valor agregado
nombres.pop()
print(nombres)
#Eliminar un indice
del nombres[0]
print(nombres)
#Limpiar todos los elementos
nombres.clear()
print(nombres)
#Borrar la lista por completo
del nombres
print(nombres)