#!/usr/bin/python3

# La lista es un tipo de colección ordenada

l = [ 3.14, False, "esto es una cadena", [2,"f"]]

print("podemos ver la lista")
print(l)
print("")
print("podemos escribir el primer elemento de la lista")
print(l[0])
print("")
print("podemos cambiar el segundo elemento de la lista")
l[1]=33
print(l)
print("")
print("podemos seleccionar una porcione de la lista")
new_l1 = l[0:2]
print(new_l1)
print("")
lista=[2,1,5,7,3]
print(lista)
print('print(len(lista))= '+str(len(lista)))
print('print(type(mylist)) = '+str(type(lista)))
print('print(lista[3]) = '+str(lista[3]))
print('print(lista[-1]) = '+str(lista[-1]))
print('print(lista[2:4]) = '+str(lista[2:4]))
print('print(lista[2:]) = '+str(lista[2:]))
print('print(lista[:2]) = '+str(lista[:2]))
print("")
print(lista)
print("lista.insert(2,9)")
lista.insert(2,9)
print(lista)
print(lista)
lista2=lista
print(lista)
print(lista2)
print("lista.extend(lista2)")
lista.extend(lista2)
print(lista)
print("lista.remove(1)")
lista.remove(1)
print(lista)
print("lista.pop(1)")
lista.pop(1)
print(lista)
print("del lista[4]")
del lista[4]
print(lista)
lista.sort()
print("lista.sort()")
print(lista)
lista.sort(reverse = True)
print("lista.sort(reverse = True)")
print(lista)
print("lista.clear()")
lista.clear()
print(lista)
lista=["F","H","A","v","b"]
print(lista)
lista.sort(key = str.lower)
print(lista)


l1=["x","y","z"]
l2=[1,2,3]
l3=l1+l2 #igual que extend
print(l1)
print(l1)
print(l3)
l1.append(l2)
print(l1)



