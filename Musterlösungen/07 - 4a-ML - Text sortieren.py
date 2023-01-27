# ML - Text sortieren

def sortieren(liste):
    # Ergebnisliste
    result = []
    
    # Die gesamte Liste durchgehen und jeden Wert der Ergebnisliste hinzufügen
    for text in liste:
        result = addToList(result, text)

    # Ergebnisliste zurückgeben
    return result
  
    
# Diese Funktion fügt der übergebenen Liste den Übergebenen Wert hinzu. Dabei wird der Wert alphabetisch einsortiert
def addToList(liste, wert):
    i = 0
    
    # Herausfinden an welcher Stelle der "Wert" eingefügt werden muss
    while i < len(liste):
        # Damit die Groß-/Kleinschreibung ignoriert wird, kann man das aktuelle ListenElement und den Wert für den Vergleich zu Kleinbuchstaben umwandeln
        if wert.lower() < liste[i].lower():
            break
        i += 1
    
    # Den Wert an dem gefundenen Index einfügen
    liste.insert(i, wert)
    
    return liste
    

# Testen der Funktion
liste = ["Affe", "ente", "Zebra", "Tiger", "97634", "Faultier", "Pinguin"]
print(liste)
print(sortieren(liste))





