import doctest

# Finden Sie den oder die Fehler im folgenden Skript
# Hinweis: Es sind 2 Syntaktische und 2 semantische Fehler enthalten.
     
def fibonacci(n):
    """ 
    Iterative Berechnung der Fibonacci-Zahl für n
    
    Doctests:
    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(10) 
    55
    >>> 
    #>>> fibonacci(40)
    #102334155  
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__": 
    doctest.testmod()