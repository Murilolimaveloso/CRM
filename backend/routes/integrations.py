from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.whatsapp_service import WhatsAppService
from backend.services.payment_service import PaymentService

bp = Blueprint('integrations', __name__, url_prefix='/api/integrations')

@bp.route('/whatsapp/send', methods=['POST'])
@login_required
def send_whatsapp():
    """Send WhatsApp message"""
    data = request.get_json()
    
    whatsapp_service = WhatsAppService()
    result = whatsapp_service.send_message(
        to=data['to'],
        message=data['message']
    )
    
    return jsonify(result), 200

@bp.route('/whatsapp/send-template', methods=['POST'])
@login_required
def send_whatsapp_template():
    """Send WhatsApp template message"""
    data = request.get_json()
    
    whatsapp_service = WhatsAppService()
    result = whatsapp_service.send_template(
        to=data['to'],
        template_name=data['template_name'],
        parameters=data.get('parameters', [])
    )
    
    return jsonify(result), 200

@bp.route('/payment/pix/create', methods=['POST'])
@login_required
def create_pix_payment():
    """Create Pix payment"""
    data = request.get_json()
    
    payment_service = PaymentService()
    result = payment_service.create_pix_payment(
        amount=data['amount'],
        description=data.get('description', ''),
        customer_info=data.get('customer_info', {})
    )
    
    return jsonify(result), 200

@bp.route('/payment/card/create', methods=['POST'])
@login_required
def create_card_payment():
    """Create card payment"""
    data = request.get_json()
    
    payment_service = PaymentService()
    result = payment_service.create_card_payment(
        amount=data['amount'],
        card_token=data['card_token'],
        installments=data.get('installments', 1),
        description=data.get('description', '')
    )
    
    return jsonify(result), 200

@bp.route('/payment/status/<payment_id>', methods=['GET'])
@login_required
def get_payment_status(payment_id):
    """Get payment status"""
    payment_service = PaymentService()
    result = payment_service.get_payment_status(payment_id)
    
    return jsonify(result), 200
