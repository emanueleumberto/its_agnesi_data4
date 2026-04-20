# - Tuple: Collezioni di dati ORDINATE, IMMUTABILI e permettono duplicati.
# -> t = ('Roma', 'Milano', 'Napoli')
# tuple() | type() | len() | count(val)
# Accedere ad elementi di una tupla tramite un indice
# t[i] | t[i:i] | t[:i] | t[i:] | t[-i:-i]
# NON è possibile Modificare elementi di una tupla
# Unire due o piu tuple con +
# Copiare una tupla nt = tuple(t)
# è possibile fare l'unpack di una tupla
# (t1, t2, t3) = t
# Iterare Tuple con For | While
# for ele in list:
#    istruzioni


ta = ('Roma', 'Milano', 'Napoli')
print(ta, type(ta))
t = tuple(('Roma', 'Milano', 'Napoli', 'Roma'))
print(t, type(t), len(t), t.count('Roma'))

# Per modificare una tupla (NON SI FA)
l = list(t)
l.append('Torino')
t = tuple(l)
print(t, type(t), len(t), t.count('Roma'))

# Accedere ad elementi di una tupla tramite un indice
print(t[1])
print(t[1:3])

# Unire due o piu tuple con +
bigt = ta + t
print(ta)
print(t)
print(bigt)

# Copiare una tupla nt = tuple(t)
newt = tuple(bigt) # copia della tupla
print(newt)

# Unpack di una tupla
t = ('Roma', 'Milano', 'Napoli')
t1 = t[0]
t1, t2 = t[0], t[1]

(c1, c2, c3) = t
print(c1)
print(c2)
print(c3)

# Iterare Tuple
i = 0
while i < len(t):
    print(t[i])
    i += 1

print("--------------------------")

for ele in t: 
    print(ele)


# Crea una tupla chiamata persona contenente le seguenti informazioni:
# nome, cognome, età, città
# Stampa l'intera tupla
# Stampa separatamente ciascun elemento della tupla(Uno per riga)
# inserendo una etichetta chiara (Nome: , Cognome: ...)
# verifica se l'età è maggiore o uguale a 18 e stampa un messaggio 
# adeguato (La persona nome cognome è maggiorenne oppure minorenne)

persona = ("Mario", "Rossi", 25, "Roma")
print(persona)
(nome, cognome, eta, citta) = persona
print(f"Nome: {nome}, Cognome: {cognome}, Età: {eta}, Città: {citta}")
if(eta >= 18):
    print(f"La persona {nome} {cognome} è maggiorenne")
else:
    print(f"La persona {nome} {cognome} è minorenne")
    

# Un piccolo negozio di libri desidera gestire il proprio catalogo 
# in maniera semplice. 
# Ogni libro è rappresentato da una tupla contenente le seguenti 
# informazioni: 
# (titolo: str, autore: str, anno_pubblicazione: int, prezzo: float)
# Scrivi uno script Python che soddisfi i seguenti requisiti:
# - Crea una lista di almeno 5 libri, ciascuno rappresentato 
#   come una tupla nel formato sopra indicato.
# - Stampa tutti i libri presenti nel catalogo, uno per riga, 
#   formattando le informazioni in modo leggibile 
#   (es. “Titolo: ..., Autore: ..., Anno: ..., Prezzo: ...”).
# - Chiedi all’utente un anno, quindi stampa tutti i libri 
#   pubblicati dopo quell’anno.
# - Chiedi all’utente il nome di un autore e mostra 
#   tutti i libri scritti da quell’autore.
# - Calcola e stampa il prezzo medio dei libri presenti nel catalogo.
# - Trova e stampa il libro più costoso nel catalogo.
# - Poiché le tuple sono immutabili, spiega in un commento come 
#   potresti aggiornare il prezzo di un libro 