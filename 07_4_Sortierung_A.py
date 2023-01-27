# •	Entwickeln Sie einen Algorithmus, der eine Liste von Texten sortieren kann. 
#   In Python können Sie zwei Texte direkt mit den Vergleichsoperatoren verglichen werden, 
#   so wie dies auch bei Zahlen möglich ist

from os import system
from mycolors import *

einkaufsliste = [ "Brot", "Wurst", "Eier", "Milch", "Käse", "Nutella", "Bier" ]
gehaltsliste = [ 1700, 2500, 2100, 2100, 1200, 1800, 3500 ]

def sort_asc( liste ):
    return sorted( liste )

def sort_desc( liste ):
    return sorted( liste, reverse=True )

system( "cls" )

print( green( "-----------------------------" ) )
print( yellow( "Sortierte Liste je nach Funktion" ) )
print( green( "---" ) + cyan( "DESC" ) + green( "----------------------" ) )
print( *sort_desc( gehaltsliste ) )
print( green( "---" ) + cyan( "ASC" ) + green( "-----------------------" ) )
print( *sort_asc( einkaufsliste ) )
print( green( "-----------------------------" ) )
