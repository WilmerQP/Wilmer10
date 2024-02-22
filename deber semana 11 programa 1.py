def buscar_en_matriz(matriz, valor):
    # Iterar sobre cada fila de la matriz
    for i in range(len(matriz)):
        # Iterar sobre cada elemento de la fila
        for j in range(len(matriz[i])):
            # Verificar si el elemento actual es igual al valor buscado
            if matriz[i][j] == valor:
                # Si se encuentra el valor, imprimir la posición y retornar True
                print(f"El valor {valor} se encuentra en la posición ({i}, {j}) de la matriz.")
                return True
    # Si el valor no se encuentra en la matriz, imprimir un mensaje y retornar False
    print(f"El valor {valor} no se encontró en la matriz.")
    return False

# Definir la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_busqueda = 5

# Llamar a la función de búsqueda e imprimir el resultado
encontrado = buscar_en_matriz(matriz, valor_busqueda)
if not encontrado:
    print("El valor no se encontró en la matriz.")