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

# Vantaggi dell’incapsulamento
# Protegge i dati
# Riduce bug
# Migliora la manutenzione
# Permette validazione automatica
# Facilita il refactoring

# Errori comuni
# Usare variabili pubbliche sempre
# Usare get_ e set_ come in Java -> In Python è meglio: @property

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
        
    # Metodo migliore: usare le 'property'
    # Le 'property' sono il modo più Pythonico per fare incapsulamento.
    #Esempio con @property
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        if importo <= 0:
            print("Non puoi aggiungere importi negativi")
            return
        self.__saldo = importo        
    
c = ContoCorrente("Mario", "Rossi")
c.saldo = -25 # Sto utilizzando il metodo Setter
print(c.saldo) # Sto utilizzando il metodo Getter
c.info()

print('##############################################################')

# Esempio pratico
class Studente:
    
    # Attributo di classe
    __contatore_matricola = 0
    
    def __init__(self, nome):
        self.__matricola = self.__genera_matricola()
        self.__nome = nome
        self.__voti = []
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def voti(self):
        return self.__voti
        
    # Metodi di istanza
    def info(self):
        return f'Studente {self.__nome} matricola: {self.__matricola} voti: {self.__voti}'

    # Metodi di istanza
    def aggiungi_voto(self, voto):
        if voto > 0 and voto <= 30:
            self.__voti.append(voto)
        else:
            print('Hai aggiunto un valore errato')
    
    # Metodo di classe
    @classmethod
    def __genera_matricola(cls):
        cls.__contatore_matricola += 1
        matricola = cls.__contatore_matricola 
        if matricola < 10:
            matricola = f'US000{matricola}'
        elif matricola < 100:
            matricola = f'US00{matricola}'
        elif matricola < 1000:
            matricola = f'US0{matricola}'
        else:
            matricola = f'US{matricola}'
        return matricola
    
    
s1 = Studente('Mario Rossi')
s2 = Studente('Giuseppe Verdi')
s3 = Studente('Francesca Neri')
# Errore logico richiamare il metodo genera_matricola() al di fuori della classe studente
# s.genera_matricola() 

s1.aggiungi_voto(30)
s1.aggiungi_voto(25)
s1.aggiungi_voto(18)

print(s1.info())
