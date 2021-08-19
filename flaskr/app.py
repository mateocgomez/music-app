from flaskr import create_app
from .modelos import db, Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

# Inicializamos la base de datos
db.init_app(app)
db.create_all()

# Test
with app.app_context():
    c = Cancion(titulo='dev', minutos=2, segundos =30, interprete='mateo')
    #Agregamos a la base de datos
    db.session.add(c)
    #Guardamos en la base de datos
    db.session.commit()
    print(Cancion.query.all())