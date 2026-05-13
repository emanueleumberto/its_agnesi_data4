# https://pypi.org/project/mysql-connector-python/
# pip install mysql-connector-python
# python_its_db

import mysql.connector as mc

# Connect to server
db = mc.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="python_its_db")

# Get a cursor
cursor = db.cursor()

# Execute a query
# cursor.execute("SELECT CURDATE()")

def crea_tabella_users():
    sql = 'CREATE TABLE IF NOT EXISTS users(\
	    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
        firstname VARCHAR(50) NOT NULL,\
        lastname VARCHAR(50) NOT NULL,\
        age INT NULL DEFAULT 18\
        );'
    cursor.execute(sql)
    print('Tabella Users creata con successo!')
    
def aggiungi_utente():
    try:
        nome = input('Inserisci nome: ')
        cognome = input('Inserisci cognome: ')
        eta = int(input('Inserisci età: '))
        
        sql = 'INSERT INTO users (firstname, lastname, age) VALUES (%s, %s, %s);' # Utilizzo dei segnaposto per i dati da sostituire in fase di esecuzione
        values = (nome, cognome, eta)
        cursor.execute(sql, values) #Eseguo la query SQL passandogli i valori da inserire
    
        db.commit() # Completa l'operazione
        
        if cursor._last_insert_id:
            print(f'Utente {nome} {cognome} salvato nel DB')
        
        
    except Exception as e:
        print('Problema nella scrittura sul DB')
        db.rollback() # Ripristina la condizione iniziale
    
def leggi_utente(id):
    sql = 'SELECT * FROM users WHERE id = %s'
    cursor.execute(sql, (id,)) # Una tupla deve avere almeno 2 valori
    
    utente = cursor.fetchone()
    return utente
    
def leggi_tutto():
    sql = 'SELECT * FROM users'
    cursor.execute(sql)
    
    return cursor.fetchall()
   
def modifica_utente(utente):
    nome = input(f'Modifica nome ({utente[1]}): ') or utente[1]
    cognome = input(f'Modifica cognome ({utente[2]}): ') or utente[2]
    eta = input(f'Modifica età ({utente[3]}): ') or utente[3]
    
    try:
        sql = 'UPDATE users SET firstname=%s, lastname=%s, age=%s WHERE id=%s'
        values = (nome, cognome, eta, utente[0])
        cursor.execute(sql, values)
        db.commit() # Completa l'operazione
    except Exception as e:
        print('Problema nella scrittura sul DB')
        db.rollback() # Ripristina la condizione iniziale

def elimina_utente(utente):
    try:
        sql = 'DELETE FROM users WHERE id = %s'
        cursor.execute(sql, (utente[0],)) # Una tupla deve avere almeno 2 valori
        db.commit() # Completa l'operazione
    except Exception as e:
        print('Problema nella scrittura sul DB')
        db.rollback() # Ripristina la condizione iniziale
    

# crea_tabella_users()
# aggiungi_utente()
mario = leggi_utente(1)
# lista = leggi_tutto()
# modifica_utente(mario)