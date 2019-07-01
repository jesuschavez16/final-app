


from sqlalchemy.sql import func

from project import db


# modelo
class Alquiler(db.Model):
    __tablename__ = 'Alquiler'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_alqui = db.Column(db.Date(), nullable=False)
    fecha_devol = db.Column(db.Date(), nullable=False)
    id_cliente = db.Column(db.Integer, nullable=False)
    id_empleado = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)


    def to_json(self):
        return {
            'id': self.id,
            'fecha_alqui': self.fecha_alqui,
            'fecha_devol': self.fecha_devol,
            'id_cliente': self.id_cliente,
            'id_empleado': self.id_empleado,
            'active': self.active
        }


    def __init__(self, fecha_alqui, fecha_devol, id_cliente, id_empleado):
        self.fecha_alqui = fecha_alqui
        self.fecha_devol = fecha_devol
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado


class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128), nullable=False)
    apellido = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)  

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'active': self.active
        }

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Empleado(db.Model):
    __tablename__ = 'Empleado'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128), nullable=False)
    apellido = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'active': self.active
        }

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Pelicula(db.Model):
    __tablename__ = 'Pelicula'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128), nullable=False)
    genero = db.Column(db.Integer, nullable=False)
    fecha_lanzamiento = db.Column(db.Date(), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'genero': self.genero,
            'fecha_lanzamiento': self.fecha_lanzamiento,
            'active': self.active
        }

    def __init__(self, nombre, genero, fecha_lanzamiento):
        self.nombre = nombre
        self.genero = genero
        self.fecha_lanzamiento = fecha_lanzamiento


class Alq_Pel(db.Model):
    __tablename__ = 'Alq_Pel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_alquiler = db.Column(db.Integer, nullable=False)
    id_pelicula = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'id_alquiler': self.id_alquiler,
            'id_pelicula': self.id_pelicula,
            'active': self.active
        }
    

    def __init__(self, id_alquiler, id_pelicula):
        self.id_alquiler = id_alquiler
        self.id_pelicula = id_pelicula



