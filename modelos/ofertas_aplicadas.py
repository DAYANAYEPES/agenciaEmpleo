# modelos/ofertas_aplicadas.py
from modelos.base import ModeloBase
from datetime import datetime

class OfertaAplicada(ModeloBase):
    def __init__(self, id: int, perfil_id: int, oferta_id: int, fecha_aplicacion: datetime, estado_aplicacion: str = "Enviada"):
        self.id = id
        self.perfil_id = perfil_id
        self.oferta_id = oferta_id
        self.fecha_aplicacion = fecha_aplicacion
        self.estado_aplicacion = str(estado_aplicacion).strip()

    def to_dict(self):
        return {
            "id": self.id,
            "perfil_id": self.perfil_id,
            "oferta_id": self.oferta_id,
            "fecha_aplicacion": self.fecha_aplicacion.isoformat(), # Formato ISO para JSON
            "estado_aplicacion": self.estado_aplicacion
        }