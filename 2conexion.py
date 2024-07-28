import mysql.connector

# Configuración de la conexión
config = {
    'user': 'tu_usuario',           # Reemplaza con tu nombre de usuario MySQL
    'password': '',    # Reemplaza con tu contraseña MySQL
    'host': '127.0.0.1',
    'database': 'semana8',          # Asegúrate de que el nombre de la base de datos es correcto
    'raise_on_warnings': True
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Consulta SQL
    query = "SELECT * FROM faunaflora"
    cursor.execute(query)

    # Mostrar los resultados
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
