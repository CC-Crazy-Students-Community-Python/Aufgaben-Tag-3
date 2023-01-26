# •	Entwickeln Sie einen Algorithmus, der die Fibonacci-Zahlenfolge bis zur Zahl 20. Zahl ausgibt
#   Ausgabe einer Liste in Iterativer Version

import os
fibonacci_zahlen=[]

def fibonacci( fibn ):
    erste = 1
    zweite = 1
    for fib in range( fibn ):
        match fib:
            case 1: fib = "0"
            case 2: fib = "0", "1"
            case other: fib = "0", erste, zweite
        fib = erste + zweite
        zweite = erste
        erste = fib
        fibonacci_zahlen.append( fib )
    return fibonacci_zahlen

os.system( "cls" )

print( "\033[92m--------------------------" )
print( "\033[93mIterative Fibonacci Zahlenfolge bis 20. Zahl" )
print( "\033[92m--------------------------\033[0m" )
print( *fibonacci( 20 ) )
print( "\033[92m--------------------------\n\033[0m" )
