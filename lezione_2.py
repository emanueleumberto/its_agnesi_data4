# Operatori 
# - Operatori di assegnamento [=]
# - Operatori aritmetici [+ - * / % ** //]
# - Operatori aritmetici di assegnamento [+= -= *= /= %=]
# - Operatori di comparazione [>, <, ==, !=, >=, <=, is, is not, in, not in]
# - Operatori Logici [and or not xor]

# AND
# TRUE and TRUE  -> TRUE
# TRUE and FALSE -> FALSE
# FALSE and TRUE -> FALSE
# FALSE and FALSE -> FALSE

# OR
# TRUE or TRUE  -> TRUE
# TRUE or FALSE -> TRUE
# FALSE or TRUE -> TRUE
# FALSE or FALSE -> FALSE

# XOR
# TRUE xor TRUE  -> FALSE
# TRUE xor FALSE -> FALSE
# FALSE xor TRUE -> FALSE
# FALSE xor FALSE -> TRUE

# NOT
# NOT TRUE -> FALSE
# NOT FALSE -> TRUE

a = 10
b = 3

print(int(a/b))
print(a//b)
print(a%b)
print(3**3)

# a = a + 5
a += 5
print(a)

print(a > b)
print(a == b)
print(a != b)
print('i' in 'Ciao')
print('x' not in 'Ciao')


a = 10
b = 30
c = 3
print(a > b and b > c)
print(a > b or b > c)
print(not(a<b))

# Strutture di controllo
# - IF ELIF ELSE
#   if condizione:
#       blocco di istruzioni
#   elif condizione:
#       blocco di istruzioni
#   else:
#       blocco di istruzioni
#
# - if condizione: istruzioni else: istruzioni

if a > b:
    print("A è maggiore di B")
elif a == b:
    print("A è uguale a B")
else:
    print("A è minore di B")
    
# Strutture iterative
# - WHILE
#   while condizione:
#       blocco di istruzioni

num = 0
if num < 5:
    print("blocco di istruzioni IF")


while num < 5: 
    print("blocco di istruzioni WHILE")
    num += 1
  
while True:
    scelta = input("Inserisci il tuo nome oppure fine per terminare: ")
    if scelta == "fine":
        break
    
    print(f"Ciao {scelta}")
    
print("FINE")


# - FOR
#   for ele in iterable:
#       blocco di istruzioni