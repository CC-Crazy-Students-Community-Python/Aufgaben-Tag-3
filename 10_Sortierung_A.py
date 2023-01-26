# •	Entwickeln Sie einen Algorithmus, der eine Liste von Texten sortieren kann. 
#   In Python können Sie zwei Texte direkt mit den Vergleichsoperatoren verglichen werden, 
#   so wie dies auch bei Zahlen möglich ist

import math
import os

def ist_primzahl( primzahl ):
    prim = True
    if primzahl < 2:
        prim = False
    k = 2
    while prim and k <= math.sqrt( primzahl ):
        if primzahl % k == 0:
            prim = False
            break
        k += 1
    return prim

os.system( "cls" )

print( "\033[92m--------------------------" )
print( "\033[93mPrimzahlen bis 1000" )
print( "\033[92m--------------------------\033[0m" )
for primzahl in range( 2, 10000 ):
    if ist_primzahl( primzahl ):
        print( str( primzahl ) )
