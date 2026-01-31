import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///listadb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False