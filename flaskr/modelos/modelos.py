from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum

db = SQLAlchemy()

# Tabla de respaldo o soporte
albumes_canciones = db.Table('album_cancion',\
    db.Column('album_id',db.Integer, db.ForeignKey('album.id'), primary_key=True),\
    db.Column('cancion_id',db.Integer, db.ForeignKey('cancion.id'), primary_key=True))

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    # Relaciones
    albumes = db.relationship('Album', secondary='album_cancion', back_populates='canciones')

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 1
    CD = 3

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    year = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio = db.Column(db.Enum(Medio))
    # Llave foranea
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    # Asociaciones
    canciones = db.relationship('Cancion', secondary='album_cancion', back_populates='albumes')
    # Los nombres deben ser unicos
    __table_args__ = (db.UniqueConstraint('usuario', 'titulo', name='titulo_unico_album'),)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(128))
    password = db.Column(db.String(128))
    # Relaciones y asociaciones en python
    albumes = db.relationship('Album', cascade='all, delete, delete-orphan')

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr: str, obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor': value.value}

class AlbumSchema(SQLAlchemyAutoSchema):
    medio = EnumADiccionario(attribute='medio')
    class Meta:
        model = Album
        include_relationships = True
        load_instance = True

class CancionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cancion
        include_relationships = True
        load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True