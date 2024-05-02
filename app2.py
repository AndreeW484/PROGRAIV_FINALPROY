from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://AndreeW484:Invierno2024@localhost/biblioteca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    contrasena = db.Column(db.String(35), unique=True, nullable=False)

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date)
    pais = db.Column(db.String(40))

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    editorial = db.Column(db.String(40))
    fecha_publicacion = db.Column(db.Date)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    numero_paginas = db.Column(db.Integer)
    genero = db.Column(db.String(30))
    idioma = db.Column(db.String(30))
    
class Libro_Autor(db.Model):
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), primary_key=True)
    id_autor = db.Column(db.Integer, db. ForeignKey('autor.id'), primary_key=True)

class Usuario_Libro(db.Model):
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), primary_key=True)

with app.app_context():
    db.create_all()
    print("¡Tablas creadas correctamente en la base de datos!")

