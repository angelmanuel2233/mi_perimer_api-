from flask import Flask 
from flask_restful import Api 
from .routes import APIRourtes
from .config import Config  
from .extensions import db, jwt 

def crear_app(): 
    app = Flask (__name__)

    app.config.from_object(Config)
    
    db.init_app(app)
    
    jwt.init_app(app)

    with app.app_context():
     db.create_all()

    api =Api(app)

    routes = APIRourtes()
    routes.init__routes(api)
    
    
    return app 
