# gestionPerfiles.py
from conexion_bd import obtener_conexion
from modelos.perfiles import Perfil

class GestionPerfiles:

    @staticmethod
    def crear_perfil(perfil: Perfil):
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = """
        INSERT INTO Perfiles (usuario_id, nombre_completo, contacto, experiencia, educacion, habilidades, expectativa_salarial)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            perfil.usuario_id,
            perfil.nombre_completo,
            perfil.contacto,
            perfil.experiencia,
            perfil.educacion,
            perfil.habilidades,
            perfil.expectativa_salarial
        ))
        conn.commit()
        perfil.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return perfil

    @staticmethod
    def obtener_perfil_por_id(id: int):
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Perfiles WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Perfil(**row).to_dict()
        return None

    @staticmethod
    def obtener_perfil_por_usuario_id(usuario_id: int):
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Perfiles WHERE usuario_id = %s", (usuario_id,))
        row = cursor.fetchone() # Asumiendo un usuario tiene un solo perfil
        cursor.close()
        conn.close()
        if row:
            return Perfil(**row).to_dict()
        return None

    @staticmethod
    def actualizar_perfil(perfil: Perfil):
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = """
        UPDATE Perfiles SET
            nombre_completo = %s, contacto = %s, experiencia = %s,
            educacion = %s, habilidades = %s, expectativa_salarial = %s
        WHERE id = %s
        """
        cursor.execute(query, (
            perfil.nombre_completo,
            perfil.contacto,
            perfil.experiencia,
            perfil.educacion,
            perfil.habilidades,
            perfil.expectativa_salarial,
            perfil.id
        ))
        conn.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        conn.close()
        return rows_affected > 0

    @staticmethod
    def eliminar_perfil(id: int):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Perfiles WHERE id = %s", (id,))
        conn.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        conn.close()
        return rows_affected > 0