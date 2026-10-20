"""
Creare uno script Python che:
- chieda in input la vostra data di nascita;
- calcoli la vostra età in anni, giorni e secondi;
- stampi a schermo i risultati con stringhe formattatate in modo che appaiano incolonnati; 
per svolgere quetsa parte è necessario familiarizzare con il modulo datetime
"""

from datetime import datetime, timedelta

giorno = input ("Inserire il giorno di nascita: ")
mese = input ("Inserire il mese di nascita: ")
anno = input ("Inserire l'anno di nascita: ")

# creo la stringa della data di nascita e la converto in oggetto datetime (Formattazione stringhe)
str_nascita = "{}-{}-{}".format(giorno, mese, anno)
# trasformo la stringa di testo in un oggetto di tipo data
data_nascita = datetime.strptime(str_nascita, "%d-%m-%Y")

# data e ora attuale
datenow = datetime.now()
print("\nDi seguito l'elenco dell'anno, dell'ora e dei secondi attuali: ")
print(datenow.year, datenow.hour, datenow.second)


eta_anni = datenow.year - data_nascita.year
# controllo se il compleanno è già passato quest'anno
if datenow.month < data_nascita.month or (datenow.month == data_nascita.month and datenow.day < data_nascita.day):
    eta_anni = eta_anni - 1

differenza = datenow - data_nascita
giorni_vissuti = differenza.days
secondi_vissuti = differenza.total_seconds()

print("\n")
# il blocco ':<20' crea una colonna fissa di 20 caratteri
print("{:<20} {}".format("Età in anni:", eta_anni))
print("{:<20} {}".format("Età in giorni:", giorni_vissuti))
print("{:<20} {}".format("Età in secondi:", secondi_vissuti))
