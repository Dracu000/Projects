nombre = input("Ingrese nombre del producto ")
precio = input("Ingrese precio del producto ")
unidades = input("Ingrese cantidad de unidades del producto ")
# Ahora mostramos por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 digitos enteros y 2 decimales, el numero de unidades con tres digitos y con el coste total con 8 digitos enteros y 2 decimales. Todo ello separado por comas.
precio_formateado = f"{float(precio):06.2f}"
unidades_formateadas = f"{int(unidades):03d}"
coste_total = float(precio) * int(unidades)
coste_total_formateado = f"{coste_total:08.2f}"
print(f"{nombre},{precio_formateado},{unidades_formateadas},{coste_total_formateado}")  