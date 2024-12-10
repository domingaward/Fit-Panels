# ¿Cuántos paneles de dimensiones a x b caben en un rectángulo de dimensiones x x y?
import sys

def max_panels(a, b, x, y):
    
    # Caso base: no caben paneles
    if a > x or b > y:
        return 0

    # Calcular la cantidad de paneles que caben horizontalmente
    horizontal = (x // a) * (y // b)

    # Calcular la cantidad de paneles que caben en el espacio restante vertical
    vertical_rest = max_panels(a, b, y % b, x)

    # Retornar la cantidad total de paneles
    return horizontal + vertical_rest 


if __name__ == "__main__":
    # Leer variables a, b, x y y 
    input_data = sys.stdin.buffer.read().decode().strip()
    a, b, x, y = map(int, input_data.split())

    # Ordenar las dimensiones de los paneles y del rectángulo
    a, b = sorted([a, b])
    x, y = sorted([x, y])

    # Calcular y mostrar el resultado
    resultado = max_panels(a, b, x, y)
    print(resultado)