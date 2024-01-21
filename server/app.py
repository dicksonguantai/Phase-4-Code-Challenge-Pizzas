from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask import jsonify,request
from flask_restful import Resource
from models import db,Pizza,Restaurant,RestaurantPizza

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
    
api.add_resource(PizzaResource, '/pizzas')

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
    
api.add_resource(RestaurantResource, '/restaurants')

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
                "name": restaurant_found.name,
                "address": restaurant_found.address,
                "pizzas":pizzas_destructure
            }]
            return jsonify(restaurant),200
        else:
            return jsonify({"error":"Entered Restaurant is not available"})


    def delete(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id= id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            return "Restaurant deleted!!!!" , 204
        else:
            return jsonify({"error": "Cannot Delete non-existent restaurant"}),404
        

api.add_resource(RestaurantById, '/restaurants/<int:id>')



class RestaurantPizzaRelationship(Resource):
    def get(self):
        restaurants_pizzas = RestaurantPizza.query.all()
        restaurants_pizzas_list = [
            {
                "id":restpiz.id,
                "price":restpiz.price
            }
            for restpiz in restaurants_pizzas
        ]
        return jsonify(restaurants_pizzas_list),200
    
    def post(self):
        
        data = request.get_json()
        restpiz = RestaurantPizza(
            price = data["price"],
            pizza_id =data["pizza_id"],
            restaurant_id = data["restaurant_id"],
        )
        db.session.add(restpiz)
        db.session.commit()

        pizza_posted = Pizza.query.filter_by(id=data["pizza"]).first()
        pizza_posted_to_show=[
            {
                "id": pizza_posted.id,
                "name":pizza_posted.name,
                "ingredients": pizza_posted.ingredients

            }
        ]
        return jsonify(pizza_posted_to_show),200

api.add_resource(RestaurantPizzaRelationship, '/restaurant_pizzas')


if __name__ == "__main__":
    app.run(port=5555)

