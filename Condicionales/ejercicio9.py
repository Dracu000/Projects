edad_cliente = int(input("Ingrese la edad del cliente: "))
if edad_cliente < 4:
    print("El cliente no paga entrada")
elif 4 <= edad_cliente < 18:
    print("El cliente paga 5$")
else:
    print("El cliente paga 10$")