import pandas as pd 
import matplotlib.pyplot as plt 

# p.to 1 Lettura del file CSV e creazione del DataFrame pandas
url = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv"

df = pd.read_csv(url)

"""
Il DataFrame è una struttura dati offerta dalla 
libreria pandas.

La funzione pd.read_csv() legge un file 
CSV sia da un percorso locale sul computer sia 
direttamente da un URL web, scaricandolo e convertendolo 
automaticamente in un DataFrame.
"""

print("p.to 2 - Stampa del nome delle colonne del DataFrame: ")
print(df.columns)


#con il mando df[] estraggo dal dataframe le info
time = df["TIME"]
flux = df["PDCSAP_FLUX"]
flux_err = df["PDCSAP_FLUX_ERR"]


# p.tp 3 Grafico del flusso in funzione del tempo: ottengo una linea continua
plt.figure(figsize=(10, 5))
plt.plot(time, flux, color="blue", linewidth=0.5, label="Flusso")
plt.xlabel("Tempo (BJD)")
plt.ylabel("Flusso (e-/s)")
plt.title("Flusso Kepler in funzione del Tempo")
plt.savefig("Kepler_Flusso_tempo_linea.png")
plt.show()


# p.to 4 Grafico del flusso in funzione del tempo con soli punti 
plt.figure(figsize=(10, 5))
plt.plot(time, flux, "o", markersize=2, label="Punti di flusso")
plt.xlabel("Tempo (BJD)")
plt.ylabel("Flusso (e-/s)")
plt.title("Flusso Kepler in funzione del Tempo (Solo punti)")
plt.savefig("Kepler_Flusso_tempo_punti.png")
plt.show()


# p.to 5 produca un grafico del flusso in funzione del tempo con barre di errore 
# e salvi il risultato in un file png e/o pdf;
plt.figure(figsize=(10, 5))
plt.errorbar(
    time,
    flux,
    yerr=flux_err,
    fmt="o",
    color="blue",
    ecolor="red",
    markersize=2,
    label="Flusso con errore",
)
plt.xlabel("Tempo (BJD)")
plt.ylabel("Flusso (e-/s)")
plt.title("Flusso Kepler con Barre di Errore")
plt.legend()


# salvataggio della figura in formato PNG 
plt.savefig("kepler_flusso_errorbar.png")
# NOTA: In Matplotlib, quando chiamo plt.show(), la figura viene mostrata a schermo e subito dopo 
# viene svuotata/chiusa. Conseguenza: se scrivo plt.show() e subito dopo plt.savefig(...), il file 
# immagine salvato risulterà completamente vuoto (la figura non esiste in memoria)
plt.show()


# p.to 6 selezione di un intervallo temporale attorno a un minimo (Transito)

# Il pianeta HAT-P-7 b transita periodicamente oscurando parte della luce della stella.
# scelgo un intervallo temporale indicativo in cui avviene un transito (scelgo il BJD)
t_min_transito = 947.9
t_max_transito = 948.3

# .loc filtra il DataFrame in base alla condizione temporale
df_transito = df.loc[(df["TIME"] >= t_min_transito) & (df["TIME"] <= t_max_transito)]

plt.figure(figsize=(8, 4))
plt.errorbar(
    df_transito["TIME"],
    df_transito["PDCSAP_FLUX"],
    yerr=df_transito["PDCSAP_FLUX_ERR"],
    fmt="o",
    color="purple",
    ecolor="blue",
    markersize=3,
    label="Transito",
)
plt.xlabel("Tempo (BJD)")
plt.ylabel("Flusso (e-/s)")
plt.title("Zoom sul Transito di HAT-P-7 b")
plt.legend()
plt.savefig("Kepler_zoom_transito.png")
plt.show()



# 7. grafico con la selezione del transito mostrata come riquadro (inset)

fig, ax = plt.subplots(figsize=(12, 6))
# grafico principale con tutti i dati
ax.errorbar(
    time,
    flux,
    yerr=flux_err,
    fmt="o",
    color="blue",
    ecolor="cornflowerblue",
    markersize=1.5,
    alpha=0.6, #rendo i p.ti leggermente trasparenti (al 60% di opacità) 
    label="Dati completi",
)
ax.set_xlabel("Tempo (BJD)")
ax.set_ylabel("Flusso (e-/s)")
ax.set_title("Curva di Luce Kepler con Riquadro di Zoom sul Transito")


# creazione dell'asse interno (inset_axes)
# ins_ax = ax.inset_axes([x, y, width, height]) 
ins_ax = ax.inset_axes([.65, .62, .32, .32])

# Per non avere sovrapposizione nella figura finale, aumento il limite superiore dell'asse Y del 
# grafico grande. 
ymin, ymax = ax.get_ylim()
ax.set_ylim(ymin, ymax * 1.01)  


# riempimento del riquadro con i dati filtrati del transito
ins_ax.errorbar(
    df_transito["TIME"],
    df_transito["PDCSAP_FLUX"],
    yerr=df_transito["PDCSAP_FLUX_ERR"],
    fmt="o",
    color="royalblue",
    ecolor="pink",
    markersize=2,
)
ins_ax.set_title("Dettaglio Transito", fontsize=10)

plt.tight_layout()
plt.savefig("Kepler_completo.png")
plt.show()