from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

 
class Providers(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   company = db.Column(db.String(50))  
   #created_at = db.Column(db.DateFi)
   amount_products = db.Column(db.String(10))
   
   

def init_database(app):
   db.init_app(app)

   with app.app_context():
      db.create_all()