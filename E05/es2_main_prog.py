import numpy as np
from es2_class_prog import configurazione_strumento

# creo una lista fittizia di oggetti configurazione_strumento con raggi e risoluzioni diverse
elenco_config = [
    configurazione_strumento(raggio=20.0, risoluzione_temporale=0.5),
    configurazione_strumento(raggio=15.0, risoluzione_temporale=0.2),
    configurazione_strumento(raggio=25.0, risoluzione_temporale=1.0)
]

# converto la lista in un array di numpy
array_config = np.array(elenco_config)

print("--- Prima dell'ordinamento ---")
for configurazione in array_config:
    print(configurazione)

# uso np.sort() per ordinare l'array sfruttando i metodi di confronto (__lt__ e __gt__)
array_ordinato = np.sort(array_config)

print("\n--- Dopo l'ordinamento (per risoluzione temporale) ---")
for configurazione in array_ordinato:
    print(configurazione)