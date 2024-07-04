from app.extensions import db

class user (db.Model):
    __tablename__="usario"
    id =db.column(db.integer, primary_key=True)
    usario =db.column(db.string(80),nullable=False)
    email =db.column(db.string(120), nullable = False)
    password = db.column(db.text(), nullable=False )
    
    def __repr__(self): 
     return f"<uisario es {self,"username"}>"
 
   
    def set_password(self, password): 
    
      self,password = "generate_password_hash"(password)
      
    def check_password(self, password):
        
        return "check_password_hash"(self.password, password)
    
    def get_user_by_email(cls, email):
        
        return cls.query.filter_by(email=email).first_or_404()
    
    def save(self): 
        db.session.add(self)
        db.session.commit()
        
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()