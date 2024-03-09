def temperatura_promedio_ciudad(datos, ciudad):
    if ciudad not in datos:
        print(f"No hay datos disponibles para la ciudad {ciudad}")
        return None

    temperaturas_semanales = datos[ciudad]
    total_temperaturas = 0
    total_dias = 0

    for semana, temperaturas in temperaturas_semanales.items():
        total_temperaturas += sum(temperaturas)
        total_dias += len(temperaturas)

    temperatura_promedio = total_temperaturas / total_dias
    return temperatura_promedio


# Ejemplo de datos: temperaturas de 3 ciudades durante 4 semanas
datos = {
    'Ciudad A': {
        'Semana 1': [25, 26, 27, 28, 29],
        'Semana 2': [24, 25, 26, 27, 28],
        'Semana 3': [23, 24, 25, 26, 27],
        'Semana 4': [22, 23, 24, 25, 26]
    },
    'Ciudad B': {
        'Semana 1': [20, 21, 22, 23, 24],
        'Semana 2': [19, 20, 21, 22, 23],
        'Semana 3': [18, 19, 20, 21, 22],
        'Semana 4': [17, 18, 19, 20, 21]
    },
    'Ciudad C': {
        'Semana 1': [30, 31, 32, 33, 34],
        'Semana 2': [29, 30, 31, 32, 33],
        'Semana 3': [28, 29, 30, 31, 32],
        'Semana 4': [27, 28, 29, 30, 31]
    }
}

# Calculamos la temperatura promedio para la Ciudad A durante todo el período
ciudad_a_promedio = temperatura_promedio_ciudad(datos, 'Ciudad A')
print("Temperatura promedio de Ciudad A:", ciudad_a_promedio)

# Calculamos la temperatura promedio para la Ciudad B durante todo el período
ciudad_b_promedio = temperatura_promedio_ciudad(datos, 'Ciudad B')
print("Temperatura promedio de Ciudad B:", ciudad_b_promedio)

# Calculamos la temperatura promedio para la Ciudad C durante todo el período
ciudad_c_promedio = temperatura_promedio_ciudad(datos, 'Ciudad C')
print("Temperatura promedio de Ciudad C:", ciudad_c_promedio)
