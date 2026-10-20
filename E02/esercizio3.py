"""
Crea una lista con i nomi dei giorni della settimana;
Crea una lista con il nome dei giorni della settimana per tutto il mese di ottobre 2026;
Crea un dizionario che metta in relazione il giorno del mese di ottobre 2026 con il giorno della 
settimana;
Stampa la correlazione fra giorno del mese e della settimana a schermo.

"""

settimana = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']

"""
Uso le operazioni fra liste:
- creo una lista di 31 elementi: considero che ottobre 2026 ha il giorno 1 che è un giovedì e il 
giorno 31 che è un sabato;
-- poiché il giovedì nella lista settimana è all'indice 3, l'istruzione settimana[3:] prende gli 
elementi della lista "settimana" dall'elemento con indice 3 fino all'ultimo elemento della lista
-- poi ci sono 3 settimane intere
-- infine l'ultima settimana del mese inizia dal lunedì e finisce al sabato (indice 6)
"""
ottobre = settimana[3:] + settimana*3 + settimana[:6]


"""
Creo all'inizio un dizionario vuoto, che poi riempio con un ciclo for:
- La chiave è il numero del giorno del mese (1, 2, 3...)
- Il valore è il nome del giorno della settimana corrispondente
"""

dizionario_ottobre = {}
for i in range(len(ottobre)):
        dizionario_ottobre.update({ i+1: ottobre[i] })


for giorno_numero, giorno_nome in dizionario_ottobre.items():
    print("{} Ottobre 2026 -> {}".format(giorno_numero, giorno_nome))
