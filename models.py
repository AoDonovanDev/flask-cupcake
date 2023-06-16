"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake."""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String(20),
                     nullable=False)
    size = db.Column(db.String(20),
                          nullable=False)
    rating = db.Column(db.Integer, 
                    nullable=False)
    image = db.Column(db.String(550),
                          nullable=True,
                          default='https://tinyurl.com/demo-cupcake')

    def __repr__(self):
        """Show info about cupcake."""

        c = self
        return f"<Cupcake {c.flavor} flavored cupcake >"