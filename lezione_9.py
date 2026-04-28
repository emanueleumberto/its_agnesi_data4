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

# Comprehensions in python
# permettono di creare collezioni di dati in modo:
# -> Compatto
# -> leggibile
# -> efficiente

# è una sintassi compatta per creare collezioni come Liste, Set, Dizionari partendo da un iterabile 
# è un'alternativa più concisa al ciclo for

# List Comprehension
# [expression for item in iterable if condition]
numeri = [1,2,3,4,5]

# Soluzione utilizzando un ciclo For
quadrati = []
for val in numeri:
    q = val**2
    quadrati.append(q)

print(quadrati)

# Soluzione utilizzando List Comprehension
quadrati = [val**2 for val in numeri]
print(quadrati)

# Con utilizzo di una condizione
pari = [val for val in numeri if val % 2 == 0]
print(pari)

# Con utilizzo di if-else
elementi = ["pari" if val % 2 == 0 else "dispari" for val in numeri]
print(elementi)

# Liste annidate e matrici
# [[[[],[],[]],[],[]],[[],[],[]],[[],[],[]]]
#           0       1       2
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#          0 1 2   0 1 2   0 1 2
print(matrix[0][1])


# for n in range(0,10,2): print(n)
# lista_range = range(0,10,2)
# print(type(lista_range))
# print(type(numeri))

lista_range = [val for val in range(0,10,2)]
print(lista_range)

# Comprehension annidata
matrix = [[x*y for y in range(1,5)] for x in range(1,5)]
print(matrix)

#########################################################################
print('#########################################################################')

# List Comprehension
# [expression for item in iterable if condition]
numeri = [1,2,3,4,5]
quadrati = [val**2 for val in numeri]
print(quadrati)

# Set Comprehension
# {expression for item in iterable if condition}
numeri = [1,2,3,2,8]
unici = {val for val in numeri}
print(unici)

# Dict Comprehension
# {expression for item in iterable if condition}
numeri = [1,2,3,2,8]
diz = {val:val**2 for val in numeri}
print(diz)

# Uso di Comprehension con Liste
dati = [" Mario", "antonio", "FRANCESCA "]
dati_normalizzati = [nome.strip().capitalize() for nome in dati]
print(dati_normalizzati)

# Uso di Comprehension con Dizionari
prezzi = {'a': 10, 'b': 20, 'c': 30}
scontati = {k:v*0.9 for k,v in prezzi.items()}
print(prezzi)
print(scontati)

