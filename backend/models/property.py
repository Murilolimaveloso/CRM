from backend.app import db
from datetime import datetime

class Property(db.Model):
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    property_type = db.Column(db.String(50))  # casa, apartamento, terreno, comercial
    status = db.Column(db.String(20), default='disponível')  # disponível, vendido, alugado
    price = db.Column(db.Float, nullable=False)
    area = db.Column(db.Float)  # metros quadrados
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    parking_spaces = db.Column(db.Integer)
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.String(20))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    images = db.Column(db.Text)  # JSON array of image URLs
    amenities = db.Column(db.Text)  # JSON array of amenities
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ai_suggested_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'property_type': self.property_type,
            'status': self.status,
            'price': self.price,
            'area': self.area,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'parking_spaces': self.parking_spaces,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'images': self.images,
            'amenities': self.amenities,
            'ai_suggested_price': self.ai_suggested_price,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
