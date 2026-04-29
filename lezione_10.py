# La programmazione orientata agli oggetti (OOP) si basa su:
# •	classi → modelli
# •	oggetti → istanze

# Permette di:
# •	organizzare il codice
# •	modellare il mondo reale
# •	migliorare la riusabilità

# Definizione di classe
# class MiaClasse:
# Creazione di un oggetto:
# obj = MiaClasse()

# Metodi nell classi
# Un meto è una funzione definita all'interno di una Classe e serve a:
# •	operare sui dati di un oggetto
# •	definire il comportamento dell'oggetto
# •	incapsulare logica

# Differenza fondamentale
# Funzione  -> indipendente
# Metodo    -> legato ad una classe

# Metodo di istanza -> il tipo più comune
# •	lavora sui dati dell'oggetto tramite 'self'

# Il parametro 'self' rappresenta:
# •	l'istanza corrente
# •	il collegamento tra il meto e l'oggetto

# Metodo di classe -> condiviso tra tutti gli oggetti della classe
# Un metodo di classe lavora sulla classe e non sull'istanza della classe
# si definisce utilizzando @classmethod

# Un linguaggio ad oggetti si poggia su 4 principi fondamentali:
# •	Incapsulamento
# •	Ereditarietà
# •	Polimorfismo
# •	Astrazione

# Incapsulamento è uno dei principi fondamentali della OOP
# Consiste nel nascondere i dati interni
# e permettere l'accesso ai dati solo tramite dei metodi controllati.
# Obiettivo: proteggere lo stato interno di un oggetto
# evitare modifiche non valide
# Rendere così il codice più sicuro e manutenibile

# Convenzioni e Sintassi per rappresentare un attributo public, protected, private:
# self.prop     -> public
# self._prop    -> protected
# self.__prop   -> private

class Automobile:
    
    totale = 0
    
    # costruttore
    def __init__(self, marca, modello, colore):
        self.__marca = marca
        self.__modello = modello
        self.__colore = colore
        self.__targa = None
        self.incrementa()
        
    # Metodo di istanza
    def info(self):
        print(f"Automobile: {self.marca} {self.modello} Colore:{self.colore} Targa: {self.targa}")
    
    # Metodo di classe
    @classmethod
    def incrementa(cls):
        cls.totale += 1 
    
    # Getter e Setter per modificare proprietà private  
    def getTarga(self):
        return self.targa
    
    def setTarga(self, targa):
        self.targa = targa
        
# auto = Automobile()
# auto.marca = 'Ford'
# auto.modello = 'Fiesta'
# auto.targa = 'CD456FG'
# print(auto)   
    
auto1 = Automobile('Fiat', 'Panda', 'Nero')
# print(auto1.totale)
auto2 = Automobile('Ford', 'Fiesta', 'Verde')
# print(auto2.totale)
auto3 = Automobile('Renault', 'Clio', 'Bianco')

auto1.targa = 'AB123CD'

# auto1.info()
# auto2.info()

print(Automobile.totale)

# print(auto1.targa)
print(auto1.getTarga())


#####################################################################

class ContoCorrente:
    
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome
        self.__saldo = 0
    
    # Metodo di istanza
    def info(self):
        print(f"Conto corrente di {self.__nome} {self.__cognome} Saldo: {self.__saldo}")
    
    # Property
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        if importo <= 0:
            raise ValueError("Importo non valido!!!")
        self.__saldo = importo        
    
c = ContoCorrente("Mario", "Rossi")
c.saldo = 200 # Sto utilizzando il metodo Setter
print(c.saldo) # Sto utilizzando il metodo Getter
c.info()