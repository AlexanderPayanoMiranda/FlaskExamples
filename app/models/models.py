from app.db import db
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    sobre_mi = db.Column(db.String(100))
    miembro_desde = db.Column(db.DateTime(), default=func.now())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, nombre, apellido, email, sobre_mi):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.sobre_mi = sobre_mi
