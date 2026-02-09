from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.ai_service import AIService
from backend.models.property import Property

bp = Blueprint('ai_price', __name__, url_prefix='/api/ai')

@bp.route('/suggest-price', methods=['POST'])
@login_required
def suggest_price():
    """Get AI suggested price for a property"""
    data = request.get_json()
    
    ai_service = AIService()
    
    # Create a temporary property object
    class TempProperty:
        def __init__(self, data):
            self.area = data.get('area')
            self.bedrooms = data.get('bedrooms')
            self.bathrooms = data.get('bathrooms')
            self.parking_spaces = data.get('parking_spaces')
            self.property_type = data.get('property_type')
            self.city = data.get('city')
            self.state = data.get('state')
    
    temp_property = TempProperty(data)
    suggested_price = ai_service.suggest_price(temp_property)
    
    return jsonify({
        'suggested_price': suggested_price,
        'confidence': ai_service.get_confidence_level(),
        'factors': ai_service.get_price_factors()
    }), 200

@bp.route('/market-analysis', methods=['GET'])
@login_required
def market_analysis():
    """Get market analysis for a location"""
    city = request.args.get('city')
    property_type = request.args.get('type')
    
    ai_service = AIService()
    analysis = ai_service.market_analysis(city, property_type)
    
    return jsonify(analysis), 200

@bp.route('/property-recommendations/<int:lead_id>', methods=['GET'])
@login_required
def property_recommendations(lead_id):
    """Get AI property recommendations for a lead"""
    ai_service = AIService()
    recommendations = ai_service.recommend_properties(lead_id)
    
    return jsonify({
        'recommendations': recommendations
    }), 200
