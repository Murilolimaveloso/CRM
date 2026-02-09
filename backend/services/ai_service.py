import numpy as np
from sklearn.ensemble import RandomForestRegressor
from backend.app import db
from backend.models.property import Property
from backend.models.lead import Lead

class AIService:
    """AI Service for price prediction and property recommendations"""
    
    def __init__(self):
        self.model = None
        self.confidence = 0.85
        
    def suggest_price(self, property_obj):
        """Suggest price for a property using AI model"""
        
        # Base price calculation using simple heuristics
        # In production, this would use a trained ML model
        
        base_price = 0
        
        # Area factor (R$ per m²)
        area_price_per_m2 = {
            'casa': 3000,
            'apartamento': 4000,
            'terreno': 1500,
            'comercial': 5000
        }
        
        property_type = property_obj.property_type or 'apartamento'
        area = property_obj.area or 50
        
        base_price = area * area_price_per_m2.get(property_type, 3500)
        
        # Bedroom multiplier
        bedrooms = property_obj.bedrooms or 2
        bedroom_multiplier = 1 + (bedrooms - 2) * 0.1
        
        # Bathroom multiplier
        bathrooms = property_obj.bathrooms or 1
        bathroom_multiplier = 1 + (bathrooms - 1) * 0.05
        
        # Parking multiplier
        parking = property_obj.parking_spaces or 0
        parking_multiplier = 1 + (parking * 0.08)
        
        # City multiplier (major cities cost more)
        city_multipliers = {
            'São Paulo': 1.5,
            'Rio de Janeiro': 1.4,
            'Brasília': 1.3,
            'Belo Horizonte': 1.2,
            'Curitiba': 1.15,
            'Porto Alegre': 1.15
        }
        
        city = property_obj.city or 'Outras'
        city_multiplier = city_multipliers.get(city, 1.0)
        
        # Calculate final suggested price
        suggested_price = base_price * bedroom_multiplier * bathroom_multiplier * parking_multiplier * city_multiplier
        
        # Add some randomness for variation (-5% to +5%)
        variation = np.random.uniform(0.95, 1.05)
        suggested_price *= variation
        
        return round(suggested_price, 2)
    
    def get_confidence_level(self):
        """Return confidence level of the AI prediction"""
        return self.confidence
    
    def get_price_factors(self):
        """Return factors that influence the price"""
        return {
            'area': 'Área total do imóvel',
            'location': 'Localização (cidade e bairro)',
            'bedrooms': 'Número de quartos',
            'bathrooms': 'Número de banheiros',
            'parking': 'Vagas de garagem',
            'property_type': 'Tipo do imóvel',
            'market_trend': 'Tendência de mercado',
            'amenities': 'Comodidades adicionais'
        }
    
    def market_analysis(self, city, property_type):
        """Analyze market for a specific location and property type"""
        
        # Get properties in the area
        query = Property.query
        
        if city:
            query = query.filter_by(city=city)
        if property_type:
            query = query.filter_by(property_type=property_type)
        
        properties = query.all()
        
        if not properties:
            return {
                'average_price': 0,
                'median_price': 0,
                'min_price': 0,
                'max_price': 0,
                'total_properties': 0,
                'trend': 'neutral'
            }
        
        prices = [p.price for p in properties]
        
        return {
            'average_price': round(np.mean(prices), 2),
            'median_price': round(np.median(prices), 2),
            'min_price': round(min(prices), 2),
            'max_price': round(max(prices), 2),
            'total_properties': len(properties),
            'trend': 'growing',  # Mock value
            'price_per_m2': round(np.mean([p.price/p.area for p in properties if p.area]), 2) if any(p.area for p in properties) else 0
        }
    
    def recommend_properties(self, lead_id):
        """Recommend properties for a lead based on their preferences"""
        
        lead = Lead.query.get(lead_id)
        if not lead:
            return []
        
        # Get properties matching lead's criteria
        query = Property.query.filter_by(status='disponível')
        
        # Filter by budget
        if lead.budget:
            query = query.filter(Property.price <= lead.budget * 1.1)  # 10% tolerance
        
        # Filter by location preference
        if lead.location_preference:
            query = query.filter_by(city=lead.location_preference)
        
        # Get top 10 recommendations
        properties = query.limit(10).all()
        
        # Calculate match score for each property
        recommendations = []
        for prop in properties:
            score = self._calculate_match_score(lead, prop)
            recommendations.append({
                'property': prop.to_dict(),
                'match_score': score,
                'reason': self._get_match_reason(lead, prop)
            })
        
        # Sort by match score
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        
        return recommendations
    
    def _calculate_match_score(self, lead, property):
        """Calculate how well a property matches a lead's preferences"""
        score = 0.5  # Base score
        
        # Budget match
        if lead.budget and property.price <= lead.budget:
            score += 0.3
        elif lead.budget and property.price <= lead.budget * 1.1:
            score += 0.15
        
        # Location match
        if lead.location_preference and property.city == lead.location_preference:
            score += 0.2
        
        return min(score, 1.0)
    
    def _get_match_reason(self, lead, property):
        """Get reason why property matches the lead"""
        reasons = []
        
        if lead.budget and property.price <= lead.budget:
            reasons.append('Dentro do orçamento')
        
        if lead.location_preference and property.city == lead.location_preference:
            reasons.append(f'Localizado em {property.city}')
        
        if property.ai_suggested_price and property.price < property.ai_suggested_price:
            reasons.append('Preço abaixo do valor de mercado')
        
        return ', '.join(reasons) if reasons else 'Disponível no momento'
