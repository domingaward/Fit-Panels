# Fit-Panels
Determinar la cantidad máxima de paneles que caben en un rectángulo.

Este programa calcula la cantidad máxima de paneles de dimensiones \(a \times b\) que se pueden acomodar completamente dentro de un rectángulo de dimensiones \(x \times y\). El algoritmo toma en cuenta tanto la orientación vertical como horizontal de los paneles y optimiza su posicionamiento para maximizar el número de paneles.

## Funcionamiento

El programa utiliza un enfoque recursivo para calcular cuántos paneles caben dentro del rectángulo. Primero, posiciona los paneles horizontalmente, calculando el número que cabe en las dimensiones principales del rectángulo. Luego, evalúa el espacio restante y repite el proceso para calcular los paneles que caben en el área residual de manera vertical.

### Pasos principales del algoritmo:
1. **Caso base:** Si las dimensiones del panel son mayores que las dimensiones del rectángulo, no se puede colocar ningún panel, y el programa retorna 0.
2. **Posicionamiento horizontal:** Calcula cuántos paneles completos caben al alinear el panel en la orientación horizontal dentro del rectángulo.
3. **Espacio restante:** Recurre sobre el espacio restante vertical para calcular cuántos paneles adicionales caben en esa área.
4. **Orden de dimensiones:** El programa asegura que tanto los paneles como el rectángulo estén orientados correctamente (lado menor primero) antes de realizar los cálculos.

## Entrada

El programa recibe las dimensiones del panel (\(a\), \(b\)) y del rectángulo (\(x\), \(y\)) a través de un archivo de entrada (`input.txt`). 
- El archivo debe contener una sola línea con cuatro enteros separados por espacios: \(a, b, x, y\).
- Las dimensiones pueden estar desordenadas; el algoritmo las ordenará internamente para garantizar el cálculo correcto.

## Ejecución

Para ejecutar el programa, se utiliza el siguiente comando en la terminal:
```
python3 panels.py < input.txt > output.txt
```

### Archivo de entrada (`input.txt`)
El archivo de entrada debe contener una línea con las dimensiones del panel y del rectángulo. Ejemplo:
```
3 2 10 8
```

### Archivo de salida (`output.txt`)
El archivo de salida contendrá un único entero que representa la cantidad máxima de paneles que caben dentro del rectángulo. Ejemplo de salida para el caso anterior:
```
12
```

## Ejemplo completo

### Entrada
Archivo `input.txt`:
```
3 2 10 8
```

### Ejecución
```
python3 panels.py < input.txt > output.txt
```

### Salida
Archivo `output.txt`:
```
12
```

## Requisitos

- Python 3.x
- Archivo de entrada (`input.txt`) con las dimensiones \(a, b, x, y\).

## Notas

- Este programa considera únicamente la colocación completa de los paneles, es decir, no se permite recortar paneles para encajarlos en el espacio restante.
- El algoritmo garantiza que las dimensiones estén correctamente ordenadas para evitar errores de cálculo.
