from conexion_bd import obtener_conexion
from modelos.usuarios import Usuario

class GestionUsuarios:

    @staticmethod
    def crear_usuario(usuario: Usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = "INSERT INTO Usuarios (nombre, correo, rol_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (usuario.nombre, usuario.correo, usuario.rol_id))
        conn.commit()
        usuario.id = cursor.lastrowid # Asignar el ID generado por la BD al objeto Pydantic
        cursor.close()
        conn.close()
        return usuario # Devolvemos la instancia Pydantic completa

    @staticmethod
    def obtener_usuario_por_id(id: int):
        conn = obtener_conexion()
        # Usamos dictionary=True para obtener resultados como diccionarios
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            # Creamos y devolvemos la instancia Pydantic directamente
            return Usuario(**row)
        return None

    @staticmethod
    def obtener_todos_los_usuarios():
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuarios")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        # Creamos una lista de instancias Pydantic y la devolvemos
        usuarios_pydantic = [Usuario(**row) for row in resultados]
        return usuarios_pydantic

    @staticmethod
    def actualizar_usuario(usuario: Usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = "UPDATE Usuarios SET nombre = %s, correo = %s, rol_id = %s WHERE id = %s"
        cursor.execute(query, (usuario.nombre, usuario.correo, usuario.rol_id, usuario.id))
        conn.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        conn.close()
        return rows_affected > 0

    @staticmethod
    def eliminar_usuario(id: int):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE id = %s", (id,))
        conn.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        conn.close()
        return rows_affected > 0