# modelos/ofertas.py
from modelos.base import ModeloBase
from datetime import datetime

class Oferta(ModeloBase):
    def __init__(self, id: int, empresa_id: int, titulo: str, descripcion: str, requisitos: str, salario: float, fecha_publicacion: datetime, estado: str = "Abierta"):
        self.id = id
        self.empresa_id = empresa_id
        self.titulo = str(titulo).strip()
        self.descripcion = str(descripcion).strip()
        self.requisitos = str(requisitos).strip()
        self.salario = salario
        self.fecha_publicacion = fecha_publicacion
        self.estado = str(estado).strip()

    def to_dict(self):
        return {
            "id": self.id,
            "empresa_id": self.empresa_id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "requisitos": self.requisitos,
            "salario": self.salario,
            "fecha_publicacion": self.fecha_publicacion.isoformat(), # Formato ISO para JSON
            "estado": self.estado
        }