"""
Esercizio 2 - Diffusione 2D simmetrica
"""
import numpy as np

# A ogni passo "s", il walker si muove in una direzione angolare scelta casualmente e uniformemente tra 0 e 2pigreco. 
# Gli spostamenti sui singoli assi per ogni passo sono deltax e delta y (dati dalle formule della traccia)
# Nota: la funzione deve restituire lo spostamento totale rispetto al punto di partenza per ognuno degli N passi. 

def random_walk_2d(s, N):
    # genero in modo casuale gli angoli 
    angoli = np.random.uniform (0, 2*np.pi, size = N)
    # calcolo i singoli spostamenti elementari
    delta_x = s * np.cos(angoli)
    delta_y = s * np.sin(angoli)
    # calcolo lo spostamento tot.
    x_tot = np.cumsum(delta_x)
    y_tot = np.cumsum(delta_y)
    return x_tot, y_tot