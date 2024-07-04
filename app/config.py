class Config: 
    SQLALCHEMY_DATABASE_URI ="postegresql +psycopg2://contraseña@/mi_almacen"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "bac66c29cd653939f508290e58801e34"
    JWT_ALGORITHM = "HS256"