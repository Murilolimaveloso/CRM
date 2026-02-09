from backend.app import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20))  # venda, aluguel
    payment_method = db.Column(db.String(20))  # pix, cartão, boleto, transferência
    status = db.Column(db.String(20), default='pendente')  # pendente, pago, cancelado
    payment_reference = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    paid_at = db.Column(db.DateTime)
    
    property = db.relationship('Property', backref='transactions')
    lead = db.relationship('Lead', backref='transactions')
    
    def to_dict(self):
        return {
            'id': self.id,
            'property_id': self.property_id,
            'lead_id': self.lead_id,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'payment_method': self.payment_method,
            'status': self.status,
            'payment_reference': self.payment_reference,
            'created_at': self.created_at.isoformat(),
            'paid_at': self.paid_at.isoformat() if self.paid_at else None
        }
