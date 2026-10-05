correo_original = input("Ingrese su correo electrónico: ")
# 1. Mostrar el correo electronico con el mismo nombre pero con dominio ceu.es
partes = correo_original.split("@")
nombre_usuario = partes[0]
nuevo_correo = f"{nombre_usuario}@ceu.es"
print(nuevo_correo)