"""
Database initialization script
Creates initial data for the CRM system
"""

from backend.app import create_app, db
from backend.models.user import User
from backend.models.property import Property
from backend.models.lead import Lead
from backend.models.transaction import Transaction
from datetime import datetime, timedelta
import random

def init_database():
    """Initialize database with sample data"""
    
    app = create_app()
    
    with app.app_context():
        # Drop all tables and recreate
        print("Creating database tables...")
        db.create_all()
        
        # Create admin user
        print("Creating admin user...")
        admin = User(
            username='admin',
            email='admin@crm.com',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        
        # Create agent users
        print("Creating agent users...")
        agent1 = User(
            username='joao',
            email='joao@crm.com',
            role='agent'
        )
        agent1.set_password('senha123')
        db.session.add(agent1)
        
        agent2 = User(
            username='maria',
            email='maria@crm.com',
            role='agent'
        )
        agent2.set_password('senha123')
        db.session.add(agent2)
        
        db.session.commit()
        
        # Create sample properties
        print("Creating sample properties...")
        properties_data = [
            {
                'title': 'Apartamento Luxo 3 Quartos',
                'description': 'Lindo apartamento com vista panorâmica, acabamento de primeira qualidade',
                'property_type': 'apartamento',
                'price': 450000,
                'area': 120,
                'bedrooms': 3,
                'bathrooms': 2,
                'parking_spaces': 2,
                'address': 'Rua das Flores, 123',
                'city': 'São Paulo',
                'state': 'SP',
                'zip_code': '01234-567',
                'status': 'disponível',
                'owner_id': admin.id
            },
            {
                'title': 'Casa Condomínio Fechado',
                'description': 'Casa ampla em condomínio de alto padrão com área de lazer completa',
                'property_type': 'casa',
                'price': 650000,
                'area': 200,
                'bedrooms': 4,
                'bathrooms': 3,
                'parking_spaces': 3,
                'address': 'Av. Principal, 456',
                'city': 'São Paulo',
                'state': 'SP',
                'zip_code': '01234-890',
                'status': 'disponível',
                'owner_id': admin.id
            },
            {
                'title': 'Cobertura Vista Mar',
                'description': 'Cobertura duplex com piscina privativa e vista deslumbrante para o mar',
                'property_type': 'apartamento',
                'price': 1200000,
                'area': 250,
                'bedrooms': 5,
                'bathrooms': 4,
                'parking_spaces': 4,
                'address': 'Av. Atlântica, 789',
                'city': 'Rio de Janeiro',
                'state': 'RJ',
                'zip_code': '22000-000',
                'status': 'disponível',
                'owner_id': admin.id
            },
            {
                'title': 'Loja Comercial Centro',
                'description': 'Ponto comercial estratégico no centro da cidade',
                'property_type': 'comercial',
                'price': 350000,
                'area': 80,
                'bedrooms': 0,
                'bathrooms': 2,
                'parking_spaces': 1,
                'address': 'Rua do Comércio, 100',
                'city': 'Belo Horizonte',
                'state': 'MG',
                'zip_code': '30000-000',
                'status': 'disponível',
                'owner_id': admin.id
            },
            {
                'title': 'Terreno 500m²',
                'description': 'Terreno plano pronto para construção',
                'property_type': 'terreno',
                'price': 200000,
                'area': 500,
                'bedrooms': 0,
                'bathrooms': 0,
                'parking_spaces': 0,
                'address': 'Rua Nova Esperança, 50',
                'city': 'Curitiba',
                'state': 'PR',
                'zip_code': '80000-000',
                'status': 'disponível',
                'owner_id': admin.id
            }
        ]
        
        for prop_data in properties_data:
            prop = Property(**prop_data)
            db.session.add(prop)
        
        db.session.commit()
        
        # Create sample leads
        print("Creating sample leads...")
        leads_data = [
            {
                'name': 'João Silva',
                'email': 'joao.silva@email.com',
                'phone': '(11) 98765-4321',
                'whatsapp': '5511987654321',
                'status': 'novo',
                'source': 'website',
                'budget': 400000,
                'property_interest': 'Apartamento',
                'location_preference': 'São Paulo',
                'assigned_to': agent1.id
            },
            {
                'name': 'Maria Santos',
                'email': 'maria.santos@email.com',
                'phone': '(11) 97654-3210',
                'whatsapp': '5511976543210',
                'status': 'contactado',
                'source': 'whatsapp',
                'budget': 600000,
                'property_interest': 'Casa',
                'location_preference': 'São Paulo',
                'assigned_to': agent1.id,
                'last_contact': datetime.utcnow() - timedelta(days=1)
            },
            {
                'name': 'Pedro Oliveira',
                'email': 'pedro.oliveira@email.com',
                'phone': '(11) 96543-2109',
                'whatsapp': '5511965432109',
                'status': 'interessado',
                'source': 'indicação',
                'budget': 350000,
                'property_interest': 'Apartamento',
                'location_preference': 'São Paulo',
                'assigned_to': agent2.id,
                'last_contact': datetime.utcnow() - timedelta(hours=12)
            },
            {
                'name': 'Ana Costa',
                'email': 'ana.costa@email.com',
                'phone': '(11) 95432-1098',
                'whatsapp': '5511954321098',
                'status': 'negociando',
                'source': 'redes sociais',
                'budget': 800000,
                'property_interest': 'Casa',
                'location_preference': 'São Paulo',
                'assigned_to': agent2.id,
                'last_contact': datetime.utcnow() - timedelta(hours=6)
            },
            {
                'name': 'Carlos Pereira',
                'email': 'carlos.pereira@email.com',
                'phone': '(11) 94321-0987',
                'whatsapp': '5511943210987',
                'status': 'convertido',
                'source': 'website',
                'budget': 450000,
                'property_interest': 'Apartamento',
                'location_preference': 'São Paulo',
                'assigned_to': agent1.id,
                'last_contact': datetime.utcnow() - timedelta(hours=2)
            }
        ]
        
        for lead_data in leads_data:
            lead = Lead(**lead_data)
            db.session.add(lead)
        
        db.session.commit()
        
        print("✅ Database initialized successfully!")
        print("\nLogin credentials:")
        print("Username: admin")
        print("Password: admin123")
        print("\nAgent credentials:")
        print("Username: joao / Password: senha123")
        print("Username: maria / Password: senha123")

if __name__ == '__main__':
    init_database()
