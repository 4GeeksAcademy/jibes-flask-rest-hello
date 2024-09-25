from flask_sqlalchemy import SQLAlchemy
# this is where you make your tables
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorites": [favorite.serialize() for favorite in self.favorites] #self.favorites becomes a new list; favorite.serialize makes the favorite into a dictionary rep for json format
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id= db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    planet_id= db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    user = db.relationship('User', backref= 'favorites') #establish a relationship between a user and their favorites
    planet = db.relationship('Planet', backref= 'favorites') #establish a 'route' between the planets and the favorite list
    character = db.relationship('Character', backref='favorites') #establish a 'route' between the character and the favorite list


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'character_id': self.character_id,
            'planet_id': self.planet_id,

        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(120))
    mass = db.Column(db.String(120))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'hair_color': self.hair_color,
            'mass': self.mass,
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(120))
    terrain = db.Column(db.String(120))

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'gravity': self.gravity,
            'terrain': self.terrain,
        }