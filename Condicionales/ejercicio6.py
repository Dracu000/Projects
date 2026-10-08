sexo = input("Ingrese su sexo (M/F): ")
nombre = input("Ingrese su nombre: ")
if (sexo == "M" and nombre[0].upper() < "M") or (sexo == "F" and nombre[0].upper() > "M"):
    print("Usted pertenece al grupo A")
    else:
    print("Usted pertenece al grupo B")