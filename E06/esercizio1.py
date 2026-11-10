"""
Esercizio 1 - Distribuzioni di probabilità 
"""
import numpy as np
import matplotlib.pyplot as plt

# NOTA: CON PYTHON BISOGNA EVITARE IL PIU' POSSIBILE DI USARE I CICLI --> USARE ARRAY

def f(x):
  return (3 / 1000) * (x**2)

def distrib_prob_HitMiss(N): # ! Non serve passare x come parametro perchè lo genero dentro, ma devo passare N valori che voglio campionare

    # x varia in una distribuzione uniforme tra 0 e 10
    x = np.random.uniform (0, 10, size= N) #  # Voglio raccogliere N punti validi --> genero un array di N coordinate
    # y varia con una distrib. unif. da 0 e M con M valore massimo che può assumere f(x)
    # M è dato da f(10).
    y = np.random.uniform (0, 0.3, size= N) 
    
    # La condizione di Hit è questa: se y estratto è <= f(x), allora teniamo la x
    # Altrimenti, se y > f(X), lo scarto
    
    # impongo la condizione di Hit: restituisce un array di True/False
    mask = (y <= f(x))

    # filtro l'array x tenendo SOLO i valori dove la condizione è True
    x_accettate = x[mask]

    return x_accettate



# Genero 1000 valori con Hit or Miss
campione_hm = distrib_prob_HitMiss(1000)

# Creo l'istogramma per visualizzare la distribuzione Hitt or Miss
plt.hist(
    campione_hm, bins=30, density=True, alpha=0.6, color="g", label="Hit or Miss"
)
plt.xlabel("x")
plt.ylabel("Densità di probabilità")
plt.legend()
plt.show()


def cumulativa (N):
    z = np.random.uniform(0, 1, size=N)
    # formula dell'inversa x = C^{-1}(z) su tutto l'array
    x = (1000*z)**(1/3)
    return x 

# Genero 1000 valori con funzione cumulativa
campione_cumul = cumulativa(1000)

# Creo l'istogramma per visualizzare la distribuzione cumulativa
plt.hist(
    campione_cumul, bins=30, density=True, alpha=0.6, color="b", label="Cumulativa"
)
plt.xlabel("x")
plt.ylabel("Densità di probabilità")
plt.legend()
plt.show()



# Plotto i due istogrammi sovrapposti
plt.hist(
    campione_hm, bins=30, density=True, alpha=0.5, color="g", label="Hit or Miss",
)
plt.hist(
    campione_cumul, bins=30, density=True, alpha=0.5, color="b", label="Metodo Cumulativa",
)
plt.xlabel("x")
plt.ylabel("Densità di probabilità")
plt.title("Confronto tra Hit or Miss e Metodo della Cumulativa")
plt.legend()
plt.show()