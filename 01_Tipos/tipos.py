#!/usr/bin/python3

# Tipos básicos :
#  Números
#    int
#    float
#    complex
#  Cadenas
#  Booleanos

#Casting int() float() str()

print("=======================")
x=5
y=3.14
yc=3.14e-3
z=2.0+7.0j
print (x," es un entero ",type(x))
print (y," es un float ",type(y))
print (yc," es un float notación cientifica ",type(yc))
print (z," es un complejo ",type(z))
print(str(x)+'*'+str(x)+'='+str(x*x))
print(str(yc)+'*'+str(yc)+'='+str(yc*yc))
print(str(z)+'*'+str(z)+'='+str(z*z))
print("=======================")
b=True
print (b," es un booleano ",type(b))
print("=======================")

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



