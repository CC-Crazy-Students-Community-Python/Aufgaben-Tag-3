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

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

system( "cls" )

quicksort( einkaufsliste )
quicksort( gehaltsliste )

print( green( "-----------------------------" ) )
print( yellow( "Sortierte Liste mit Quick Sort Algorithmus" ) )
print( green( "---" ) + cyan( "ASC" ) + green( "-----------------------" ) )
print( *einkaufsliste )
print( *gehaltsliste )
