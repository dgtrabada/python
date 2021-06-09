#!/usr/bin/python3

#Tipos básicos :
  #Números
    #int
    #float
    #complex
  #Cadenas
  #Booleanos

#Operadores aritméticos:
  # +  suma
  # -  resta
  # *  multiplicación
  # ** exponente
  # /  división
  # // división entera
  # %  modulo

#Operadores a nivel bit

#Casting int() float() str()

#int
x=5
y=2
print(type(x))   # <class 'int'>
print(x+y)       # 7
print(x-y)       # 3
print(x*y)       # 10
print(x**y)      # 25
print(x/y)       # 2.5
print(x//y)      # 2
print(x%y)       # 1

#float
x=3.14
y=2.72
print(type(x))   # <class 'float'>
print(x+y)       # 5.86
print(x-y)       # 0.41999999999999993
print(x*y)       # 8.5408
print(x**y)      # 22.472357891492628
print(x/y)       # 1.1544117647058822
print(x//y)      # 1.0
print(x%y)       # 0.41999999999999993

#float notación cientifica
x=3.14e-3
print(type(x))   # <class 'float'>
print(x*y)       # 0.008540800000000001

#complex
x=2.0 + 7.0j
y=2.0 - 7.0j
print(type(x))   # <class 'complex'>
print(x+y)       # (4+0j)
print(x-y)       # 14j
print(x*y)       # (53+0j)
print(x**y)      # (139718.62243609893+428122.7199034837j)
print(x/y)       # (-0.8490566037735849+0.5283018867924528j)
#print(str(x//y))# TypeError: can't take floor of complex number.
#print(str(x%y)) # TypeError: can't mod complex numbers.

x=True
y=False
print(type(x))   # <class 'bool'>
print(x+y)       # 1
print(x+x)       # 2
print(y+y)       # 0
print(x-y)       # 1
print(y-x)       # -1
print(x*y)       # 0
print(x**y)      # 1
print(y/x)       # 0.0
print(y//x)      # 0
print(x%x)       # 0



s="Hola Mundo"
print (s," es una cadena ",type(s))
print ("Tiene una longitud de "+str(len(s)))
print(s)
print(s[0])
print(s[0:4])
print(s[:4])
print(s[4:])
print(s[-2])
print(s[-2:])
print(s[-4:-2])
print(s[5:len(s)]+" "+s[0:4])
print("Mundo" not in s)
print("hola" not in s)
print("=======================")



