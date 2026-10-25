"""
Creare uno script python che:

chieda in input 2 valori interi;
stampi i valori in rappresentazione binaria ed esadecimale;
satmpi il risultato delle operazioni AND e OR bitwise sia in 
rappresentazione binaria che esadecimale.
"""

A = input("Inserire il primo valore intero: ")
B = input("Inserire il secondo valore intero: ")
a = int(A)
b = int(B)

print ("Ecco i numeri in rappresentazione binaria: ")
print ("a = ",bin(a))
print ("b = ", bin(b))

print ("Ecco i numeri in rappresentazione esadecimale: ")
print ("a = ", hex(a))
print ("b = ", hex (b))

print("bitwise OR / AND")
print("----------------------")
print("rappresentazione binaria a :", bin(a))
print("rappresentazione binaria b :", bin(b))
print("----------------------")
print("(a|b) :", bin(a | b))
print("(a&b) :", bin(a & b))
print("----------------------")
print("rappresentazione esadecimale a :", hex(a))
print("rappresentazione esadecimale b :", hex(b))
print("----------------------")
print("(a|b) :", hex(a | b))
print("(a&b) :", hex(a & b))
