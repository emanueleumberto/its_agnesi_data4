# Una scuola vuole creare un piccolo sistema software per simulare la gestione degli studenti di una classe.
# Per evitare di inserire manualmente i dati, verrà utilizzato il modulo Python faker per 
# generare automaticamente studenti casuali.

# Il programma dovrà:
# - creare studenti fake
# - salvare le informazioni in collection Python
# - eseguire ricerche e statistiche
# - mostrare dati elaborati tramite funzioni

# Installazione libreria
# Prima di iniziare installare il modulo:

# pip install faker

# Requisiti del programma
# 1. Import del modulo Faker

# Importare e inizializzare Faker.
# from faker import Faker
# fake = Faker("it_IT")

# 2. Generazione studenti fake

# Creare una funzione:
# genera_studente()
# che restituisca un dizionario con: nome, cognome, email, età, voto medio

# Esempio struttura:
# {
#     "nome": "Mario",
#     "cognome": "Rossi",
#     "email": "mario@email.it",
#     "eta": 15,
#     "voto": 7.5
# }

# 3. Creazione lista studenti

# Creare una funzione:
# genera_classe(numero_studenti)
# che generi automaticamente una lista di studenti.

# Esempio: classe = genera_classe(20)

# 4. Funzioni obbligatorie
# Implementare le seguenti funzioni:

# - Visualizzazione studenti: mostra_studenti(classe) | Mostra tutti gli studenti.
# - Calcolo media classe: calcola_media(classe) | Restituisce la media voti della classe.
# - Ricerca miglior studente: miglior_studente(classe) | Restituisce lo studente con il voto più alto.
# - Ricerca studenti sufficienti: studenti_promossi(classe) | Restituisce tutti gli studenti con voto >= 6.
# - Raggruppamento età: Creare un dizionario che conti quanti studenti hanno la stessa età.
# Esempio output:
# {
#     14: 5,
#     15: 10,
#     16: 5
# }
# 5. Utilizzo delle collection
# Il programma deve usare obbligatoriamente:

# - list -> lista studenti
# - dict -> dati studente
# - set -> email uniche
# - tuple -> dati statistici finali

# 6. Controlli richiesti

# Gestire:
# - input errati
# - numero studenti negativo
# - lista vuota

# Utilizzare:
# try
# except

# 7. Menu interattivo
# Creare un menu testuale:

# 1. Genera classe
# 2. Mostra studenti
# 3. Calcola media
# 4. Miglior studente
# 5. Studenti promossi
# 6. Statistiche età
# 7. Esci

# Utilizzare:
# while
# if/elif

# 8. Output finale richiesto

# Il programma deve mostrare:

# elenco studenti
# media classe
# miglior studente
# numero promossi
# statistiche età
# Esempio di utilizzo atteso
# classe = genera_classe(10)

# mostra_studenti(classe)

# print(calcola_media(classe))

# print(miglior_studente(classe))

# Esempio output
# Mario Rossi - 7.5
# Luigi Verdi - 6.0
# Anna Bianchi - 8.5

# Media classe: 7.3

# Miglior studente:
# Anna Bianchi - 8.5