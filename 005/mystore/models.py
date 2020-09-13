from . import db 
# Database models for mystore

class Item(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True)
    price = db.Column(db.Float)
    in_stock = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'<Item: {self.name}>'