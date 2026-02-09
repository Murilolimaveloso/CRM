from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.app import db
from backend.models.property import Property
from backend.services.ai_service import AIService

bp = Blueprint('properties', __name__, url_prefix='/api/properties')

@bp.route('/', methods=['GET'])
def get_properties():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    property_type = request.args.get('type')
    status = request.args.get('status')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    city = request.args.get('city')
    
    query = Property.query
    
    if property_type:
        query = query.filter_by(property_type=property_type)
    if status:
        query = query.filter_by(status=status)
    if min_price:
        query = query.filter(Property.price >= min_price)
    if max_price:
        query = query.filter(Property.price <= max_price)
    if city:
        query = query.filter_by(city=city)
    
    properties = query.paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'properties': [prop.to_dict() for prop in properties.items],
        'total': properties.total,
        'pages': properties.pages,
        'current_page': page
    }), 200

@bp.route('/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = Property.query.get_or_404(property_id)
    return jsonify({'property': property.to_dict()}), 200

@bp.route('/', methods=['POST'])
@login_required
def create_property():
    data = request.get_json()
    
    property = Property(
        title=data['title'],
        description=data.get('description'),
        property_type=data['property_type'],
        price=data['price'],
        area=data.get('area'),
        bedrooms=data.get('bedrooms'),
        bathrooms=data.get('bathrooms'),
        parking_spaces=data.get('parking_spaces'),
        address=data.get('address'),
        city=data.get('city'),
        state=data.get('state'),
        zip_code=data.get('zip_code'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        images=data.get('images'),
        amenities=data.get('amenities'),
        owner_id=current_user.id
    )
    
    # Get AI suggested price
    ai_service = AIService()
    property.ai_suggested_price = ai_service.suggest_price(property)
    
    db.session.add(property)
    db.session.commit()
    
    return jsonify({
        'message': 'Property created successfully',
        'property': property.to_dict()
    }), 201

@bp.route('/<int:property_id>', methods=['PUT'])
@login_required
def update_property(property_id):
    property = Property.query.get_or_404(property_id)
    data = request.get_json()
    
    # Update fields
    for field in ['title', 'description', 'property_type', 'status', 'price', 'area', 
                  'bedrooms', 'bathrooms', 'parking_spaces', 'address', 'city', 'state', 
                  'zip_code', 'latitude', 'longitude', 'images', 'amenities']:
        if field in data:
            setattr(property, field, data[field])
    
    # Recalculate AI suggested price if relevant fields changed
    if any(field in data for field in ['area', 'bedrooms', 'bathrooms', 'city', 'property_type']):
        ai_service = AIService()
        property.ai_suggested_price = ai_service.suggest_price(property)
    
    db.session.commit()
    
    return jsonify({
        'message': 'Property updated successfully',
        'property': property.to_dict()
    }), 200

@bp.route('/<int:property_id>', methods=['DELETE'])
@login_required
def delete_property(property_id):
    property = Property.query.get_or_404(property_id)
    db.session.delete(property)
    db.session.commit()
    
    return jsonify({'message': 'Property deleted successfully'}), 200
