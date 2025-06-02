import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave-secreta')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///petscare.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
