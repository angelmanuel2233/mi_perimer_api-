from flask_restful import Resource 

class HelloWorld(Resource): 
        def get (salf): 
              return {"message":"hola munsdo la API", "status":200}
 

class APIRourtes():
  def init__routes(self,api):
    api.add_resource(HelloWorld, "/")

    