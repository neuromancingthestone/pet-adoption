from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!
class Pet(db.Model):
    """Pet model to store all pets in the DB"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)

    species = db.Column(db.String(30), nullable=False)

    photo_url = db.Column(db.String)

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.String(500), nullable=True)

    available = db.Column(db.Boolean, default=True, nullable=False)


                     


