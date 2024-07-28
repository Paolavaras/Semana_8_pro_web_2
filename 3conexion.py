import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="semana8"  
        )  
        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Ejemplo de uso
conn = create_connection()
if conn:
    conn.close()
    print("Conexión cerrada.")
    
