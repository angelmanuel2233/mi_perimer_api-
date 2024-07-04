from app.extensions import db                          

class producto (db.model): 
    __tablename__="objetos_almacen"
    
    id =db.column(db.Integer, primary_key=True)
    nombre = db.column(db.string(50), nullable=False)
    catidad = db.column(db.integar, nullabel=False)
    
    
    def __repr__(self):
        return f"<producto {self.nombre}>"
    