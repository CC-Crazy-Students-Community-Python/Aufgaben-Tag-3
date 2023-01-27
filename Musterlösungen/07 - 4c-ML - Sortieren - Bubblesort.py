# ML - Bubblesort

def bubblesort(liste):
    i = len(liste) - 1 # i beginnt als Index mit dem letzten Element der Gesamten Liste
    
    # Äußere Schleife, diese läuft solange bis das erste Element sortiert ist
    while i > 0:
        
        # Für die Innere Schleife muss immer wieder vorne angefangen werden
        for j in range(0, i):
            # Nun wird überprüft, ob vertauscht werden muss
            if liste[j].lower() > liste[j+1].lower():
                liste[j], liste[j+1] = liste[j+1], liste[j] # vertauschen der Elemente von j und j+1
          
        # Die neue Endposition wird um eins verkürzt, weil das im aktuellen Durchlauf größte Element automatisch an Position i zu finden ist.      
        i -= 1
        
    # Sortierte Liste zurückgeben
    return liste
    

# Alternativ eine noch kürzere Variante mit 2 for-Schleifen
def bubblesort2(liste):
    index = list(range(len(liste)-1, -1, -1))

    # Äußere Schleife, diese läuft solange bis das erste Element sortiert ist
    for i in index:
        # Für die Innere Schleife muss immer wieder vorne angefangen werden
        for j in range(0, i):
            # Nun wird überprüft, ob vertauscht werden muss
            if liste[j].lower() > liste[j+1].lower():
                liste[j], liste[j+1] = liste[j+1], liste[j] # vertauschen der Elemente von j und j+1

    # Sortierte Liste zurückgeben
    return liste
    
# Testen
liste = ["Affe", "ente", "Zebra", "Tiger", "97634", "Faultier", "Pinguin"]
print(bubblesort(liste))
print(bubblesort2(liste))