barras_vendidas_antiguas = int(input("Introduce el número de barras de ayer: "))
barras_vendidas_hoy = int(input("Introduce el número de barras de hoy: "))
barras_hoy = 3.49
barras_ayer = 3.49 * 0.6
print("El dinero recaudado ayer fue:", f"{barras_vendidas_antiguas * barras_ayer:.2f}")
print("El dinero recaudado hoy fue:", f"{barras_vendidas_hoy * barras_hoy:.2f}")