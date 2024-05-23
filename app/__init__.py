from flask import Flask 
from flask_restful import Api 
from .routes import APIRourtes

def crear_app(): 
    app = Flask (__name__)
    api =Api(app)

    routes = APIRourtes()
    routes.init__routes(api)
    
    
    return app 
