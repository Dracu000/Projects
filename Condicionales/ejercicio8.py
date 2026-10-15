puntuacion = float(input("Ingrese la puntuación: "))
if puntuacion == 0.0:
    print("Inaceptable, dinero recibido= " + str(puntuacion * 2400))
elif puntuacion == 0.4:
    print("Aceptable, dinero recibido= " + str(puntuacion * 2400))
elif puntuacion >= 0.6:
    print("Meritorio, dinero recibido= " + str(puntuacion * 2400))