from modelo import Permiso, RolPermiso


def tiene_permiso(id_rol, nombre_permiso):

    permiso = (
        RolPermiso.query
        .join(Permiso)
        .filter(
            RolPermiso.id_rol == id_rol,
            Permiso.nombre == nombre_permiso,
            RolPermiso.estado == "Activo"
        )
        .first()
    )

    return permiso is not None