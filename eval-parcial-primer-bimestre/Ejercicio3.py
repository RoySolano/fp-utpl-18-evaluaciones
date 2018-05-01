
segundos = int(input("Ingrese el número de segundos: "))
minutos  = segundos // 60
resto = segundos - 60*minutos
print("%d segundos es  igual a %d minuto(s) y %d segundos" % (segundos,minutos,resto))