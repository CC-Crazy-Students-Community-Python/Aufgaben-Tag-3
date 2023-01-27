# •	Entwickeln Sie einen Algorithmus, der eine Liste von Texten sortieren kann. 
#   In Python können Sie zwei Texte direkt mit den Vergleichsoperatoren verglichen werden, 
#   so wie dies auch bei Zahlen möglich ist

from os import system
from mycolors import *

students = [ "Michael", "Peter", "Stephan", "Markus"]

def sort_asc( liste, getter ):
    return sorted( liste, key=getter.__getitem__ )

def sort_desc( liste, getter ):
    return sorted( liste, reverse=True, key=getter.__getitem__ )

newgrades = { "Markus": "1", "Michael": "6", "Peter": "1", "Stephan": "4" }

system( "cls" )

print( green( "-----------------------------" ) )
print( yellow( "Sortierte Liste je nach Item" ) )
print( green( "---" ) + cyan( "DESC" ) + green( "----------------------" ) )
print( *sort_desc( students, newgrades ) )
print( green( "---" ) + cyan( "ASC" ) + green( "-----------------------" ) )
print( *sort_asc( students, newgrades ) )
print( green( "-----------------------------" ) )
