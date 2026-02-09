from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.app import db
from backend.models.property import Property
from backend.models.lead import Lead
from backend.models.transaction import Transaction
from sqlalchemy import func
from datetime import datetime, timedelta

bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')

@bp.route('/stats', methods=['GET'])
@login_required
def get_dashboard_stats():
    """Get dashboard statistics"""
    
    # Today's stats
    today = datetime.utcnow().date()
    
    # New leads today
    new_leads_today = Lead.query.filter(
        func.date(Lead.created_at) == today
    ).count()
    
    # New properties today
    new_properties_today = Property.query.filter(
        func.date(Property.created_at) == today
    ).count()
    
    # Active properties
    active_properties = Property.query.filter_by(status='disponível').count()
    
    # Leads by status
    leads_novo = Lead.query.filter_by(status='novo').count()
    leads_contactado = Lead.query.filter_by(status='contactado').count()
    leads_interessado = Lead.query.filter_by(status='interessado').count()
    leads_negociando = Lead.query.filter_by(status='negociando').count()
    
    # Recent activity
    recent_leads = Lead.query.order_by(Lead.created_at.desc()).limit(5).all()
    recent_properties = Property.query.order_by(Property.created_at.desc()).limit(5).all()
    
    # This month's revenue
    first_day_of_month = datetime.utcnow().replace(day=1)
    monthly_revenue = db.session.query(
        func.sum(Transaction.amount)
    ).filter(
        Transaction.status == 'pago',
        Transaction.paid_at >= first_day_of_month
    ).scalar() or 0
    
    return jsonify({
        'new_leads_today': new_leads_today,
        'new_properties_today': new_properties_today,
        'active_properties': active_properties,
        'leads_by_status': {
            'novo': leads_novo,
            'contactado': leads_contactado,
            'interessado': leads_interessado,
            'negociando': leads_negociando
        },
        'recent_leads': [lead.to_dict() for lead in recent_leads],
        'recent_properties': [prop.to_dict() for prop in recent_properties],
        'monthly_revenue': monthly_revenue
    }), 200

@bp.route('/charts/leads-trend', methods=['GET'])
@login_required
def get_leads_trend():
    """Get leads trend for the last 30 days"""
    days = request.args.get('days', 30, type=int)
    start_date = datetime.utcnow() - timedelta(days=days)
    
    leads_by_day = db.session.query(
        func.date(Lead.created_at).label('date'),
        func.count(Lead.id).label('count')
    ).filter(
        Lead.created_at >= start_date
    ).group_by('date').all()
    
    return jsonify({
        'data': [{'date': str(date), 'count': count} for date, count in leads_by_day]
    }), 200

@bp.route('/charts/revenue-trend', methods=['GET'])
@login_required
def get_revenue_trend():
    """Get revenue trend"""
    months = request.args.get('months', 12, type=int)
    start_date = datetime.utcnow() - timedelta(days=months*30)
    
    revenue_by_month = db.session.query(
        func.strftime('%Y-%m', Transaction.paid_at).label('month'),
        func.sum(Transaction.amount).label('revenue')
    ).filter(
        Transaction.status == 'pago',
        Transaction.paid_at >= start_date
    ).group_by('month').all()
    
    return jsonify({
        'data': [{'month': month, 'revenue': revenue} for month, revenue in revenue_by_month]
    }), 200
