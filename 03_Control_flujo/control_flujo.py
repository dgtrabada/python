#!/usr/bin/python3

#funciones, condicionaes y bucles

print ("========= funciones y condicionales ============")
def f(x):
  return x*x

x=2
print(f(x))   # 4



def f(x,y):
  if x < y :
    print ("es mayor")

f(1,2)        # es mayor
f(2,1)        #
f(1,1)        #

def f(x,y):
  if x < y :
    print ("es mayor")
  else:
    print ("es menor")

f(1,2)        # es mayor
f(2,1)        # es menor
f(1,1)        # es menor

def f(x,y):
  if x < y :
    print ("es mayor")
  elif x == y:
    print ("es igual")
  else:
    print ("es menor")

f(1,2)        # es mayor
f(2,1)        # es menor
f(1,1)        # es igual

f("A","B")    # es mayor
f("B","A")    # es menor
f("A","A")    # es igual



def f(x):
  if x > 0  and x <= 10 :
    print ("entre 0-10") 
  if x > 10  and x <= 20 :
    print ("entre 10-20") 
  if x > 20  and x <= 30 :
    print ("entre 20-30") 
  if x > 30  and x <= 40 :
    print ("entre 30-40") 

f(1)          # entre 0-10
f(22)         # entre 20-30

# podríamos pasar varios valores que retornar
def f(x, y):
  return x * 2, y * 3

a, b = f(1, 2)
print(a)      # 2
print(b)      # 6

#funcion anónima lambda

y = lambda x : x * x
print(y(2))   # 4

y= lambda x , y : x * y
print(y(2,5)) # 10




print ("========= bucles ============")
i = 1
while i < 5:
  print(i)
  i += 1
# 1
# 2
# 3
# 4

for i in range(5):
  print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(2,5):
  print(i)
# 2
# 3
# 4

for i in range(1,10,2):
  print(i)
# 1
# 3
# 5
# 7
# 9


l=[1,2,3,4,5]
for i in l:
  print(i)
# 1
# 2
# 3
# 4
# 5

l=["casa","perro",3,"fruta"]
for i in l:
  print(i)
# casa
# perro
# 3
# fruta

for i in range(0,len(l)):
  print(l[i])
# casa
# perro
# 3
# fruta


A=[[1,2],[3,4]]
for i in A:
  print (i)

# [1, 2]
# [3, 4]


for i in A:
  for j in i:
    print(j)
# 1
# 2
# 3
# 4



 
