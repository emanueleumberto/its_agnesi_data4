# Stack delle chiamate

def func1():
    print('Start func1.')

def func2():
    print('Start func2.')
    func1()
    print('End func2.')
    
def func3():
    print('Start func3.')
    func2()
    print('End func3.')
    
# func3()
# print('FINE')

def ricorsiva(n):
    print('Funzione ricorsiva:', n)
    if n==0:
        print('Ricorsione finita.')
        return
    ricorsiva(n-1) # in attesa nello stack delle chiamate
    # riparte da qui dopo la fine della ricorsione
    print('Fine Funzione ricorsiva:', n)
    
#ricorsiva(5)

def fattoriale(n):
    if n==0:
        print('Ricorsione finita.')
        return 1
    print("Fattoriale:", n)
    return n * fattoriale(n-1)
        
result = fattoriale(5)
print(result)

# 5 * fattoriale(4) -> 5 * 24
# 4 * fattoriale(3) -> 4 * 6
# 3 * fattoriale(2) -> 3 * 2
# 2 * fattoriale(1) -> 2 * 1
# 1 * fattoriale(0) -> 1 * 1
# 1

import sys

# Python ha un limite di profondità dello stack
print(sys.getrecursionlimit())


# Contare le occorrenze di un elemento
# Scrivere una funzione ricorsiva che conti quante volte un valore appare in una lista.
# Scrivi una funzione -> def conta_elemento(lista, valore) che:
# ✔ restituisce il numero di volte in cui valore compare nella lista
# ✔ utilizza la ricorsione
# ❌ non usare .count()

# Caso base: lista vuota → ritorna 0
# Caso ricorsivo: se il primo elemento è uguale a valore → +1 poi continua con il resto della lista

# Debug richiesto -> Aggiungi logging per capire il flusso della funzione ricorsiva