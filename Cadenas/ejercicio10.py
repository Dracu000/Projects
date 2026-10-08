lista_compra = input("Ingrese los productos de la lista de compra separados por comas: ")
productos = lista_compra.split(",")
print("Productos de la lista de compra:")
for producto in productos:
    print(producto.strip())