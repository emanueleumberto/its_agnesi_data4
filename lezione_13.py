# In Python, un'eccezione è un evento che interrompe il flusso normale di esecuzione di un programma quando si verifica un errore.
# Le eccezioni servono a:
# •	intercettare errori
# •	evitare il crash dell'applicazione
# •	gestire condizioni anomale in modo controllato
# •	separare la logica applicativa dalla gestione degli errori

# In Python, tutte le eccezioni derivano dalla classe base: BaseException
# La gerarchia principale è:
# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  └── Exception
#       ├── ValueError
#       ├── TypeError
#       ├── IndexError
#       ├── KeyError
#       ├── ZeroDivisionError
#       └── FileNotFoundError

# ________________________________________
# Errori vs Eccezioni
# È importante distinguere:
# Errore sintattico   ->	errore nel codice
# Eccezione           ->	errore durante l'esecuzione

# Errore di sintassi
# if x = 5 -> Questo genera un SyntaxError.
# Il programma non parte.

# Eccezione a runtime
# print(10 / 0)
# Errore: ZeroDivisionError
# Il programma si interrompe durante l'esecuzione.

# ________________________________________
# Struttura base della gestione delle eccezioni
# La gestione delle eccezioni usa il costrutto:
# try -> except
# Sintassi base:
# try:
#     codice_rischioso
# except TipoEccezione:
#     gestione_errore
# Esempio:
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Divisione per zero non consentita")
# Output:
# Divisione per zero non consentita
# ________________________________________

# Flusso di esecuzione
# Il funzionamento logico è:
# 1.	Python esegue il blocco try
# 2.	se non ci sono errori, il blocco except viene ignorato
# 3.	se si verifica un'eccezione:
# o	Python interrompe il try
# o	cerca un except compatibile
# o	esegue il codice di gestione
# Diagramma logico:
# try
#  │
#  ├─ nessun errore → continua
#  │
#  └─ errore → except

# La sintassi completa è:
# try:
#     codice
# except TipoErrore:
#     gestione
# else:
#     eseguito se nessun errore
# finally:
#     sempre eseguito

# Best practice professionali
# Linee guida comuni:
# •	catturare eccezioni specifiche
# •	non usare except: generico
# •	non ignorare gli errori
# •	usare eccezioni personalizzate per logica di business

# Gestione di più eccezioni
# È possibile gestire diversi tipi di errore.
# Possiamo ottenere informazioni sull'errore.
# Il blocco else viene eseguito solo se non si verifica alcuna eccezione.
# Questo è utile per: logging | debugging | messaggi utente
# Il blocco finally viene sempre eseguito, indipendentemente dagli errori.
# Questo è molto usato per: chiudere file | liberare risorse | chiudere connessioni database

try:
    x = 10 # int(input('Inserisci un valore numerico: '))
    y = 2 # int(input('Inserisci un valore numerico: '))
    result = x / y
    # print(result) # Non viene eseguito se si verifica una eccezione
except ZeroDivisionError:
    print('Non puoi fare la divisione per 0')
except ValueError as e:
    print('Devi inserire un valore numerico!!')
    print(f'Errore: {e}') # Stampa il messaggio di errore specifico
else:
    print('La divisione è stata eseguita correttamente')
    print(result)
finally:
    print('Operazione terminata')


# Sollevare eccezioni manualmente
# Possiamo generare eccezioni usando: raise

try:
    age = -5 # int(input('Inserisci la tua età: '))
    if age < 0:
        raise ValueError('L\'età non può essere negativa')
except ValueError as e:
    print(f'Errore: {e}')
else:
    print(f'La tua età è: {age}')
    
    
################################################################

user = {'nome': '', 'età': 0, 'email': ''}

def inserisci_nome():
    nome = input('Inserisci un nome: ')
    if not nome.isalpha():
        raise ValueError('Il nome deve contenere solo lettere')
    user['nome'] = nome
    return user

def inserisci_eta():
    eta = input('Inserisci l\'età: ')
    if not eta.isdigit():
        raise ValueError('L\'età deve essere un numero intero')
    user = inserisci_nome()
    user['età'] = int(eta)
    return user

def inserisci_email():
    email = input('Inserisci l\'email: ')
    if '@' not in email:
        raise ValueError('L\'email non è valida')
    user = inserisci_eta()
    user['email'] = email
    return user

def inserisci_dati():
    try:
        dati = inserisci_email()
        print('Dati inseriti correttamente:', dati)
    except ValueError as e:
        print(f'Errore: {e}')

inserisci_dati()

# Permette di:
# capire dove è avvenuto l’errore
# ricostruire il flusso del programma
# Fondamentale per debugging

# Propagazione delle eccezioni
# Quando un’eccezione non viene gestita:
# sale nello stack (propaga)
# Si ferma solo quando trova un try/except
# Se non gestita: il programma termina


class Mia_eccezione(Exception):
    pass

try :
    if x == 10:
        raise Mia_eccezione('x non può essere 10')
except Mia_eccezione as e:
    print(f'Errore personalizzato: {e}')