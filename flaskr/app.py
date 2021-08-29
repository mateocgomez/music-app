from flaskr import create_app
from .modelos import db, Album, Usuario, Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

# Inicializamos la base de datos
db.init_app(app)
db.create_all()

# Test
with app.app_context():
    u = Usuario(nombre_usuario='dev', password='12345')
    a = Album(titulo='dev_prueba', year=1994, descripcion='holamundo', medio=Medio.CD)
    # Juntar los usuarios
    u.albumes.append(a)
    #Agregamos a la base de datos
    db.session.add(u)
    #Guardamos en la base de datos
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    # Eliminar algo en la BD
    db.session.delete(u)
    print(Album.query.all())
    print(Usuario.query.all())