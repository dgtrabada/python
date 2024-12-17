#!/usr/bin/python3
import sys
#import os
#sys.path.append("/home/dani/python/ajedrez")
import random
from tablero import tablero


def print_help() :
    print (sys.argv[0]+" -help print this help")
    print (sys.argv[0]+" pinta el tablero inicial")
    print (sys.argv[0]+" -n X pinta X damas en el tablero sin darse jaque")


def n_damas(n):
    if n > 8:
        n=8
        print("no es posible poner mas de 8 damas en un tablero 8x8 sin que se amenacen entre sí")
    damas=[]
    x = ["a","b","c","d","e","f","g","h"] 
    y = [1, 2, 3, 4, 5, 6, 7, 8]
    #damos posiciones random sin que se amenacen en horizontal y vertical
    for i in range(n):
        damas.append("db_"+str(x[i])+str(y[i]))
    T=tablero(damas)
    intentos=0
    amenaza=True
    while(amenaza):
        intentos+=1
        #solo hay que comprobar las diagonales
        random.shuffle(y)
        for i in range(n):
            T.Lista_fichas[i].name="db_"+str(x[i])+str(y[i])
            T.Lista_fichas[i].setPos()

        amenaza=False
   
        for dama1 in range(len(T.Lista_fichas)):
           for dama2 in range(dama1+1,8):
               pos1 = T.Lista_fichas[dama1].getPosInt()
               pos2 = T.Lista_fichas[dama2].getPosInt()
               if (abs(pos1[0]-pos2[0]) == abs(pos1[1]-pos2[1])):
                   amenaza=True
    T.pintar_tablero()
    print(f"hemos probado {intentos}")

for i in range(1,len(sys.argv)):
    if sys.argv[i] == '-help' :
        print_help() 
    if sys.argv[i] == '-n' :
        n_damas(int(sys.argv[i+1]))
        
if (len(sys.argv) == 1):
    print("Tablero inicio")
    #blancas mayusculas y negras en minusculas
    inicio = ['tb_a1', 'cb_b1', 'ab_c1', 'rb_d1', 'db_e1', 'ab_f1', 'cb_g1', 'tb_h1',
            'pb_a2', 'pb_b2', 'pb_c2', 'pb_d2', 'pb_e2', 'pb_f2', 'pb_g2', 'pb_h2',
            'pn_a7', 'pn_b7', 'pn_c7', 'pn_d7', 'pn_e7', 'pn_f7', 'pn_g7', 'pn_h7',
            'tn_a8', 'cn_b8', 'an_c8', 'rn_d8', 'dn_e8' ,'an_f8', 'cn_g8', 'tn_h8'      
            ]
    T=tablero(inicio)
    T.pintar_tablero()
    T.cambiar_posicion_ficha("pb_d2","pb_d4")
    T.cambiar_posicion_ficha("cn_b8","cn_c6") 
    T.cambiar_posicion_ficha("ab_c1","ab_e3")
    T.comer_ficha("cn_c6","cn_d4")
    T.pintar_tablero()

 
