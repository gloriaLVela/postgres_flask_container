import flask_sqlalchemy

# the db varaible is imported from here by the __init__.py, that is how the db.create_all()
# function knows which classes/tables to create in the database

db = flask_sqlalchemy.SQLAlchemy()

class Cats(db.model):
    __tablename__ = 'cats'
    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100))