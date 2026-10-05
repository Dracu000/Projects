precio_completo = input("Ingrese el precio completo del producto: ")
euros, centimos = precio_completo.split(".")
precio_formateado = f"{euros} euros y {centimos} céntimos"
print(precio_formateado)