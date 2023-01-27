# •	Entwickeln Sie einen Algorithmus, der eine Liste von Texten sortieren kann. 
#   In Python können Sie zwei Texte direkt mit den Vergleichsoperatoren verglichen werden, 
#   so wie dies auch bei Zahlen möglich ist

from os import system
from mycolors import *

# // low  --> Starting index,
# // high  --> Ending index
# quickSort(arr[], low, high) {

#   // Till starting index is lesser than ending index
#   if (low < high) {

#     // pi is partitioning index,
#     // arr[p] is now at right place
#     pi = partition(arr, low, high);

#     // Before pi
#     quickSort(arr, low, pi - 1);
#     // After pi
#     quickSort(arr, pi + 1, high);
#   }
# }

einkaufsliste = [ "Brot", "Wurst", "Eier", "Milch", "Käse", "Nutella", "Bier" ]
gehaltsliste = [ 1700, 2500, 2100, 2100, 1200, 1800, 3500 ]

def quickSort( liste ):
    swapped = False
    for arr in range( len( liste ) ):
        for elem in range( 0, len(liste) - arr - 1 ):
            if liste[ elem ] > liste[ elem + 1 ]:
                temp = liste[ elem ]
                liste[ elem ] = liste[ elem + 1 ]
                liste[ elem + 1 ] = temp
                swapped = True
        if not swapped:
            break

def quickSort_desc( liste ):
    swapped = False
    for arr in range( len( liste ) ):
        for elem in range( 0, len(liste) - arr - 1 ):
            if liste[ elem ] < liste[ elem + 1 ]:
                temp = liste[ elem ]
                liste[ elem ] = liste[ elem + 1 ]
                liste[ elem + 1 ] = temp
                swapped = True
        if not swapped:
            break

system( "cls" )

bubbleSort( einkaufsliste )
bubbleSort( gehaltsliste )

print( green( "-----------------------------" ) )
print( yellow( "Sortierte Liste mit Quick Sort Algorithmus" ) )
print( green( "---" ) + cyan( "ASC" ) + green( "-----------------------" ) )
print( *einkaufsliste )
print( *gehaltsliste )

bubbleSort_desc( einkaufsliste )
bubbleSort_desc( gehaltsliste )

print( green( "---" ) + cyan( "DESC" ) + green( "----------------------" ) )
print( *einkaufsliste )
print( *gehaltsliste )
print( green( "-----------------------------" ) )
