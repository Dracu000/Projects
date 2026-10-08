fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
dia, mes, anio = fecha.split("/")
# zfill rellena con un cero a la izquierda si tiene un solo dígito
dia = dia.strip().zfill(2)
mes = mes.strip().zfill(2)
anio = anio.strip()

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")