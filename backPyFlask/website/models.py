# En esta página, creamos los modelos de la base de datos
from . import db  # Importamos del paquete, carpeta 'website' el objeto 'db'.
# Si estuviesemos fuera del directorio 'website', en lugar de poner '.', deberiamos poner 'website'

from flask_login import UserMixin
from sql_alchemy import func


class Note(db.Model):  # Todos las 'Note' deben cumplir esto
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1500))
    database = db.Column(db.DateTime(timezone=True), default=func.now())
    # En la siguiente linea, asociamos informacion con el 'user'
    # Una columna que hace referencia a otra columna dentro de la base de datos
    # Queremos asociar la nota con el 'id' del 'user'. El 'db.Integer', debe coincidir.
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'))
    # En la linea anterior, 'user' hace referencia a la class/tabla 'User'. Aunque sea en Capital 'U', a
    # la hora de leerlo, lo hace en minúscula. el 'id', corresponde al 'field'.


# Solo en el caso de 'User', debemos poner tambien 'UserMixin' # Todos los 'User' deben cumplir esto
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # 150 es la longitud máxima aceptada. 'unique=True' hace que dos usuarios no puedan tener el mismo email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
