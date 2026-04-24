from genuine.fake import GenuineFake as gf
import datetime as d

def genera_profili(n):
    profili_utente = []  
    while len(profili_utente) < n:
        date_of_birth = gf.date_of_birth()
        utente = {
            'nomeCompleto': gf.name(),
            'email': gf.email(),
            'dataDiNascita': date_of_birth,
            'eta': calcola_eta(date_of_birth),
            'indirizzo': gf.capital_city() + " " + gf.country(),
            'dataCreazione': d.date.today()
        }
        profili_utente.append(utente)
    return profili_utente 

def calcola_eta(dataDiNascita):
    today = d.date.today().strftime('%Y')
    data = dataDiNascita.split(' ')[2]
    return int(today) - int(data)
    
def stampa_profili(listaProfili):
    print('***** Lista di profili generati *****')
    for u in listaProfili:
        print('Nome completo', u['nomeCompleto'])
        print('Email', u['email'])
        print('Data di nascita', u['dataDiNascita'])
        print('Età', u['eta'])
        print('Indirizzo', u['indirizzo'])
        print('Data Creazione', u['dataCreazione'])
        print('-------------------------------------')
        print()


