import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WhatsAppService:
    """Service for WhatsApp Business API integration"""
    
    def __init__(self):
        self.api_key = os.getenv('WHATSAPP_API_KEY')
        self.phone_id = os.getenv('WHATSAPP_PHONE_ID')
        self.api_url = 'https://graph.facebook.com/v17.0'
    
    def send_message(self, to, message):
        """Send a WhatsApp message"""
        
        if not self.api_key:
            return {
                'success': False,
                'error': 'WhatsApp API key not configured',
                'demo_mode': True
            }
        
        url = f'{self.api_url}/{self.phone_id}/messages'
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'messaging_product': 'whatsapp',
            'to': to,
            'type': 'text',
            'text': {
                'body': message
            }
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            
            return {
                'success': True,
                'message_id': response.json().get('messages', [{}])[0].get('id')
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def send_template(self, to, template_name, parameters=None):
        """Send a WhatsApp template message"""
        
        if not self.api_key:
            return {
                'success': False,
                'error': 'WhatsApp API key not configured',
                'demo_mode': True
            }
        
        url = f'{self.api_url}/{self.phone_id}/messages'
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'messaging_product': 'whatsapp',
            'to': to,
            'type': 'template',
            'template': {
                'name': template_name,
                'language': {
                    'code': 'pt_BR'
                }
            }
        }
        
        if parameters:
            data['template']['components'] = [
                {
                    'type': 'body',
                    'parameters': [
                        {'type': 'text', 'text': param} for param in parameters
                    ]
                }
            ]
        
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            
            return {
                'success': True,
                'message_id': response.json().get('messages', [{}])[0].get('id')
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def send_property_notification(self, to, property_data):
        """Send property details to a lead via WhatsApp"""
        
        message = f"""
🏠 *Novo Imóvel Disponível*

*Título:* {property_data['title']}
*Tipo:* {property_data['property_type']}
*Preço:* R$ {property_data['price']:,.2f}
*Área:* {property_data['area']} m²
*Quartos:* {property_data['bedrooms']}
*Banheiros:* {property_data['bathrooms']}
*Localização:* {property_data['address']}, {property_data['city']}

{property_data['description']}

Entre em contato para agendar uma visita!
        """.strip()
        
        return self.send_message(to, message)
