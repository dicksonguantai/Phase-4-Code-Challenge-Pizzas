from faker import Faker
from random import randint, choice as rc 
from app import app 
from models import db,Pizza,Restaurant,RestaurantPizza

fake = Faker()


with app.app_context():
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    pizzas = []
    for i in range(15):
        pizza = Pizza(name = fake.pizza(), address =fake.address())
        pizzas.append(pizza)

    db.session.add_all(pizzas)

    restaurants = []
    for i  in range(15):
        restaurant = Restaurant(name=fake.restaurant(),address = fake.address())
        restaurants.append(restaurant)
    db.session.add_all(restaurants)


    restaurant_pizzas = []
    for i in range(30):
        restaurant_pizza = RestaurantPizza( price=randint(1,30),pizzas_id = randint(1,15),restaurant_id = randint(1,15))
        restaurant_pizzas.append(restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
    