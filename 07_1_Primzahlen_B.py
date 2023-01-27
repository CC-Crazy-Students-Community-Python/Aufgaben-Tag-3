# •	Entwerfen Sie einen Algorithmus, welcher alle Primzahlen von 2 bis 10000 auflisten kann
#   Ausgabe einer Liste in verschiednen Versionen

import math
import os
primzahlen=[]

def ist_primzahl( primzahl ):
    for pz in range( 2, int( math.sqrt( primzahl ) ) + 1 ):
        if ( primzahl % pz ) == 0:
            return False
    return True

for primzahl in range( 2, 10000 ):
    if ist_primzahl( primzahl ):
        primzahlen.append( primzahl )

os.system( "cls" )

print( "\033[92m--------------------------" )
print( "\033[93mPrimzahlen bis 1000" )
print( "\033[92m--------------------------\033[0m" )
#print( primzahlen )                 #printed das Array
#print( *primzahlen, sep="," )       #printed Inhalt mit Seperator
print( *primzahlen )                #printed Inhalt mit default Seperator
