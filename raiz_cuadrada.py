# Autor: Abraham Espinoza Lopez
def raiz_cuadrada(n, precision=0.00001):
    if n < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo"

    estimacion = n / 2.0  # Estimación inicial
    while abs(estimacion * estimacion - n) > precision:
        estimacion = (estimacion + n / estimacion) / 2.0
    return estimacion

numero = float(input("Ingrese un número: "))
print("La raíz cuadrada de {numero} es  {raiz_cuadrada(numero)}")
