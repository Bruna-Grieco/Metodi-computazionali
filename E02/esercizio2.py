#Somma dei primi N numeri naturali
print ('Somma dei primi N numeri naturali')

nn = input('Immettere il numero N: ')
nni = int(nn)
somma = 0

for i in range(1, nni+1):
	somma = somma + i
	
print ('La somma dei primi N numeri reali è ', somma)
