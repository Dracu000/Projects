dinero = float(input("Ingrese la cantidad de dinero: "))
interes_anual = float(input("Ingrese el interés anual (en porcentaje): "))
numero_anios = int(input("Ingrese el número de años: "))
# Mostramos el dinero obtenido cada año
for anio in range(1, numero_anios + 1):
    dinero = dinero + (dinero * (interes_anual / 100))
    print("Año", anio, ": dinero obtenido =", round(dinero, 2))