from datetime import datetime
from configs.extensiones import db

class RolPermiso(db.Model):
    __tablename__ = 'rol_permiso'

    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    id_permiso = db.Column(db.Integer, db.ForeignKey('permisos.id'), nullable=False)
    estado =  db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    rol = db.relationship('Rol', back_populates='permisos')
    permiso = db.relationship('Permiso', back_populates='roles')