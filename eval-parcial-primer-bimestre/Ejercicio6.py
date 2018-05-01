
mes = int(input("Ingrese el número del mes: "))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
	dias = 31
if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
	dias = 30
if (mes == 2):
	dias = 28
print("El mes %d tiene %d días." % (mes,dias))