# conexion_bd.py
import mysql.connector

def obtener_conexion():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
             port=3308,
            user="root",        
            password="",   
            database="agenciaEmpleo"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        # Puedes decidir si relanzar el error o devolver None/manejarlo de otra forma
        raise