# Un linguaggio ad oggetti si poggia su 4 principi fondamentali:
# •	Incapsulamento
# •	Ereditarietà
# •	Polimorfismo
# •	Astrazione

# Ereditarietà
# Cos’è l’ereditarietà
# È un principio della programmazione orientata agli oggetti (OOP)
# Permette a una classe (figlia) di:
# riutilizzare codice di una classe (padre)
# estenderlo o modificarlo

class Animale:
    def __init__(self, nome):
        self.__nome = nome # Proprietà privata
    
    # Getter e setter
    @property
    def nome(self): return self.__nome
    @nome.setter
    def nome(self, nome): self.__nome = nome
        
    def faiVerso(self):
        return 'Animale fa un verso '
            
class Cane(Animale):
    
    def __init__(self, nome, razza):
        super().__init__(nome)
        self.__razza = razza
    
    def faiVerso(self):
        # Uso di super() -> permette di richiamare i membri della classe padre
        return super().faiVerso() + 'Bau'
     
class Gatto(Animale):
    def faiVerso(self):
        # Uso di super() -> permette di richiamare i membri della classe padre
        return super().faiVerso() + 'Miao'
    
class Coniglio(Animale):
    pass

bobby = Cane('Bobby', 'Labrador')
# print(bobby.faiVerso())

tom = Gatto('Tom')
# print(tom.faiVerso())

cony = Coniglio('Cony')


# Risultato
# Cane eredita da Animale
# Può usare il metodo faiVerso() senza ridefinirlo


# Polimorfismo
# permette di utilizzare oggetti diversi con la stessa interfaccia

def parla(animale):
    print(animale.faiVerso())
    
parla(bobby)
parla(tom)
parla(cony)

animali = [bobby, tom, cony]

for animale in animali:
    print(animale.faiVerso())
    
    
# Caso reale completo

class Utente:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password
    
    def accesso(self):
        return 'Accesso base'
    
class Admin(Utente):
    def accesso(self):
        return 'Accesso completo'
    
class Guest(Utente):
    def accesso(self):
        return 'Accesso limitato'

users = [
        Utente('MarioRossi', 'm.rossi@example.com', 'Pa$$w0rd!'),
        Admin('GiuseppeVerdi', 'g.verdi@example.com', 'Pa$$w0rd!'),
        Guest('FrancescaNeri', 'f.neri@example.com', 'Pa$$w0rd!')
        ]

for user in users:
    print(user.accesso())
    
    
# Astrazione
# Come si implementa in python
# Utilizzando il modulo built-in ABC (Abstract Base Classes)

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcolaArea(self):
        # metodo astratto non ha nessuna implementazione
        pass

class Rettangolo(Forma):
    
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    
    def calcolaArea(self):
        return self.base * self.altezza
    
class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio
    def calcolaArea(self):
        return self.raggio
        
         
forma1 = Rettangolo(25, 5)
forma2 = Cerchio(5)
forma3 = Forma() # TypeError

print('Fine')

