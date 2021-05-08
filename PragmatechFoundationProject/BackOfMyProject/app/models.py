from app import db
    
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25))
class Advantage(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    icon = db.Column(db.String(250))
    text = db.Column(db.String(255))