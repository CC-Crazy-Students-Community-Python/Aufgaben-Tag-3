# •	Entwerfen Sie einen Algorithmus, welcher alle Primzahlen von 2 bis 10000 auflisten kann
#   Originalversion aus dem Lehrgang mit Zeilenweiser Ausgabe

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
