
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))
z = float(input("Ingrese el valor de z: "))
m = ((x*z + y) / z) / ((x*z - y) / z)
print("El valor de m, en base a las variables:\n\tx = %.2f\n\t\ty = %.2f\n\t\t\tz = %.2f" % (x,y,z))
print("Da como resultado:\n\t\t\t\tm = %.2f" % (m))