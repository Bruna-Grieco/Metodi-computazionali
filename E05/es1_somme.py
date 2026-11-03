import numpy as np 
import math # per la radice quadrata

"""
Creare il file python somme.py in cui vanno definite due funzioni:
- una funzione che restituisca la somma dei primi n numeri naturali, con n da passare tramite un argomento;
- una funzione che restituisca la somma delle radici dei primi n numeri naturali, con n da passare tramite un argomento.
Creare uno script python che importi il modulo somme appena creato e ne utilizzi le funzioni
Esaminare la cartella di lavoro
"""

# modulo python: file .py che contiene codice riutilizzabile
# per la prima funzione scelgo di usare range() perchè più veloce ripetto al for
   
def somma_n_naturali(n):
    som = 0 
    for i in range(1, n+1):
        som = som + i 
    return som

def somma_radici(n):
    som = 0.0
    for i in range(1, n+1):
        som = som + math.sqrt(i)
    return som 

"""
Modificare il file somme.py aggiungendo:
- una funzione che restituisca la somma e il prodotto dei primi n numeri naturali, con n da passare tramite un argomento;
- una funzione che restituisca la somma per i che va da 0 ad n di i^alpha, con n da passare tramite un argomento e alpha
  da passare come argomento opzionale con valore di default pari a 1.
Modificare lo script python che importa il modulo somme in modo da utilizzare le funzioni appena create.
"""

def prodotto(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

def somma_i(n, alpha = 1):
    sum = 0
    for i in range (0, n+1):
        sum = sum + pow(i, alpha)
    return sum