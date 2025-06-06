# modelos/perfiles.py
from modelos.base import ModeloBase

class Perfil(ModeloBase):
        id : int 
        usuario_id: int
        nombre_completo : str
        contacto: str
        experiencia: str
        educacion: str
        habilidades : str
        expectativa_salarial: float