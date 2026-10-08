edad = int(input("Ingrese su edad: "))
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: "))
if edad > 16 and ingresos_mensuales >= 1000: 
    print("Usted debe de tributar.") 
else:
    print ("Usted no debe de tributar.")
