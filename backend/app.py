from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///crm.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)
    
    # Import routes
    from backend.routes import auth, properties, leads, reports, ai_price, dashboard, integrations
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(properties.bp)
    app.register_blueprint(leads.bp)
    app.register_blueprint(reports.bp)
    app.register_blueprint(ai_price.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(integrations.bp)
    
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
