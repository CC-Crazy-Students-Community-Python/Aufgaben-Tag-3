# •	Entwickeln Sie einen Algorithmus, der eine Liste von Texten sortieren kann. 
#   In Python können Sie zwei Texte direkt mit den Vergleichsoperatoren verglichen werden, 
#   so wie dies auch bei Zahlen möglich ist

from os import system
from mycolors import *

students = [
    ( "Michael", "6", "12" ),
    ( "Peter", "1", "25" ),
    ( "Stephan", "4", "18" ),
    ( "Markus", "1", "14" )
]

def sort_asc( liste, dim ):
    return sorted( liste, key=lambda list: list[ dim ] )

def sort_desc( liste, dim ):
    return sorted( liste, reverse=True, key=lambda list: list[ dim ] )

system( "cls" )

print( green( "--------------------------" ) )
print( yellow( "Sortierte Liste je nach Dimension (Alter)" ) )
print( green( "---" ) + cyan( "DESC" ) + green( "----------------------" ) )
print( *sort_desc( students, 2 ) )
print( green( "---" ) + cyan( "ASC" ) + green( "-----------------------" ) )
print( *sort_asc( students, 2 ) )
print( green( "--------------------------" ) )
print( yellow( "Sortierte Liste je nach Dimension (Note)" ) )
print( green( "---" ) + cyan( "DESC" ) + green( "----------------------" ) )
print( *sort_desc( students, 1 ) )
print( green( "---" ) + cyan( "ASC" ) + green( "-----------------------" ) )
print( *sort_asc( students, 1 ) )
print( green( "--------------------------" ) )
