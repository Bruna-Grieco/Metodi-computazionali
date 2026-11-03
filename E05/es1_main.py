"""
Creare il file python somme.py in cui vanno definite due funzioni:
- una funzione che restituisca la somma dei primi n numeri naturali, con n da passare tramite un argomento;
- una funzione che restituisca la somma delle radici dei primi n numeri naturali, con n da passare tramite un argomento.
Creare uno script python che importi il modulo somme appena creato e ne utilizzi le funzioni
Esaminare la cartella di lavoro
"""

import es1_somme

print ("Il programma eseguirà la somma dei primi n numeri naturali.")
N = input ("Inserire n: ")
n = int (N)

risultato_somma = es1_somme.somma_n_naturali(n)
print("Risultato somma:", risultato_somma)

print ("\nIl programma eseguirà la somma delle radici dei primi n numeri naturali.")
risultato_radici = es1_somme.somma_radici(n)
print("Risultato radici:", risultato_radici)


"""
Modificare il file somme.py aggiungendo:
- una funzione che restituisca la somma e il prodotto dei primi n numeri naturali, con n da passare tramite un argomento;
- una funzione che restituisca la somma per i che va da 0 ad n di i^alpha, con n da passare tramite un argomento e alpha
  da passare come argomento opzionale con valore di default pari a 1.
Modificare lo script python che importa il modulo somme in modo da utilizzare le funzioni appena create.
"""

print ("\nIl programma eseguirà il prodotto dei primi n numeri naturali.")
risultato_prodotto = es1_somme.prodotto(n)
print ("Risultato prodotto:", risultato_prodotto)

print ("\nIl programma eseguirà la somma da 0 ad n dei numeri elevati ad alpha = 1 .")
risultato_sum = es1_somme.somma_i(n)
print ("Risultato sommatoria:", risultato_sum)