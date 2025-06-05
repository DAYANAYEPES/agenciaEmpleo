# modelos/roles.py
from modelos.base import ModeloBase

class Rol(ModeloBase):
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = str(nombre).strip()

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }