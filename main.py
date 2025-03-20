import CalcularPotencias
import Division
import factorial
import logaritmo
import Modulo
import multiplicacion
import raiz_cuadrada
import resta
import suma
import trigonometria

def menu():
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Calcular Potencias")
        print("2. División")
        print("3. Factorial")
        print("4. Logaritmo")
        print("5. Módulo")
        print("6. Multiplicación")
        print("7. Raíz Cuadrada")
        print("8. Resta")
        print("9. Suma")
        print("10. Trigonometría")
        print("11. Salir")
        
        opcion = input("Seleccione una operación: ")

        if opcion == "11":
            print("Saliendo...")
            break

        elif opcion == "1":  # Potencias
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            print(f"Resultado: {CalcularPotencias.calcular_potencias(base, exponente)}")

        elif opcion == "2":  # División
            a = float(input("Ingrese el dividendo: "))
            b = float(input("Ingrese el divisor: "))
            print(f"Resultado: {Division.division(a, b)}")

        elif opcion == "3":  # Factorial
            n = int(input("Ingrese un número entero: "))
            print(f"Resultado: {factorial.factorial(n)}")

        elif opcion == "4":  # Logaritmo
            n = float(input("Ingrese el número: "))
            base = float(input("Ingrese la base del logaritmo (default 10): ") or 10)
            print(f"Resultado: {logaritmo.logaritmo(n, base)}")

        elif opcion == "5":  # Módulo
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {Modulo.modulo(a, b)}")

        elif opcion == "6":  # Multiplicación
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {multiplicacion.multiplicacion(a, b)}")

        elif opcion == "7":  # Raíz Cuadrada
            n = float(input("Ingrese un número: "))
            print(f"Resultado: {raiz_cuadrada.raiz_cuadrada(n)}")

        elif opcion == "8":  # Resta
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {resta.resta(a, b)}")

        elif opcion == "9":  # Suma
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {suma.suma(a, b)}")

        elif opcion == "10":  # Trigonometría
            print("\nSeleccione la función trigonométrica:")
            print("1. Seno")
            print("2. Coseno")
            print("3. Tangente")
            trig_opcion = input("Seleccione una opción: ")

            angulo = float(input("Ingrese el ángulo en grados: "))

            if trig_opcion == "1":
                print(f"Resultado: {trigonometria.seno(angulo)}")
            elif trig_opcion == "2":
                print(f"Resultado: {trigonometria.coseno(angulo)}")
            elif trig_opcion == "3":
                print(f"Resultado: {trigonometria.tangente(angulo)}")
            else:
                print("Opción no válida.")

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()