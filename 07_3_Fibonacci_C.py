# •	Entwickeln Sie einen Algorithmus, der die Fibonacci-Zahlenfolge bis zur Zahl 20. Zahl ausgibt
#   Ausgabe einer Liste an Hand der Mathematischen Formel

from math import sqrt
import os
fibonacci_zahlen=[]

def fibo( fib ):
    return int( ( ( ( 1 + sqrt( 5 ) ) ** fib ) - ( ( 1 - sqrt( 5 ) ) ** fib ) ) / ( 2 ** fib * sqrt( 5 ) ) )

def fibonacci( max ):
    fibn = 0
    cur = fibo( fibn )
    for i in range( max ):
        fibonacci_zahlen.append( cur )
        fibn += 1
        cur = fibo( fibn )
    return fibonacci_zahlen

os.system( "cls" )

print( "\033[92m--------------------------" )
print( "\033[93mFibonacci Zahlenfolge bis 20. Zahl nach Mathematischer Formel" )
print( "\033[93m\tFn = ( ( 1 + sqrt( 5 ) )**n - ( 1 - sqrt( 5 ) )**n ) / ( 2**n * sqrt( 5 ) )" )
print( "\033[92m--------------------------\033[0m" )
print( *fibonacci( 20 ) )
print( "\033[92m--------------------------\n\033[0m" )
