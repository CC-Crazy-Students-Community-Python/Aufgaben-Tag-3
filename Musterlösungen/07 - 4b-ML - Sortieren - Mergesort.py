# ML - Text sortieren

def sortieren(liste):
    result = []
    # Wenn zwei Elemente in der Liste vorhanden sind, dann werden diese sortiert und zurückgegeben
    if len(liste) == 2:
        if (liste[0].lower() > liste[1].lower()):
            result.append(liste[1])
            result.append(liste[0])
        else:
            result.append(liste[0])
            result.append(liste[1])
            
    # Ist nur ein Element in der Liste, dann wird dieses als Liste zurückgegeben
    elif len(liste) == 1:
        result.append(liste[0])
        
    # Sind mehr Elemente in der Liste, so muss diese in 2 Listen geteilt werden
    else:
        # Mitte der Anzahl der Elemente bestimmen
        mitte = len(liste) // 2
        
         # Aufteilen der Listen
        listeA = liste[:mitte]  # Bis zum Element an Position 'mitte' (exlusive) werden alle Elemente in die ListeA kiopiert
        listeB = liste[mitte:]  # Ab dem Element an Position 'mitte' (inklusive) werden alle Elemente in die ListeB kiopiert
        
        #print(listeA)
        #print(listeB)

        # Alternativ zu den beiden oberen Zeilen kann man das auch mit Schleifen einsortieren
        """
        listeA = []
        listeB = []
        
        for i in range(0, mitte):
            listeA.append(liste[i])
        
        for i in range(mitte, len(liste)):
            listeB.append(liste[i])
        
        # print(listeA)
        # print(listeB)
        """
        
        # Rekursive Aufrufe mit den Listen
        listeA = sortieren(listeA)
        listeB = sortieren(listeB)
        
        print(listeA)
        print(listeB)
        print()
        
        # Nach dem rekursiven Aufruf ergeben sich zwei sortierte Listen.
        # Diese beiden müssen nun miteinander verbunden werden
        i = 0
        j = 0
        
        while i < len(listeA) and j < len(listeB):
            if listeA[i].lower() > listeB[j].lower():
                result.append(listeB[j])
                j += 1
            else:
                result.append(listeA[i])
                i += 1
                
        # Die eventuell fehlenden Elemente einer der beiden Listen werden nun der Gesamtliste hinzugefügt
        result += listeA[i:]
        result += listeB[j:]
            
    return result
        

liste = ["Affe", "ente", "Zebra", "Tiger", "97634", "Faultier", "Pinguin"]
print(sortieren(liste))