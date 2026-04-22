# - Set: Collezioni di dati NON ORDINATE e per questo non indicizzabili, 
#        non modificabili e non permettono duplicati
# -> s = {'Roma', 'Milano', 'Napoli'}
# set() | type() | len()
# NON è possibile accedere e/o modificare elementi di un set tramite un indice
# è possibile inserire un elemento in un set con il metodo add()
# è possibile rimuovere elementi da un set remove(val) | pop() | del l | clear()
# è possibile copiare un set ns = s.copy() | ns = set(s)
# è possibile unire due o più set con union() o |
#   Creare un nuovo set con tutti i dati presenti nei set uniti ma senza duplicati (Full Join)
# è possibile unire due o più set con intersection() o &
#   Creare un nuovo set con tutti i dati comuni presenti nei set (Inner Join)
# è possibile unire due o più set con difference() o -
#   Creare un nuovo set con tutti i dati presenti nel set principale (Left Join)
# è possibile unire due o più set con symmetric_difference()
#   Creare un nuovo set con tutti i dati NON comuni presenti nei set (Contrario Inner Join)
# è possibile iterare un set tramite un for o tramite while

s1 = {'Roma', 'Milano', 'Torino', 'Roma'}
s2 = set(('Napoli', 'Milano', 'Firenze', 'Roma'))
print(s1, type(s1), len(s1))
print(s2, type(s2), len(s2))

# s1.add('Firenze')
# s1.remove('Milano')
# s1.pop()

s_union = s1.union(s2)
print("Set union: ", s_union) # {'Roma', 'Torino', 'Napoli', 'Milano', 'Firenze'}
s_intersection = s1.intersection(s2)
print("Set intersection: ", s_intersection) # {'Milano', 'Roma'}
s_difference = s1.difference(s2)
print("Set difference : ", s_difference ) # {'Torino'}
s_symmetric_difference = s1.symmetric_difference(s2)
print("Set symmetric_difference : ", s_symmetric_difference ) # {'Firenze', 'Napoli', 'Torino'}

print("-----------------------------------------------------------------------")

# - Dictonary: Collezioni di dati ORDINATE e modificabili ma non permettono duplicati
# I Dizionari sonoun insieme di coppie chiave/valore, sono l'equivalente degli oggetti in altri linguaggi
# -> v = {"nome": "Mario", "cognome": "Rossi", "citta": "Roma"}
# dict() | type() | len()
# è possibile accedere ad un valore del dizionario tramite la sua chiave -> d[chiave]
# è possibile modificare valori di un dizionario tramite la sua chiave
# d[chiave] = nuovoValore | d.update({chaive: valore})
# è possibibile rimuovere elementi da un dizionario 
# pop(chiave) | del d[chiave] | del d | clear()
# è possibibile copiare un dizionario nd = d.copy() | nd = dict(d)
# è possibile iterare un dizionario tramite un for o tramite while

d1 = {"nome": "Mario", "cognome": "Rossi", "citta": "Roma", "anni": 25}
print(d1, type(d1), len(d1))
d2 = dict({"nome": "Giuseppe", "cognome": "Verdi", "citta": "Milano", "anni": 39})
print(d2, type(d2), len(d2))

d1["email"] = "m.rossi@example.com"
print(d1["nome"])
d1["cognome"] = "Rossini"
d1.update({"citta": "Torino", "anni": 99})
print(d1)

d1.pop("citta")
del d1["anni"]
print(d1)

dc = d2.copy()
dc = dict(d2)

for k in d2.keys(): # itera le chiavi di un dizionario
    print(k, d2[k])

for v in d2.values(): # itero i valori di un dizionario
    print(v)

for i in d2.items(): # itero una tupla composta da (chiave/valore) di un dizionario
    print(i)
