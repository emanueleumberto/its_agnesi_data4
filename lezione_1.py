# Questo è un commento
# ctrl + ù -> attiva/disattiva commento

# Python NON è un linguaggio fortemente tipizzato
# String miaVar -> Java -> fortemente tipizzato

miaVar = 5
# print(miaVar, type(miaVar))
miaVar = "testo"
# print(miaVar, type(miaVar))
miaVar = True
# print(miaVar, type(miaVar))

# Nomenclatura di un elemento python
# CamelCase | PascalCase | SnakeCase
nomeDatoVariabile = 0 # CamelCase
NomeDatoVariabile = 0 # PascalCase
nome_dato_variabile = 0 # SnakeCase
nomedatovariabile = 0
NOME_DATO_COSTANTE = 0 # Convenzione per le Costanti

# Assegnazioni singole
x = 1
y = 2
z = 3

# Assegnazioni multiple
x,y,z = 1,2,3
x = y = z = 1

# Tipi di dato in python
# - int     -> numerico intero      -> d = 5
# - float   -> numerico decimale    -> d = 5.5
# - string  -> testo                -> d = "testo"
# - boolean -> True/False           -> d = True
# - none    -> None                 -> d = None

# Funzioni predefinite in Python
# print(args)   -> Funzione che stampa nel terminale il valore di args
# type(var)     -> Funzione che restituisce il tipo di dato di una variabile
# input()       -> FUnzione che permette l'inserimento di valori da terminale
# len(str)      -> Funzione che restituisce la lunghezza di una stringa
# help(func)    -> Retituisce la documentazione di una funzione passata come parametro

# Funzioni predefinite di Casting
# int(param)    -> resituisce il valore inserito in formato int
# float(param)  -> restituisce il valore inserito in formato float
# str(param)    -> restituisce il valore inserito in formato string
# bool(param)   -> restituisce il valore inserito in  format boolean
#   bool(0) | bool('') | bool([]) | bool(()) | bool({}) -> False

miaVar = "sono una Stringa"
print(miaVar)
print(type(miaVar))
print(len(miaVar))
nome = 'Mario Rossi' # input("Inserisci un nome: ")
print("Il nome che hai inserito è ", nome)
age = '25' # input("Inserisci età: ") # -> string
eta = int(age) # trasformo la stringa in un valore intero
# eta = float(age) # trasformo la stringa in un valore decimale
# eta = bool(age) # trasformo la stringa in un valore booleano
print(eta, type(eta))
print("FINE")

# String in python
# Per creare una stringa in python si utilizzano ' ' o " "
# Per creare una stringa multiriga si utilizzano ''' ''' o """ """
# Possiamo accedere ai singoli caratteri di una stringa tramite l'indice [i]
# Possiamo selezionare porzioni di stringa [n:m]
# Metodi predefiniti per manipolare una stringa
#   lower() | upper() | strip() | replace() | split() | format()

multiStr = """ Sono
            una 
            stringa"""
#      0123456789....
str = "Sono una Stringa" # stringa a singola riga
print(str[1])
print(str[5:8])
print(str[:8])
print(str[5:])
print(str[-5:-1])
print(str[-7:])

print(str.lower()) # Restituisce una copia della stringa in minuscolo
print(str.upper()) # Restituisce una copia della stringa in maiuscolo
print(str.strip()) # Restituisce una copia della stringa in senza spazi inizio/fine
print(str.replace('n', 'x')) # Restituisce una copia della stringa con ii valori sostituiti
print(str.split(' ')) # Restituisce un contenitore con portzioni di stringa tagliate in base ad un separatore
print(str)

nome = "Mario"
cognome = "Rossi"
eta = 25
# saluta = "Ciao " + nome + " " + cognome + " anni " + eta + " sono una stringa!"
saluta = "Ciao {} {} anni {} sono una stringa!"
print(saluta.format(nome, cognome, eta))
saluta = "Ciao {1} {0} anni {2} sono una stringa!"
print(saluta.format(cognome, nome,  eta))
#                      0       1     2
saluta = "Ciao {name} {lastname} anni {age} sono una stringa!"
print(saluta.format(name = nome, lastname = cognome, age = eta))

print(f"Ciao {nome} {cognome} anni {eta} sono una stringa!")

# if-else
# if condizione:
#     istruzione
# else:
#    istruzione

age = 20
if age >= 18:
    print("Maggiore di 18")
else:
    print("Minore o uguale di 18")
    
    
# Sistema Registrazione Utente
# Stai sviluppando un semplice programma da terminale 
# per registrare un utente e mostrare un riepilogo formattato.

# Il programma deve:
# Chiedere all’utente: nome, cognome, età
#Eseguire le seguenti operazioni:
# - Convertire l’età da stringa a intero
# - Calcolare la lunghezza del nome e cognome
# Trasformare:
# - nome → maiuscolo
# - cognome → minuscolo
# Stampare un riepilogo con:
# - nome completo formattato
# - età
# - lunghezza nome e cognome
# - tipo della variabile età

# Usare obbligatoriamente:
# - input()
# - print()
# - type()
# - len()
# Usare almeno 2 metodi delle stringhe:
# .upper()
# .lower()
# .strip()
# Inserire controlli if per:
# età negativa
# nome vuoto