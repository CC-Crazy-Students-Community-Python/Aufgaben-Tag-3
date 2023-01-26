# •	Entwickeln Sie einen Algorithmus, der die Fibonacci-Zahlenfolge bis zur Zahl 20. Zahl ausgibt
#   Ausgabe einer Liste in Rekursiver Version

import os
fibonacci_zahlen=[]

def fibonacci( fibn ):
    if fibn > 1:
        return fibonacci( fibn - 1 ) + fibonacci( fibn - 2 )
    return fibn

for fib in range( 20 ):
    fibonacci_zahlen.append( fibonacci( fib ) )

os.system( "cls" )

print( "\033[92m--------------------------" )
print( "\033[93mRekursive Fibonacci Zahlenfolge bis 20. Zahl" )
print( "\033[92m--------------------------\033[0m" )
print( *fibonacci_zahlen )
print( "\033[92m--------------------------\n\033[0m" )
