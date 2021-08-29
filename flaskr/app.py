from flaskr import create_app
from .modelos import db, Album, Usuario, Medio, Cancion
from .modelos import AlbumSchema, UsuarioSchema, CancionSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

# Inicializamos la base de datos
db.init_app(app)
db.create_all()

# Test
with app.app_context():
    album_schema = AlbumSchema()
    cancion_schema = CancionSchema()
    usuario_schema = UsuarioSchema()
    A = Album(titulo='Prueba', year=1994, descripcion='holoa', medio=Medio.CD)
    U = Usuario(nombre_usuario='Prueba', password='12345')
    C = Cancion(titulo='Prueba', minutos=1994, segundos=20, interprete='mateodev')
    db.session.add(A)
    db.session.add(U)
    db.session.add(C)
    db.session.commit()
    print([album_schema.dumps(album) for album in Album.query.all()])
    print([cancion_schema.dumps(cancion) for cancion in Cancion.query.all()])
    print([usuario_schema.dumps(usuario) for usuario in Usuario.query.all()])