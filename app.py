from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://AndreeW484:Invierno2024@localhost/biblioteca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


def verificar_conexion_db():
    try:
        with app.app_context():
            db.session.execute(text('SELECT 1'))  
            print('¡Conexión a la base de datos exitosa!')
    except Exception as e:
        print('Error al conectar a la base de datos:', e)

if __name__ == '__main__':
    verificar_conexion_db()  
    app.run(debug=True)
