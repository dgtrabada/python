#!/usr/bin/python3

# Colecciones
  # Listas
  # Tuplas
  # Diccionarios

# La lista es un tipo de colección ordenada

print ( "======== listas =======")
lista = [ 2.1, 2.0, 3.1, 4.5, 8.0 ]
print(lista)                 # [2.1, 2.0, 3.1, 4.5, 8.0]
                             # Primer elemento de la lista
print(lista[0])              # 2.1
lista[1]=33                  # Cambiar el segundo elemento de la lista
print(lista)                 # [2.1, 33, 3.1, 4.5, 8.0]
print(len(lista))            # 5 
print(type(lista))           # <class 'list'>
print(lista[3])              # 4.5
print(lista[-1])             # 8.0
print(lista[2:4])            # [3.1, 4.5]
print(lista[2:])             # [3.1, 4.5, 8.0]
print(lista[:2])             # [2.1, 33]
lista.insert(2,9)            # 
print(lista)                 # [2.1, 33, 9, 3.1, 4.5, 8.0]
lista.remove(2.1)
print(lista)                 # [33, 9, 3.1, 4.5, 8.0]
lista.pop(1)
print(lista)                 # [33, 3.1, 4.5, 8.0]
del lista[2]
print(lista)                 # [33, 3.1, 8.0]
lista.extend(lista)
print(lista)                 # [33, 3.1, 8.0, 33, 3.1, 8.0]
lista.sort()
print(lista)                 # [3.1, 3.1, 8.0, 8.0, 33, 33]
lista.sort(reverse = True)
print(lista)                 # [33, 33, 8.0, 8.0, 3.1, 3.1]
aux = lista[0:2]             # seleccionar una porciones de la lista
print(aux)                   # [33, 33]
lista.clear()
print(lista)                 # []

lista=["F","H","A","v","b"]
print(lista)                 # ['F', 'H', 'A', 'v', 'b']  
lista.sort(key = str.lower)
print(lista)                 # ['A', 'b', 'F', 'H', 'v']


l1=["x","y","z"]
l2=[1,2,3]
l3=l1+l2                     # igual que extend   
print(l3)                    # ['x', 'y', 'z', 1, 2, 3] 
l1.append(l2)
print(l1)                    # ['x', 'y', 'z', [1, 2, 3]]


print("======== Tuplas =======")
#En realidad el constructor de la tupla es la coma, no el paréntesis, pero el intérprete muestra los paréntesis, y nosotros deberíamos utilizarlos,por claridad.
# tupla = 1,2,3,4
tupla = (1,2,3,4)
print(tupla)                 # (1, 2, 3, 4) 
                             # Primer elemento de la lista
print(tupla[0])  
# las tuplas son inmutables, es decir, sus valores no se pueden modificar una vez creada; y tienen un tamaño fijo      
#tupla[1]=33 TypeError: 'tuple' object does not support item assignment
print(len(tupla))            # 4 
print(type(tupla))           # <class 'tuple'>
print(tupla[3])              # 4
print(tupla[-1])             # 4
print(tupla[2:4])            # (3, 4)
print(tupla[2:])             # (3, 4)
print(tupla[:2])             # (1, 2)
aux = tupla[0:2]             # seleccionar una porciones de la lista
print(aux)                   # (1, 2)

print("======== Diccionarios =======")
#Son colecciones que relacionan una clave y un valor
d = {
  "Yellow": "Amarillo",
  "Blue": "Azul",
  "Black": "Negro"
}
print(d)                  # {'Yellow': 'Amarillo', 'Blue': 'Azul', 'Black': 'Negro'}
print(len(d))             # 3 
print(type(d))            # <class 'dict'>
#se accede por su clave
print(d["Blue"])          # Azul
d["Blue"]="0000FF"        # 0000FF
print(d["Blue"])




