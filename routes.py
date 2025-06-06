# routes.py
# routes.py
from fastapi import APIRouter, HTTPException, status
from modelos.usuarios import Usuario
from modelos.perfiles import Perfil
from modelos.ofertas import Oferta
from modelos.ofertas_aplicadas import OfertaAplicada # Si lo usas
from gestionUsuarios import GestionUsuarios
from gestionPerfiles import GestionPerfiles
import traceback
# Importa otras clases de gestión que crees (Empresas, Ofertas, etc.)
# from datetime import datetime # No es necesario si no se usa directamente en rutas

router = APIRouter()

# --- Rutas de Usuarios ---
@router.post("/usuarios/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: Usuario):
    try:
        nuevo_usuario = GestionUsuarios.crear_usuario(usuario)
        return nuevo_usuario
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {e}")

@router.get("/usuarios/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int):
    usuario = GestionUsuarios.obtener_usuario_por_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/usuarios/", response_model=list[Usuario])
def obtener_todos_usuarios():
    usuarios = GestionUsuarios.obtener_todos_los_usuarios()
    return usuarios

# --- Rutas de Perfiles (Perfilador de hojas de vida) ---
@router.post("/perfiles/", response_model=Perfil, status_code=status.HTTP_201_CREATED)
def crear_perfil(perfil: Perfil):
    try:
        nuevo_perfil = GestionPerfiles.crear_perfil(perfil)
        return nuevo_perfil
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear perfil: {e}")

@router.get("/perfiles/{perfil_id}", response_model=Perfil)
def obtener_perfil(perfil_id: int):
    try:
        perfiles = GestionPerfiles.obtener_perfil_por_id(perfil_id)
        if not perfiles:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")
        return perfiles
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar perfil: {e}")

@router.get("/perfiles/usuario/{usuario_id}", response_model=Perfil)
def obtener_perfil_por_usuario(usuario_id: int):
    perfil = GestionPerfiles.obtener_perfil_por_usuario_id(usuario_id)
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado para este usuario")
    return perfil
