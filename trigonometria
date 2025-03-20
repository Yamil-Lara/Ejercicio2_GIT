import math
import numpy as np
import matplotlib.pyplot as plt

def calcular_trigonometria(angulo):
    """Calcula el seno, coseno y tangente de un ángulo dado en grados."""
    radianes = math.radians(angulo)
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    tangente = math.tan(radianes) if coseno != 0 else None  # Evita división por cero
    
    print(f"Ángulo: {angulo}°")
    print(f"Seno: {seno:.4f}")
    print(f"Coseno: {coseno:.4f}")
    print(f"Tangente: {'Indefinido' if tangente is None else f'{tangente:.4f}'}")
    return seno, coseno, tangente

def graficar_trigonometria():
    """Grafica las funciones seno, coseno y tangente en un rango de -360° a 360°."""
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
    seno_y = np.sin(x)
    coseno_y = np.cos(x)
    tangente_y = np.tan(x)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, seno_y, label='Seno', color='b')
    plt.plot(x, coseno_y, label='Coseno', color='r')
    plt.plot(x, tangente_y, label='Tangente', color='g', linestyle='dotted')
    
    plt.ylim(-2, 2)  # Limitar la escala para que la tangente no explote
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Funciones Trigonométricas: Seno, Coseno y Tangente")
    plt.xlabel("Ángulos en radianes")
    plt.ylabel("Valor de la función")
    plt.show()

# Pedir un ángulo al usuario
angulo_usuario = float(input("Ingresa un ángulo en grados: "))
calcular_trigonometria(angulo_usuario)

graficar_trigonometria()
