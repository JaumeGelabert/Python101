from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Creamos nueva base de datos [OBJETO]
DB_NAME = "database.db"  # Nombre de la base de datos


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'barcelona'
    #En la siguiente linea, decimos a 'Flask' donde esta localizada la base de datos
    #En este caso, se guarda dentro de la carpeta 'website'
    # f-string, solo funciona en Python3.6 o superior
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) # Inicializamos la base de datos

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
