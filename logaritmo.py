import math


def calcular_logaritmo():
    try:
        numero = float(input("Ingresa el número para calcular el logaritmo: "))
        base = float(input("Ingresa la base del logaritmo (deja en blanco para base e): ") or math.e)

        if numero <= 0 or base <= 0 or base == 1:
            print("El número y la base deben ser mayores que 0 y la base no puede ser 1.")
            return

        resultado = math.log(numero, base)
        print(f"El logaritmo de {numero} en base {base} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")


if __name__ == "__main__":
    calcular_logaritmo()