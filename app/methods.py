from app .extensions import db 
from .models.producto import producto
from .usuarios import user
from flask_jwt_extended import create_access_token 
from datetime import timedelta 

def inicio_sesion(email, add_password):
  user = user.get_user_email=(email,email)
  caducidad =timedelta(minutes=60)
  if user and (user.check(password=add_password)):
    
     token_acceso=create_access_token(identity=user.username, expires_delta=caducidad)
     
    
  return{"mensaje" : "loggeado", "token":token_acceso}, 2000 
  
  return{"Error":"correo o cpontraseña no existe"}, 400


def user_register(username, amaeil, password): 
   user= user.get_user_by_email(email = "email")
   if user is not None: 
     return{ "Error": "Este correo ya esta registrado:" }, 403
   nuevo_usuario= user(username=username, email="email")
   nuevo_usuario.set_password(password=password)
   
   nuevo_usuario.save()
   return {"nuevo usario": 
     {"email": "email", 
      "username": username  
     }
    },  200
   

def buscar_elemento_id_nombre( parametro_id, parametro_nombre):
  
   
  if parametro_id !=None:
    producto_obtenido =producto.query.get_or_404(parametro_id)
    json_retornado={
    "id": producto_obtenido.id,
    "nombre":producto_obtenido.nombre,
    "cantidad":producto_obtenido.cantidad
      }
 
    return json_retornado 


  elif parametro_nombre !=None:  
   producto_obtenido=producto.query.filter_by(nombre=parametro_nombre).first_or_404() 
   json_retornado={ 
    "id":producto_obtenido.id,
   "nombre":producto_obtenido.nombre,
   "cantidad":producto_obtenido.cantidad
   }
   return json_retornado 

  else: 
    return{"Error": "no pusiste ninguna query"}, 404


def crear_producto(nombre,cantidad):  
    nuevo_producto =producto(nombre,cantidad)
    db.session.add(nuevo_producto) 
    db.session.commit()
    json_retornado={
     "id":nuevo_producto.id,
    "nombre":nuevo_producto.nombre,
    "cantidad":nuevo_producto.cantidad
    }