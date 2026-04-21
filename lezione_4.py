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



