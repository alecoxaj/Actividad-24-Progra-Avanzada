def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)
def suma_naturales(n):
    if n == 0:
        return 0
    return n + suma_naturales(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def contar_letra(palabra, letra, indice=0):
    if indice == len(palabra):
        return 0
    return (1 if palabra[indice] == letra else 0) + contar_letra(palabra, letra, indice + 1)


def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    return cadena[-1] + invertir_cadena(cadena[:-1])


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

while True:
    print("MENÚ:")
    print("1. Calcular el factorial de un número")
    print("2. Suma de los primeros N números naturales")
    print("3. Calcular número fibonacci")
    print("4. Contar cuántas veces aparece una letra en una palabra")
    print("5. Invertir cadena de texto")
    print("6. Calcular potencia")
    print("7. Salir")

    option = input("Selecciona una opción (1-7): ")

    match option:
        case "1":
            try:
                n = int(input("Ingresa un número: "))
                if n < 0:
                    print("El número debe ser positivo.")
                else:
                    print(f"El factorial de {n} es: {factorial(n)}")
            except ValueError:
                print("Carácter inválido. Debe ser un número entero.")

        case "2":
            try:
                n= int(input("Ingresa un número entero positivo: "))
                if n < 0:
                    print("El número debe ser positivo.")
                else:
                    print(f"La suma de los primeros {n} números naturales es: {suma_naturales(n)}")
            except ValueError:
                print("Carácter inválido. Debe ser un número entero.")
        case "3":
            try:
                n = int(input("Ingresa el valor n (entero positivo): "))
                if n < 0:
                    print("El valor debe ser positivo.")
                else:
                    print(f"El término {n} de fibonacci es: {fibonacci(n)}")
            except ValueError:
                print("Carácter inválido. Debe ser un número entero.")

        case "4":
            palabra = input("Ingrese una palabra: ")
            letra = input("Ingresa la letra a contar: ")
            if len(letra) != 1:
                print("Debes ingresar una sola letra.")
            else:
                print(f"La letra '{letra}' aparece {contar_letra(palabra, letra)} veces en '{palabra}'.")

        case "5":
            cadena = input("Ingresa una cadena de texto: ")
            print(f"La cadena invertida es: {invertir_cadena(cadena)}")

        case "6":
            try:
                base = float(input("Ingresa la base: "))
                exponente = int(input("Ingresa el exponente (entero positivo: "))
                if exponente < 0:
                    print("El exponente debe ser positivo.")
                else:
                    print(f"{base}^{exponente} = {potencia(base, exponente)}")
            except ValueError:
                print("Carácter inválido. La base de ser un número y exponente un entero positivo.")

        case "7":
            print("¡Programa finalizado! Saliendo...")
            break

        case _:
            print("Opción no válida. Intenta nuevamente.")






