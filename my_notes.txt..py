# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribir al menos tres líneas de notas personales en el archivo
    file.write("Notas Personales:\n")
    file.write("1. Hoy tengo una reunión importante a las 10 a.m.\n")
    file.write("2. Necesito comprar leche y pan en el supermercado.\n")
    file.write("3. Recordar enviar el informe al jefe antes de las 5 p.m.\n")

# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Mostrar en la consola cada línea leída
        print(line.strip())  # Utilizamos strip() para eliminar espacios en blanco alrededor de la línea

# Cierre de Archivos
# Asegurarse de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias
# No es necesario cerrar explícitamente el archivo porque estamos utilizando el gestor de contexto 'with'
# que se encarga de cerrar automáticamente el archivo al salir del bloque 'with'
