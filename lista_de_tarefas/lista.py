import os
from flask import Flask
from config import Config
from controllers.lista_controller import ListaController
from models.listadb import db

lista = Flask(__name__, template_folder=os.path.join('view', 'templates'))
lista.config.from_object(Config)

db.init_app(lista)

with lista.app_context():
    db.create_all()

lista.add_url_rule('/', 'index', ListaController.index)

if __name__ == '__main__':
    lista.run(debug=True)