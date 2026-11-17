n = int(input("Introduce un número entero: "))

if n <= 1:
    print(f"El {n} no es un número primo.")
else:
    i = 2
    while n % i != 0:
        i += 1
        print(f"El {n} es un número primo.")
    else:
        print(f"El {n} no es un número primo.")