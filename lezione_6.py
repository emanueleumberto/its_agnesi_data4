# Funzione Custom in Python 
# Serve per creare un blocco di istruzioni riutilizzabile più volte
# Per creare una funzione si utilizza l'operatore def
# def nomeFunc(?params): blocco di istruzioni
# per eseguire una funzione senza paramentri -> nomeFunc()
# per eseguire una funzione con paramentri -> nomeFunc(param1, param2, ..., paramN)
# per eseguire una funzione con paramentri variabile -> nomeFunc(*params)
# una funzione in python può avere o non avere dei valori di ritorno da riutilizzare nel codice


# Dichiarazione di funzione
def saluta():
    print("Ciao a tutti!!")
    
# Chiamata ad una funzione
saluta()

def somma(param1, param2):
    if param1 > 0 and param2 > 0 :
        sum = param1 + param2
        print(f"La somma tra i numeri {param1} e {param2} è {sum}")
    else :
        print(f"Non è possibile fare la somma tra i numeri {param1} e {param2}")
        
somma(5, 8)
somma(25, 90)
somma(23, 6)
somma(45, 9)

def sommaTutto(*nums):
    # print(nums)
    acc = 0
    for n in nums:
        acc += n
    
    print(f"La somma totale è {acc}")
    return acc
    
    
res1 = sommaTutto(3,5,8,0)
res2 = sommaTutto(3,5,1,4,7,9,3,5)
print(sommaTutto(res1, res2))



