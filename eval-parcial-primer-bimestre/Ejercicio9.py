
lado1 = float(input("Ingrese el lado 1 del  primer triángulo: "))
lado2 = float(input("Ingrese el lado 2 del  primer triángulo: "))
lado3 = float(input("Ingrese el lado 3 del  primer triángulo: "))
angulo1 = float(input("Ingrese el angulo 1 del  primer triángulo: "))
angulo2 = float(input("Ingrese el angulo 2 del  primer triángulo: "))
angulo3 = float(input("Ingrese el angulo 3 del  primer triángulo: "))

lado4 = float(input("Ingrese el lado 1 del  segundo triángulo: "))
lado5 = float(input("Ingrese el lado 2 del  segundo triángulo: "))
lado6 = float(input("Ingrese el lado 3 del  segundo triángulo: "))
angulo4 = float(input("Ingrese el angulo 1 del  segundo triángulo: "))
angulo5 = float(input("Ingrese el angulo 2 del  segundo triángulo: "))
angulo6 = float(input("Ingrese el angulo 3 del  segundo triángulo: "))

if (angulo1 + angulo2 + angulo3 == 180 and angulo4 + angulo5 + angulo6 == 180):
    if (lado1 == lado4 or lado1 == lado5 or lado1 == lado6) and (angulo1 == angulo4 or angulo1 == angulo5 or angulo1 == angulo6):
    	if(lado2 == lado4 or lado2 == lado5 or lado2 == lado6) and (angulo2 == angulo4 or angulo2 == angulo5 or angulo2 == angulo6):
    		if (lado3 == lado4 or lado3 == lado5 or lado3 == lado6) and (angulo3 == angulo4 or angulo3 == angulo5 or angulo3 == angulo6):
    			congruencia1 = 1
    		else:
    			congruencia1 = 0
    	else:
    		congruencia1 = 0
    else:
    	congruencia1 = 0
    if (congruencia1 == 1):
    	print("Los triangulos son congruentes.")
    else:
    	print("Los triangulos no son congruentes.")
else:
	print("Los valores de los angulos no corresponden a un triángulo.")