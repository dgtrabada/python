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

#Operadores de comparación
 # ==  igual
 # !=  no igual
 #  >  mayor que
 #  <  menor que
 # >=  mayor o igual que 
 # <=  menor o igual que 

#Operadorres lógicos
 # and
 # or
 # not
 # is
 # is not

#operadores binarios
 # &  and
 # |  or
 # ^  xor
 # ~  not
 # << desplazar bits
 # >> desplazar bits

#Casting int() float() str()

print(" ======== int =======")
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
x+=2             #igual  x = x + 2
print(x)         # 7
x-=2
print(x)         # 5
x*=2
print(x)         # 10
x**=2
print(x)         # 100
x/=2
print(x)         # 50.0
x//=2
# Operadores de comparación
x=4
y=5
print(x == y)    # False
print(x != y)    # True
print(x >  y)    # False
print(x <  y)    # True
print(x >= y)    # False
print(x <= y)    # True

# Desplazamiento de bits
x=12             # 1100
y=10             # 1010
print(x&y)       # 1000 = 8
print(x|y)       # 1110 = 14
print(x^y)       # 0110 = 6
print(~x)        # -(1100+1) = -13
x >>= 3          # 1 
print(x)         # 1
x <<= 3          # 1000
print(x)         # 8

print(" ======== float =======")
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

print(" ======== complex  =======")
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


print(" ======== cadenas  =======")
s="Hola Mundo"
print (type(s))               # <class 'str'>
print (len(s))                # 10
print(s)                      # Hola Mundo
print(s[0])                   # H
print(s[0:4])                 # Hola
print(s[:4])                  # Hola
print(s[5:])                  # Mundo
print(s[-2])                  # d
print(s[-2:])                 # do
print(s[-4:-2])               # un
print(s[5:len(s)]+" "+s[0:4]) # Mundo Hola
print("Mundo" not in s)       # False
print("hola" not in s)        # True
print("Mundo" in s)           # True
print("hola" in s)            # False
print(s.upper())              # HOLA MUNDO
print(s.lower())              # hola mundo
print(s.lower().title())      # Hola Mundo
print(s.replace(" ","."))     # Hola.Mundo
print(s.split(" "))           # ['Hola', 'Mundo']
print(s.find("Mu"))           # 5
print(s.count("o"))           # 2
print(s.index("o"))           # 1
print(s.index("do"))          # 8 


print(" ======== booleanos  =======")
x=True
y=False
print(x and y)      # False
print(x or y)       # True
print(not x)        # False
print(x is y)       # False
print(x is not y)   # True


print (" ======== Casting =========" )
x=3.14
print(int(x))
print(float(x))
print(str(x))
# print("x ="+x) TypeError: can only concatenate str (not "float") to str
print("x = "+str(x))
