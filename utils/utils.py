from flask import abort
from configs import db

def obtener_entidad_activa(modelo, id_entidad, nombre='Entidad'):
    entidad = db.session.get(modelo, id_entidad)
    if not entidad or getattr(entidad, 'estado', None) != 'Activo':
        abort(404, description=f"{nombre} no encontrado o inactivo")
    return entidad
