from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.app import db
from backend.models.property import Property
from backend.models.lead import Lead
from backend.models.transaction import Transaction
from sqlalchemy import func
from datetime import datetime, timedelta

bp = Blueprint('reports', __name__, url_prefix='/api/reports')

@bp.route('/overview', methods=['GET'])
@login_required
def get_overview():
    # Get total counts
    total_properties = Property.query.count()
    total_leads = Lead.query.count()
    total_transactions = Transaction.query.filter_by(status='pago').count()
    
    # Get properties by status
    properties_by_status = db.session.query(
        Property.status, func.count(Property.id)
    ).group_by(Property.status).all()
    
    # Get leads by status
    leads_by_status = db.session.query(
        Lead.status, func.count(Lead.id)
    ).group_by(Lead.status).all()
    
    # Get revenue
    total_revenue = db.session.query(
        func.sum(Transaction.amount)
    ).filter_by(status='pago').scalar() or 0
    
    # Monthly revenue (last 12 months)
    twelve_months_ago = datetime.utcnow() - timedelta(days=365)
    monthly_revenue = db.session.query(
        func.strftime('%Y-%m', Transaction.paid_at).label('month'),
        func.sum(Transaction.amount).label('revenue')
    ).filter(
        Transaction.status == 'pago',
        Transaction.paid_at >= twelve_months_ago
    ).group_by('month').all()
    
    return jsonify({
        'total_properties': total_properties,
        'total_leads': total_leads,
        'total_transactions': total_transactions,
        'total_revenue': total_revenue,
        'properties_by_status': dict(properties_by_status),
        'leads_by_status': dict(leads_by_status),
        'monthly_revenue': [{'month': m, 'revenue': r} for m, r in monthly_revenue]
    }), 200

@bp.route('/properties', methods=['GET'])
@login_required
def get_property_report():
    # Properties by type
    by_type = db.session.query(
        Property.property_type, func.count(Property.id)
    ).group_by(Property.property_type).all()
    
    # Average price by type
    avg_price = db.session.query(
        Property.property_type, func.avg(Property.price)
    ).group_by(Property.property_type).all()
    
    # Properties by city
    by_city = db.session.query(
        Property.city, func.count(Property.id)
    ).group_by(Property.city).limit(10).all()
    
    return jsonify({
        'by_type': dict(by_type),
        'avg_price_by_type': {t: round(p, 2) for t, p in avg_price},
        'by_city': dict(by_city)
    }), 200

@bp.route('/leads', methods=['GET'])
@login_required
def get_lead_report():
    # Leads by source
    by_source = db.session.query(
        Lead.source, func.count(Lead.id)
    ).group_by(Lead.source).all()
    
    # Conversion rate
    total_leads = Lead.query.count()
    converted_leads = Lead.query.filter_by(status='convertido').count()
    conversion_rate = (converted_leads / total_leads * 100) if total_leads > 0 else 0
    
    # Average response time (mock data for now)
    avg_response_time = 2.5  # hours
    
    return jsonify({
        'by_source': dict(by_source),
        'conversion_rate': round(conversion_rate, 2),
        'avg_response_time': avg_response_time,
        'total_leads': total_leads,
        'converted_leads': converted_leads
    }), 200

@bp.route('/sales', methods=['GET'])
@login_required
def get_sales_report():
    # Total sales
    total_sales = Transaction.query.filter_by(status='pago').count()
    total_revenue = db.session.query(
        func.sum(Transaction.amount)
    ).filter_by(status='pago').scalar() or 0
    
    # Sales by payment method
    by_payment = db.session.query(
        Transaction.payment_method, func.count(Transaction.id)
    ).filter_by(status='pago').group_by(Transaction.payment_method).all()
    
    # Top performing agents (mock for now)
    top_agents = []
    
    return jsonify({
        'total_sales': total_sales,
        'total_revenue': total_revenue,
        'by_payment_method': dict(by_payment),
        'top_agents': top_agents
    }), 200
