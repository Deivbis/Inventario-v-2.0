from flask import abort
from configs import db

def obtener_entidad_activa(modelo, id_entidad, nombre='Entidad'):
    entidad = db.session.get(modelo, id_entidad)
    if not entidad or getattr(entidad, 'estado', None) != 'Activo':
        abort(404, description=f"{nombre} no encontrado o inactivo")
    return entidad


def obtener_entidades_activas(modelo):
    try:
        entidades = modelo.query.filter_by(estado='Activo').all()
        return entidades

    except Exception as e:
        print(e)
        return None