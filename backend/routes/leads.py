from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.app import db
from backend.models.lead import Lead
from datetime import datetime

bp = Blueprint('leads', __name__, url_prefix='/api/leads')

@bp.route('/', methods=['GET'])
@login_required
def get_leads():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    status = request.args.get('status')
    source = request.args.get('source')
    
    query = Lead.query
    
    if status:
        query = query.filter_by(status=status)
    if source:
        query = query.filter_by(source=source)
    
    # Filter by assigned agent if not admin
    if current_user.role != 'admin':
        query = query.filter_by(assigned_to=current_user.id)
    
    leads = query.order_by(Lead.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'leads': [lead.to_dict() for lead in leads.items],
        'total': leads.total,
        'pages': leads.pages,
        'current_page': page
    }), 200

@bp.route('/<int:lead_id>', methods=['GET'])
@login_required
def get_lead(lead_id):
    lead = Lead.query.get_or_404(lead_id)
    return jsonify({'lead': lead.to_dict()}), 200

@bp.route('/', methods=['POST'])
@login_required
def create_lead():
    data = request.get_json()
    
    lead = Lead(
        name=data['name'],
        email=data.get('email'),
        phone=data.get('phone'),
        whatsapp=data.get('whatsapp'),
        status=data.get('status', 'novo'),
        source=data.get('source'),
        budget=data.get('budget'),
        property_interest=data.get('property_interest'),
        location_preference=data.get('location_preference'),
        notes=data.get('notes'),
        assigned_to=data.get('assigned_to', current_user.id),
        interested_property_id=data.get('interested_property_id')
    )
    
    db.session.add(lead)
    db.session.commit()
    
    return jsonify({
        'message': 'Lead created successfully',
        'lead': lead.to_dict()
    }), 201

@bp.route('/<int:lead_id>', methods=['PUT'])
@login_required
def update_lead(lead_id):
    lead = Lead.query.get_or_404(lead_id)
    data = request.get_json()
    
    for field in ['name', 'email', 'phone', 'whatsapp', 'status', 'source', 
                  'budget', 'property_interest', 'location_preference', 'notes', 
                  'assigned_to', 'interested_property_id']:
        if field in data:
            setattr(lead, field, data[field])
    
    if 'status' in data:
        lead.last_contact = datetime.utcnow()
    
    db.session.commit()
    
    return jsonify({
        'message': 'Lead updated successfully',
        'lead': lead.to_dict()
    }), 200

@bp.route('/<int:lead_id>', methods=['DELETE'])
@login_required
def delete_lead(lead_id):
    lead = Lead.query.get_or_404(lead_id)
    db.session.delete(lead)
    db.session.commit()
    
    return jsonify({'message': 'Lead deleted successfully'}), 200
