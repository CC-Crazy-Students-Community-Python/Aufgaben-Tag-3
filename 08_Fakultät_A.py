# •	Entwickeln Sie einen Algorithmus, der die Fakultät einer beliebigen Zahl berechnen kann
#   o	Nutzen Sie als Entwurfsmuster die Iteration

import random
import os

def factorial( zahl ): 
    match zahl:
        case z if z < 0:
            print( "Negative Fakultäten gibt es nicht" )
        case z if z == 0:
            return 1
        case other:
            factor = 1
            while( zahl > 1 ):
                factor *= zahl 
                zahl -= 1
            return factor

zahlen = {
    random.randint( 1, 20 ),
    random.randint( 1, 20 ),
    random.randint( 1, 20 ),
    random.randint( 1, 20 ),
    random.randint( 1, 20 ),
    random.randint( 1, 20 ),
    random.randint( 1, 20 )
}

os.system( "cls" )

print( "\033[92m--------------------------" )
print( "\033[93mIterative Fakltät" )
print( "\033[92m--------------------------\033[0m" )
for zahl in zahlen:
    print( "\tFakultät von", str( zahl ), "ist", factorial( zahl ) )
print( "\033[92m--------------------------\n\033[0m" )
