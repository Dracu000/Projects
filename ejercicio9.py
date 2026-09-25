capital = int(input("Introduce el capital inicial: "))
interes = float(input("Introduce el interes anual (en porcentaje): "))
años = int(input("Introduce el numero de años: "))
capital_final = capital * (1 + interes / 100) ** años
print("El capital final despues de", años, "años es:", capital_final)