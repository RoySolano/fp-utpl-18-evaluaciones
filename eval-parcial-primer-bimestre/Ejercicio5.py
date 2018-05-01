
calificacion1 = float(input("Ingrese el valor de la calificación 1: "))
calificacion2 = float(input("Ingrese el valor de la calificación 2: "))
calificacion3 = float(input("Ingrese el valor de la calificación 3: "))
calificacion4 = float(input("Ingrese el valor de la calificación 4: "))
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4
if (promedio <= 100 and promedio >= 90):
	puntuacion = "A"
if (promedio <= 89 and promedio >= 80):
	puntuacion = "B"
if (promedio <= 79 and promedio >= 70):
	puntuacion = "C"
if (promedio <= 69 and promedio >= 0):
	puntuacion = "D"
print("El estudiante con el promedio de calificaciones %.2f, tiene una puntuación de %s." % (promedio,puntuacion))