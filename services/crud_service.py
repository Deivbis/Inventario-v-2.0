from configs import db


def guardar_entidad(entidad):

    try:
        db.session.add(entidad)
        db.session.commit()

        return True

    except Exception as e:
        db.session.rollback()
        print(e)
        return False


def editar_entidad(entidad):
    
    try: 
        db.session.commit()
        return True
    
    except Exception as e:
        db.session.rollback()
        print(e)
        return False



def desactivar_entidad (entidad):

    try:
        entidad.estado = 'Inactivo'
        db.session.commit()
        return True
    
    except Exception as e:
        db.session.rollback()
        print(e)
        return False
    
