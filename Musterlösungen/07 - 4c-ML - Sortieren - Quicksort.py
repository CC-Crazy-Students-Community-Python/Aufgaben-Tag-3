# ML - Sortieren Quicksort
# https://de.wikipedia.org/wiki/Quicksort

def quicksort(index_l, index_r):
    if index_l < index_r:
        teiler = teile(index_l, index_r)
        quicksort(index_l, teiler-1)
        quicksort(teiler+1, index_r)
    

def teile(index_l, index_r):
    pivot = liste[index_r].lower()
    i = index_l     # Erstes Element in der Liste
    j = index_r-1   # Links vom Pivot-Element
    
    # solange i an j nicht vorbeigelaufen ist 
    while i < j:
        # Suche von links ein Element, welches größer oder gleich dem Pivotelement ist
        while i < index_r and liste[i].lower() < pivot:
            i += 1
            
        # Suche von rechts ein Element, welches kleiner als das Pivotelement ist
        while j > index_l and liste[j].lower() >= pivot:
            j -= 1
        
        # Daten tauschen, falls i kleiner ist als j, also falls ein Tausch sinnvoll ist
        if i < j: 
            liste[i], liste[j] = liste[j], liste[i]
            
    # Tausche Pivotelement (liste[index_r]) mit neuer endgültiger Position (liste[i])
    # und gib die neue Position des Pivotelements zurück, beende Durchlauf
    if liste[i].lower() > pivot:
        liste[i], liste[index_r] = liste[index_r], liste[i]
        
    return i
        

# Testen
# Die Liste wird als globale Variable definiert. Dies dient dazu, dass sie im gesamten Quellcode verfügbar ist und nicht immer übergeben werden muss
global liste
liste = ["Affe", "ente", "Zebra", "Tiger", "97634", "Faultier", "Pinguin"]
print('Unsortierte Liste: ' + str(liste))
quicksort(0, len(liste)-1)
print('Sortierte Liste: ' + str(liste))