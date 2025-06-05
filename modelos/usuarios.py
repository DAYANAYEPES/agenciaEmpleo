# modelos/usuarios.py
from modelos.base import ModeloBase

class Usuario(ModeloBase):
    id: int | None = None 
    nombre: str
    correo: str
    rol_id: int