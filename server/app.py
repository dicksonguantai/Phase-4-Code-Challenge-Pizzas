from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask import jsonify,request
from flask_restful import Resource
from models import db,Pizza,Restaurant

app = Flask(__name__)
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app)
db.init_app(app)

class Index(Resource):
    def get(self):
        return "Tumetoboa!!!!"
    
api.add_resource(Index, '/')

class PizzaResource(Resource):
    def get(self):
        all_pizzas= Pizza.query.all()
        pizzas_list = [
            {
                "id":pizza.id,
                "name":pizza.name,
                "ingredients":pizza.ingredients,
            }
            for pizza in all_pizzas
        ]
        return jsonify(pizzas_list),200
    

class RestaurantResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurants_list = [
            {
                "id": restaurant.id,
                "name": restaurant.name,
                "address":restaurant.address
            }
            for restaurant in restaurants
        ]
        return jsonify(restaurants_list),200
    

class RestaurantById(Resource):
    def get(self):
        restaurant_found = Restaurant.query.filter_by(id=id).first()
        if restaurant_found:
            pizzas_destructure = [{
                "id": pizza.id,
                "name":pizza.name,
                "ingredients": pizza.ingredients

            }
            for pizza in restaurant_found.pizzas
            ]
            restaurant = [{
                "id":restaurant_found.id,
                "name":
            }]












if __name__ == "__main__":
    app.run(port=5555)

