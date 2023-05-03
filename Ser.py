#set no mantienen un orden != listas y tuplas

planetas = {'Marte','Jupiter','Venus'}
print(planetas)
# Largo
print(len(planetas))
# revisar si un elemento esta presente
print('Marte' in planetas) #== con listas y tuplas
#añadir
planetas.add('Tierra')
print(planetas)
# no se puede duplicar elementos
planetas.add('Tierra')
print(planetas)
# eliminar elementos posible arrojando error
planetas.remove('Tierra')
print(planetas)
# eliminar sin error
planetas.discard('Jupiter')
print(planetas)
# limpiar set
planetas.clear()
print(planetas)
# eliminar ppr completo
del planetas
print(planetas)