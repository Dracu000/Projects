numero = int(input("Introduce un número: "))
# Monstramos la cuenta atras de ese numero hasta 0 separado por comas
if numero < 0:
    print("El número debe ser mayor o igual a 0")
else:
    for i in range(numero, -1, -1):
        if i != 0:
            print(i, end=", ")
        else:
            print(i)