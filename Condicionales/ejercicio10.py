vegetariana = input("¿Desea una pizza vegetariana? (si/no): ")
if vegetariana.lower() == "si":
    print("Ingredientes disponibles: Pimiento, Tofu")
    ingrediente = input("Seleccione un ingrediente adicional: ")
    if ingrediente.lower() == "pimiento":
        print("Ha seleccionado una pizza vegetariana con pimiento.")
    elif ingrediente.lower() == "tofu":
        print("Ha seleccionado una pizza vegetariana con tofu.")
    else:
        print("Ingrediente no válido.")
else:
    print("Ingredientes disponibles: Jamón, Pepperoni, Salmón")
    ingrediente = input("Seleccione un ingrediente adicional: ")
    if ingrediente.lower() == "jamón":
        print("Ha seleccionado una pizza no vegetariana con jamón.")
    elif ingrediente.lower() == "pepperoni":
        print("Ha seleccionado una pizza no vegetariana con pepperoni.")
    elif ingrediente.lower() == "salmón":
        print("Ha seleccionado una pizza no vegetariana con salmón.")
    else:
        print("Ingrediente no válido.")