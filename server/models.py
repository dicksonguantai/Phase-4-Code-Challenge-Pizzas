from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer , primary_key= True)
    name = db.Column(db.String(30),unique = True, nullable = False)
    address = db.Column(db.String(150))
    pizzas = db.relationship("Pizza", secondary = "restaurant_pizzas",back_populates = "restaurants")


class Pizza(db.Model,SerializerMixin):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),nullable = False)
    ingredients = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    restaurants = db.relationship("Restaurant", secondary = "restaurant_pizzas", back_populates = "pizzas")

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key = True)
    price =db.Column(db.Float, nullable = False)
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer,db.ForeignKey('pizzas.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())    

    @validates()
    def validates_price(self,key,price):
        if isinstance(price, int) and (price >= 1 and price <=30):
            return price 
        else:
            raise ValueError("The Price can only be between 1 to 30")