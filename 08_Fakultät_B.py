# •	Entwickeln Sie einen Algorithmus, der die Fakultät einer beliebigen Zahl berechnen kann
#   o	Nutzen Sie als Entwurfsmuster die Rekursion, leider maximal 995 ansonsten kommt Error

import random
import os

def factorial( zahl ): 
    return 1 if ( zahl <= 1 ) else zahl * factorial( zahl - 1 )

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
print( "\033[93mRekursive Fakltät" )
print( "\033[92m--------------------------\033[0m" )
for zahl in zahlen:
    print( "\tFakultät von", str( zahl ), "ist", factorial( zahl ) )
print( "\033[92m--------------------------\n\033[0m" )
