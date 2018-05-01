
ventas = float(input("Ingrese el valor de sus ventas: "))
if (ventas <= 500):
	sueldo = 360.40 + (ventas*0.05)
if (ventas > 500 and ventas <= 1000):
	sueldo = 360.40 + (ventas*0.08)
if (ventas > 1000 and ventas <= 5000):
	sueldo = 360.40 + (ventas*0.10)
if (ventas > 1000 and ventas <= 5000):
	sueldo = 360.40 + (ventas*0.15)
print("Su sueldo es: %.2f\n" % (sueldo))