vegetariana = input("¿Desea una pizza vegetariana? (si/no): ")
if vegetariana.lower() == "si":
    print("Ingredientes disponibles: Pimiento, Tofu")
    ingrediente = input("Seleccione un ingrediente adicional: ")
    if ingrediente.lower() == "pimiento":
        print("Ha seleccionado una pizza vegetariana con pimiento, mozzarella y tomate..")
    elif ingrediente.lower() == "tofu":
        print("Ha seleccionado una pizza vegetariana con tofu, mozzarella y tomate..")
    else:
        print("Ingrediente no válido.")
else:
    print("Ingredientes disponibles: Jamón, Pepperoni, Salmón")
    ingrediente = input("Seleccione un ingrediente adicional: ")
    if ingrediente.lower() == "jamón":
        print("Ha seleccionado una pizza no vegetariana con jamón, mozzarella y tomate.")
    elif ingrediente.lower() == "pepperoni":
        print("Ha seleccionado una pizza no vegetariana con pepperoni, mozzarella y tomate..")
    elif ingrediente.lower() == "salmón":
        print("Ha seleccionado una pizza no vegetariana con salmón, mozzarella y tomate.")
    else:
        print("Ingrediente no válido.")