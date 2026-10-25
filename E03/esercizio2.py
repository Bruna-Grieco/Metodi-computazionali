"""
Creare uno script python che:

- chieda in input un valore intero e il numero di bit cui applicare delle operazioni di bit shift;
- stampi il valore intero in rappresentazione binaria ed esadecimale;
- satmpi il risultato delle operazioni di bit shift (<< e >>) sia in rappresentazione binaria che 
esadecimale.
"""

N = input("inserire un numero intero: ")
n = int(N)
B = input("a quanti bit vuoi applicare il bit shift? ")
bb1 = int(B)
bs_plus = (n << bb1)
bs_minus = (n >> bb1)

print("\n--------------------------------------")
print("          valore inserito            ")
print("--------------------------------------")
print("decimale     :", n)
print("binario      :", bin(n))
print("esadecimale  :", hex(n))

print("\n--------------------------------------")
print("        bit shift di {} bit          ". format(bb1))
print("--------------------------------------")
print("shift a sinistra ( << {} ):". format(bb1))
print("  binario    :", bin(bs_plus))
print("  esadecimale:", hex(bs_plus))

print("shift a destra ( >> {} ):".format(bb1))
print("  binario    :", bin(bs_minus))
print("  esadecimale:", hex(bs_minus))
print("--------------------------------------")
