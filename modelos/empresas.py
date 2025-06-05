# modelos/empresas.py
from modelos.base import ModeloBase

class Empresa(ModeloBase):
    def __init__(self, id: int, nombre: str, descripcion: str, contacto: str):
        self.id = id
        self.nombre = str(nombre).strip()
        self.descripcion = str(descripcion).strip()
        self.contacto = str(contacto).strip()

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "contacto": self.contacto
        }