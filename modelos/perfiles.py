# modelos/perfiles.py
from modelos.base import ModeloBase

class Perfil(ModeloBase):
    def __init__(self, id: int, usuario_id: int, nombre_completo: str, contacto: str, experiencia: str = "", educacion: str = "", habilidades: str = "", expectativa_salarial: float = 0.0):
        self.id = id
        self.usuario_id = usuario_id
        self.nombre_completo = str(nombre_completo).strip()
        self.contacto = str(contacto).strip()
        self.experiencia = str(experiencia).strip()
        self.educacion = str(educacion).strip()
        self.habilidades = str(habilidades).strip()
        self.expectativa_salarial = expectativa_salarial

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "nombre_completo": self.nombre_completo,
            "contacto": self.contacto,
            "experiencia": self.experiencia,
            "educacion": self.educacion,
            "habilidades": self.habilidades,
            "expectativa_salarial": self.expectativa_salarial
        }