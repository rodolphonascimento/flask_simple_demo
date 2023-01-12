from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Providers(db.Model):
   id = db.Column('id', db.String(16), primary_key=True)
   name = db.Column(db.String(100))
   company = db.Column(db.String(50))  
   created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
   amount_products = db.Column(db.String(10))
   
   @classmethod
   def serialize(self, provider):
      return {
         "name": provider.name,
         "id": provider.id,
         "company": provider.company,
         "created_at": provider.created_at,
         "amount_products": provider.amount_products
      }
   
   
def get_database():
   return db

def init_database(app):
   db.init_app(app)

   with app.app_context():
      db.create_all()