from backend.app import db
from datetime import datetime

class Lead(db.Model):
    __tablename__ = 'leads'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    whatsapp = db.Column(db.String(20))
    status = db.Column(db.String(20), default='novo')  # novo, contactado, interessado, negociando, convertido, perdido
    source = db.Column(db.String(50))  # website, whatsapp, indicação, redes sociais
    budget = db.Column(db.Float)
    property_interest = db.Column(db.String(100))
    location_preference = db.Column(db.String(100))
    notes = db.Column(db.Text)
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))
    interested_property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_contact = db.Column(db.DateTime)
    
    interested_property = db.relationship('Property', backref='interested_leads', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'whatsapp': self.whatsapp,
            'status': self.status,
            'source': self.source,
            'budget': self.budget,
            'property_interest': self.property_interest,
            'location_preference': self.location_preference,
            'notes': self.notes,
            'assigned_to': self.assigned_to,
            'interested_property_id': self.interested_property_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'last_contact': self.last_contact.isoformat() if self.last_contact else None
        }
