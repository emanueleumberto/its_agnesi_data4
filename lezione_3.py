# Collection
# List | Tuple | Set | Dictionary
# - List: Collezioni di dati ORDINATE, MODIFICABILI e permettono duplicati.
# -> v = ['Roma', 'Milano', 'Napoli']
# - Tuple: Collezioni di dati ORDINATE, IMMUTABILI e permettono duplicati.
# -> v = ('Roma', 'Milano', 'Napoli')
# - Set: Collezioni di dati NON ORDINATE e per questo non indicizzabili, 
#        non modificabili e non permettono duplicati
# -> v = {'Roma', 'Milano', 'Napoli'}
# - Dictonary: Collezioni di dati ORDINATE e modificabili ma non permettono duplicati
# -> v = {"nome": "Mario", "cognome": "Rossi", "citta": "Roma"}

# List
# Collezioni di dati ORDINATE, MODIFICABILI e permettono duplicati.
# è possibile creare liste, tuple, set con valori dello stesso tipo e di tipo diverso
# list() | type() | len() | count(val)
# Accedere ad elementi di una lista tramite un indice
# l[i] | l[i:i] | l[:i] | l[i:] | l[-i:-i]
# Modificare elementi di una lista tramite un indice
# l[i] = 'nuovo valore' | l[0: i] = ['val1', '...', 'valN']
# Aggiungere elementi ad una lista tramite append('val) | insert(index, 'val')
# Rimuovere elementi da una lista 
# remove(val) | pop() | pop(index) | del l[index] | del l | clear()
# Ordinare una lista sort() | sort(reverse=True)
# Copiare una lista nl = l.copy() | nl = list(l)
# Unire due o piu liste con extend(newList)
# Iterare Liste con For | While
# for ele in list:
#    istruzioni

l = ['Roma', 'Milano', 'Napoli'] # []
print(l, type(l))
l = list(('Roma', 'Milano', 'Napoli', 'Roma'))
print(l, type(l))
print(len(l))
print(l.count('Roma'))

#       0       1          2        3       | indexing
l = ['Roma', 'Milano', 'Napoli', 'Roma'] 
#    |      |         |         |      |
#    0      1         2         3      4    | slicing
#   -4     -3        -2        -1      0
print(l[1]) # indexing 
print(l[3]) # indexing

print(l[1:3]) # slicing
print(l[:2]) # slicing
print(l[1:]) # slicing
print(l[-3:-1]) # slicing

# Modificare una lista
l[1] = "Firenze"
print(l)
l[1:3] = ['Torino', "Udine"]
print(l)

# Inserire in una lista
l.append('Cagliari')
print(l)
l.insert(2, "Palermo")
print(l)

# Rimuovere da una lista
# l.remove('Roma')
# print(l)
# l.pop()
# print(l)
# l.pop(1)
# print(l)
# del l[1]
# print(l)
# l.clear()
# print(l)
# del l
# print(l)

# Ordinare una lista
l.sort()
print(l)
l.sort(reverse=True)
print(l)

print("-----------------------------------------------------")
# Copiare una lista
nl = l # errore non sto facendo una copia ma leggo la stessa lista 
nl = l.copy() # copia di una lista
nl = list(l) # copia di una lista

nl.append("Parigi")
print(nl)
print(l)

# Unire due o più liste
l2 = ['Firenze', 'Bari', 'Latina', 'Viterbo']
l.extend(l2)
print(l)

# Iterare Liste
  
i = 0
while i < len(l):
    print(l[i])
    i += 1

print("--------------------------")

for ele in l: 
    print(ele)

# Deve contenere tutte le città della lista principale che terminano per 'o'
searchList = [] 
for ele in l: 
    if ele[-1] == 'o':
        searchList.append(ele)
        
print(searchList)
