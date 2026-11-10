import numpy as np
from es2_diff import random_walk_2d
import matplotlib.pyplot as plt

# parametri della simulazione
s = 1.0  # lunghezza del passo
N = 1000  # numero di passi
num_walker = 5

# PUNTO A: faccio un ciclo per i 5 walker 
for i in range(num_walker):
  # genero le posizioni X e Y per il walker corrente
  x, y = random_walk_2d(s, N)

  # lo traccio sul grafico 2D
  plt.plot(x, y, alpha=0.7, label=f"Walker {i+1}")

plt.xlabel("Asse X")
plt.ylabel("Asse Y")
plt.title("Random Walk 2D per 5 Walker (1000 passi)")
plt.legend()
plt.grid(True)
plt.show()

# PUNTO B: costruire un grafico con due pannelli: uno che ha il graph di A e uno che mostri il quadrato della 
#          distanza dal punto di partenza in funzione dei passi degli stessi 5 random walker

# Genero una figura con 2 pannelli (1 riga, 2 colonne) affiancati
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- primo pannello: Grafico 2D delle posizioni (Punto A) ---
for i in range(num_walker):
  x, y = random_walk_2d(s, N)
  ax1.plot(x, y, alpha=0.7, label=f"Walker {i+1}")

  # --- secondo pannello: Quadrato della distanza in funzione dei passi ---
  # Il quadrato della distanza è x^2 + y^2
  distanza_quadrata = x**2 + y**2

  # L'asse x dei passi va da 1 a N 
  passi = np.arange(1, N + 1)

  ax2.plot(passi, distanza_quadrata, alpha=0.7, label=f"Walker {i+1}")

# primo pannello
ax1.set_xlabel("Coordinata X")
ax1.set_ylabel("Coordinata Y")
ax1.set_title("Tracce 2D dei 5 Random Walker")
ax1.legend()

# secondo pannello
ax2.set_xlabel("Numero di passi")
ax2.set_ylabel("Quadrato della distanza")
ax2.set_title("Quadrato della distanza dal punto di partenza")
ax2.legend()


plt.tight_layout()
plt.show()