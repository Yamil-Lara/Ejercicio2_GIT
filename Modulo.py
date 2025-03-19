#Autor: Juan Diego Delgadillo Fernandez
def calcular_modulo(a, b):
    """
    Función que calcula el módulo de dos números dados.
    """
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a % b

# Solicitar valores al usuario
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

# Calcular y mostrar el resultado
resultado = calcular_modulo(a, b)
print(f"El módulo de {a} % {b} es: {resultado}")