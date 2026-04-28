# Logging

# Il logging in Python è il meccanismo standard per registrare eventi 
# che avvengono durante l’esecuzione di un programma.
# Serve per: debug, monitoraggio, audit, analisi di errori in ambienti di produzione.
# È preferibile a print() perché: è configurabile, supporta livelli di gravità, 
# può scrivere su più destinazioni (console, file, rete).

# modulo logging è già incluso nella standard library
# Logging ha un architettura basata su: Logger, Handler, Formatter e Level

# livelli di logging - Ordine di severità
# - DEBUG   -> Informazioni per il debug
# - INFO    -> Eventi normali funzionamento
# - WARNING -> Situazioni anomale ma non critiche
# - ERROR   -> Errori che impediscono il corretto funzionamento
# - CRITICAL-> Errori che bloccano completamente l'applicazione

# Handler: destinazione dei log
# - StreamHandler -> terminale
# - FileHandler   -> file
# - RotatingHandler -> dimensione di file

import logging as log


# log.basicConfig(level=log.DEBUG)

# log.debug("Messaggio di Debug")
# log.info("Messaggio di Info")
# log.warning("Messaggio di Warning")
# log.error("Messaggio di Error")
# log.critical("Messaggio di Critical")

##################################################################

# logger = log.getLogger('app_logger')
# logger.setLevel(log.DEBUG)

# logging.basicConfig(
#     level=logging.ERROR,
#     format="%(levelname)s - %(message)s",
#     force=True
#     )

# print(logging.getLogger().level) # Valore numerico del log impostato

# logger.debug("Messaggio di Debug")
# logger.info("Messaggio di Info")
# logger.warning("Messaggio di Warning")
# logger.error("Messaggio di Error")
# logger.critical("Messaggio di Critical")

##################################################################

# log.basicConfig() # Resetta il livello di Log impostato di default
# logger = log.getLogger('file_logger') # assegno un nome al Logger
# logger.setLevel(log.DEBUG) # Imposto il livello di severità del logger

# # Formatter -> Formato del messaggio
# formatter = log.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") #Formatto il log nel formato desiderato
# # Scrittura su file
# file_handler = log.FileHandler("app.log") # Imposto il file sul quale voglio salvare i log
# file_handler.setFormatter(formatter) # applico il formato desiderato al log

# logger.addHandler(file_handler) # aggiungo il file handler al logger

# logger.info("Applicazione avviata!")


##################################################################

from logging.handlers import RotatingFileHandler

log.basicConfig() # Resetta il livello di Log impostato di default
logger = log.getLogger('file_logger') # assegno un nome al Logger
logger.setLevel(log.DEBUG) # Imposto il livello di severità del logger

formatter = log.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") #Formatto il log nel formato desiderato
handler = RotatingFileHandler("app.log", maxBytes=1024) # Imposto il file sul quale voglio salvare i log e la dimensione massima del file
handler.setFormatter(formatter) # applico il formato desiderato al log

logger.addHandler(handler) # aggiungo il file handler al logger

logger.info("Applicazione avviata!")





