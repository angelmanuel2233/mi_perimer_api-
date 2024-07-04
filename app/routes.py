from flask_restful import Resource 

from flask import request, jsonify 

from .methods import* 


from flask_jwt_extended import jwt_required, get_jwt_identity  


class HelloWorld(Resource):
  @jwt_required()    
  def get (salf):
   identidad =get_jwt_identity() 
   return {"mensaje", "hola indentidad", "estatus"/200}

class Almacen(Resource):
 def post(sel):
  parametro_id=request.args.get("id")
  parametro_nombre =request.args.get("nombre")
  
  return "buscar",parametro_id ,"nombre"( parametro_id, parametro_nombre)
      
class user_registre(Resource):
  def post(self): 
    data=request.form
    username =data.get("username")
    email = data.get("email")
    _password= data.get("password")
    #print(email, username, _password)
    respuesta,status=user_register(username,email, _password)
    
    return respuesta, status 
  
class user_login(Resource):
  def post(self): 
    data= request.form 
    email=data.get("email")
    password=data.get("pssword")
    
    respuesta,status= user_login(email,password)
    return respuesta, status    
   
def post(self):
  data = request.get_json()

  return crear_producto(data["nombre"], data["cantodad"])        
  

 
class APIRourtes():
  def init__routes(self,api):
   api.add_resource(HelloWorld, "/")
   api.add_resource(user_registre, "/usarios/registros")
   
    
   api.add_resource(Almacen, "/objetos_almacen")
    

