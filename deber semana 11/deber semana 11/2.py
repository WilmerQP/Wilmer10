def ordenar_fila(matriz, fila):
    # Obtener la fila específica
    fila_a_ordenar = matriz[fila]
    # Utilizar el algoritmo de ordenación de tu elección, por ejemplo, Bubble Sort
    for i in range(len(fila_a_ordenar)):
        for j in range(0, len(fila_a_ordenar) - i - 1):
            if fila_a_ordenar[j] > fila_a_ordenar[j + 1]:
                fila_a_ordenar[j], fila_a_ordenar[j + 1] = fila_a_ordenar[j + 1], fila_a_ordenar[j]

# Definir la matriz
matriz = [
    [3, 2, 9],
    [5, 1, 4],
    [7, 8, 6]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila que deseamos ordenar (empezando desde 0)
fila_a_ordenar = 1

# Llamar a la función para ordenar la fila específica
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
