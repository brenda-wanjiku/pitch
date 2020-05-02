from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(225))
    pitches = db.relationship('Pitch', backref = 'pitch', lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch_title = db.Column(db.String(225))
    pitch_content = db.Column(db.String(225))
    pitch_category = db.Column(db.String(225))

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User {self.username}'