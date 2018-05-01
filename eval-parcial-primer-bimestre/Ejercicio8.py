
letra1 = input("Ingrese la letra 1:")
letra2 = input("Ingrese la letra 2:")
letra3 = input("Ingrese la letra 2:")
if letra1 < letra2:
	primera = letra1
else:
	primera = letra2
if letra1 < letra3:
    primera = letra1 
else:
    primera = letra3  
print("La primera letra en aparecer en el abecedario es: %s." % (primera))