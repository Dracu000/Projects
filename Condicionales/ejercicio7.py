renta_anual = float(input("Ingrese su renta anual: "))
if renta_anual < 10000:
    print("Su tipo impositivo es del 5% " + str(renta_anual * 0.05))
elif renta_anual < 20000:
    print("Su tipo impositivo es del 15% " + str(renta_anual * 0.15))
elif renta_anual < 35000:
    print("Su tipo impositivo es del 20% " + str(renta_anual * 0.20))
elif renta_anual < 60000:
    print("Su tipo impositivo es del 30% " + str(renta_anual * 0.30))
else:
    print("Su tipo impositivo es del 45% " + str(renta_anual * 0.45))