import numpy as np

"""
    Questa classe serve per la configurazione strumentale di un sistema PET.
    Modella i parametri geometrici e prestazionali dello strumento (come il raggio dell'anello 
    e la risoluzione temporale) per consentire il confronto tra diverse configurazioni ToF.
"""


class configurazione_strumento:
    
    def __init__(self, raggio, risoluzione_temporale):
        
        # inizializzo un nuovo sistema PET. I parametri sono:
        # - raggio (float): il raggio dell'anello dei rivelatori (in cm)
        # - risoluzione_temporale (float): la risoluzione temporale dello strumento (in nanosecondi)
        
        self.raggio = raggio
        self.risoluzione_temporale = risoluzione_temporale


    # Operatore minore di (<) basato sulla risoluzione temporale
    def __lt__(self, altro):
        return self.risoluzione_temporale < altro.risoluzione_temporale
        # confronto due sistemi PET: restituisce True se questo ha una risoluzione temporale minore (migliore)


    # Operatore maggiore di (>) basato sulla risoluzione temporale
    def __gt__(self, altro):
        return self.risoluzione_temporale > altro.risoluzione_temporale
        # confronta due sistemi PET: restituisce True se questo ha una risoluzione temporale maggiore (peggiore).


    # stampo l'oggetto
    def __repr__(self):
        return "PET(raggio={}, res={}ns)".format(self.raggio, self.risoluzione_temporale)