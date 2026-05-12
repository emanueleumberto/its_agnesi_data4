# Lettura e scrittura su file


import os

filename = 'miofile.txt'

try:
    # Controllo se il file esiste, altrimenti lo crea.
    if not os.path.exists(filename): # Controllo se il file esiste
        print('File non presente')
        open(filename, 'x') # Apre il file se presente o lo crea
        print(f'File {filename} created.')
    
    # Leggo il file in modalità scrittura e scrivo del testo 
    # in modalità sovrascrittura
    f = open(filename, 'w')
    f.write('Questo è un testo generato da python... \n')
    f.close()
    
    f = open(filename, 'a')
    f.write('Altro testo generato da python... \n')
    f.close()
    
except Exception as err:
    print('Error: ', err)
else:
    print('Scrittura file completata')
finally:
    f.close()
    
    
# Leggo un file
try:
    print(f'Lettura del file {filename}')
    f = open(filename, 'r')
    txt = f.read() # Legge il contenuto di un file e lo salva in una variabile
    # txt = f.read(10) # Legge i primi 10 caratteri di un file e lo salva in una variabile
    # txt = f.readline() # Legge la prima riga di testo contenuta in un file
    # txt = f.readlines() # Legge tutte le righe di testo contenute in un file
    print(txt)
except Exception as e:
    print('Error: ', err)
else:
    print('Lettura file completata')
finally:
    f.close()
    

# Controllo se il file esiste e lo cancello
if os.path.exists(filename):
    os.remove(filename)
    print(filename + ' deleted!')