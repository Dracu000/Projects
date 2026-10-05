frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")
# 1. Mostrar la frase con la vocal ingresada en mayúscula
frase_modificada = frase.replace(vocal, vocal.upper())
print(frase_modificada)