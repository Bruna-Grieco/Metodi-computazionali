import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2025.csv"

df_eso = pd.read_csv(url, comment='#')
# dice a Pandas di ignorare tutte le righe del file che iniziano con il carattere # 

print(df_eso.columns) # p.to 2

print("\n estratto del DataFrame")
print(df_eso.head()) 

# dati del sistema solare per il confronto
solar_system = {
    'pl_name': ['mercurio', 'venere', 'terra', 'marte', 'giove', 'saturno', 'urano', 'nettuno'],
    'pl_orbper': [87.97, 224.7, 365.25, 686.98, 4332.59, 10759.22, 30685.4, 60189.0], # periodo orbitale (espresso in giorni)
    'pl_bmassj': [0.000174, 0.00256, 0.00315, 0.000338, 1.0, 0.299, 0.046, 0.054], # massa dei pianeti espressa in masse gioviane
    'pl_orbsmax': [0.387, 0.723, 1.0, 1.524, 5.204, 9.582, 19.201, 30.047], # semiasse maggiore: distanza media del pianeta dal Sole espressa in Unità Astronomiche
    'st_mass': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] # massa della stella attorno a cui i pianeti orbitano, espressa in masse solari
}
df_solar = pd.DataFrame(solar_system)


# p.to 4 grafico: massa del pianeta in funzione del periodo orbitale (log-log)
plt.figure(figsize=(8, 6))
plt.scatter(df_eso['pl_orbper'], df_eso['pl_bmassj'], alpha=0.5, label='Esopianeti', s=10)
plt.scatter(df_solar['pl_orbper'], df_solar['pl_bmassj'], color='red', marker='*', s=120, label='Sistema Solare')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Periodo Orbitale [giorni]')
plt.ylabel('Massa del Pianeta [$M_{Jup}$]')
plt.title('Massa del Pianeta vs Periodo Orbitale')
plt.legend()
plt.savefig('Exoplanets_massa_vs_periodorbit.png')
plt.show()


# p.to 5 grafico: semiasse maggiore in funzione del periodo orbitale (log-log)
plt.figure(figsize=(8, 6))
plt.scatter(df_eso['pl_orbper'], df_eso['pl_orbsmax'], alpha=0.5, label='Esopianeti', s=10) # con s regolo la grandezza dei marker 
plt.scatter(df_solar['pl_orbper'], df_solar['pl_orbsmax'], color='red', marker='*', s=120, label='Sistema Solare')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Periodo Orbitale [giorni]')
plt.ylabel('Semiasse Maggiore [$au$]')
plt.title('Semiasse Maggiore vs Periodo Orbitale')
plt.legend()
plt.savefig('Exoplanets_R_vs_periodorbit.png')
plt.show()


# p.to 6 grafico: massa stellare in funzione del periodo orbitale (log-log)
# produca un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale 
# distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente 
# legenda (gli altri tipi di esopianeti non vanno considerate nel grafico);
transit_df = df_eso.loc[df_eso['discoverymethod'] == 'Transit']
rv_df = df_eso.loc[df_eso['discoverymethod'] == 'Radial Velocity']
plt.figure(figsize=(8, 6))
plt.scatter(transit_df['pl_orbper'], transit_df['pl_bmassj'], alpha=0.5, label='Transit (Esopianeti)', s=10, color='royalblue')
plt.scatter(rv_df['pl_orbper'], rv_df['pl_bmassj'], alpha=0.5, label='Radial Velocity (Esopianeti)', s=10, color='orange')
plt.scatter(df_solar['pl_orbper'], df_solar['pl_bmassj'], color='red', marker='*', s=120, label='Sistema Solare')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Periodo Orbitale [giorni]')
plt.ylabel('Massa del Pianeta [$M_{Jup}$]')
plt.title('Massa vs Periodo Orbitale per metodo di scoperta')
plt.legend()
plt.savefig('Exoplanets_massa_vs_periodorbit_filtrato.png')
plt.show()



# p.to 7 istogramma: si produca l'istogramma sovrapposto della massa del pianeta distinguendo gli esopianeti per metodo di scoperta 
# (Transit/Radial Velocity) con la corrispondente legenda;

# Estrazione dei dati del Sistema Solare come array per il grafico a griglia
ss_orbper = df_solar['pl_orbper']
ss_bmassj = df_solar['pl_bmassj']

fig = plt.figure(figsize=(12,11))

# creo griglia 2x2 per subplot con asse X in comune per le colonne e asse Y in comune per le righe 
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
# fig.add_gridspec definisce una griglia subplots di 2 righe e 2 colonne. I parametri hspace=0 e wspace=0 azzerano lo spazio (i margini vuoti) 
# tra un grafico e l'altro, facendo in modo che i pannelli siano perfettamente attaccati.
ax = gs.subplots( sharex='col', sharey='row')
# gs.subplots genera una matrice di assi (ax) dove le colonne condividono lo stesso asse X (sharex='col') e le righe condividono 
# lo stesso asse Y (sharey='row'). Serve per allineare perfettamente gli istogrammi ai lati dello scatter plot.

# Scatter Plot Centrale (in basso a sinistra: ax[1,0])
ax[1,0].scatter(np.log10(transit_df['pl_orbper']),
                np.log10(transit_df['pl_bmassj']), color='limegreen', alpha=0.3, label='Transit')
ax[1,0].scatter(np.log10(rv_df['pl_orbper']),
                np.log10(rv_df['pl_bmassj']), color='darkorange', alpha=0.3, label='Radial Velocity')
ax[1,0].scatter(np.log10(ss_orbper), np.log10(ss_bmassj), color='slategray', marker='*', s=100, label='Solar System')

ax[1,0].tick_params(axis='both', which='major', labelsize=14)
ax[1,0].set_xlabel('log(Period [days])', fontsize=16)
ax[1,0].set_ylabel(r'log(Planet Mass [$m_J$])', fontsize=16)
ax[1,0].legend(fontsize=14)


# Istogramma Periodo (in alto a sinistra: ax[0,0])
ax[0,0].hist(np.log10(transit_df['pl_orbper']),
             bins=50, range=(-2, 5), color='limegreen', alpha=0.5, label='Transit')
ax[0,0].hist(np.log10(rv_df['pl_orbper']),
             bins=50, range=(-2, 5), color='darkorange', alpha=0.5, label='Radial Velocity')

ax[0,0].tick_params(axis='both', which='major', labelsize=14)
ax[0,0].set_ylabel(r'Number of planets', fontsize=16)
ax[0,0].legend(fontsize=14)


# p.to 8 istogramma: si produca un grafico analogo al precedente per il logaritmo in base 10 della massa del pianeta.
# Istogramma Massa pianeta (in basso a destra: ax[1,1])
ax[1,1].hist(np.log10(transit_df['pl_bmassj']),
             bins=50, range=(-4, 4), color='limegreen', alpha=0.5, orientation='horizontal', label='Transit')
ax[1,1].hist(np.log10(rv_df['pl_bmassj']),
             bins=50, range=(-4, 4), color='darkorange', alpha=0.5, orientation='horizontal', label='Radial Velocity')

ax[1,1].tick_params(axis='both', which='major', labelsize=14)
ax[1,1].set_xlabel('Number of planets', fontsize=16)
ax[1,1].legend(fontsize=14)

# Rimuovo assi per il riquadro in alto a destra (non necessario)
ax[0,1].axis('off')

# Salvataggio e visualizzazione
plt.savefig('Exoplanets_Period_vs_Mass_Detection.png', bbox_inches='tight')
plt.show()