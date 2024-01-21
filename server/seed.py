from faker import Faker
from random import randint, choice as rc 
from app import app 
from models import db,Pizza,Restaurant,RestaurantPizza

fake = Faker()
pizza_data = [
    {"name": "Margherita", "ingredients": "Tomato, mozzarella, basil"},
    {"name": "Pepperoni", "ingredients": "Pepperoni, tomato sauce, mozzarella"},
    {"name": "Vegetarian", "ingredients": "Mushrooms, bell peppers, onions, olives, tomato sauce, mozzarella"},
]


with app.app_context():
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    pizzas = []
    for pizza_info in pizza_data:
        pizza = Pizza(**pizza_info)
        db.session.add(pizza)

    db.session.add_all(pizzas)

    restaurants = []
    for i  in range(15):
        restaurant = Restaurant(name=fake.company(),address = fake.address())
        restaurants.append(restaurant)
    db.session.add_all(restaurants)


    restaurant_pizzas = []
    for i in range(30):
        restaurant_pizza = RestaurantPizza( price=randint(1,30),pizza_id = randint(1,15),restaurant_id = randint(1,15))
        restaurant_pizzas.append(restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
