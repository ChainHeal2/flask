"""usar __init__ lo que hace es que interprete la carpeta de aplicacion
como si esta fuera un modulo

para que funcione debemos usar export FLASK_APP=aplicacion:create_app
para que la variable de entorno detecte que estamos usando nuestra app
"""
import os
from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        secret_key = "mikey",
        database_host = os.environ.get('flask_database_host'),
        database_password = os.environ.get('flask_database_password'),
        database_user = os.environ.get('flask_database_user'),
        database_datbase = os.environ.get('flask_database_'),
    )
    
    @app.route('/')
    def hola():
        return 'hola mundo'
    return app