from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask import jsonify,request,make_response
from flask_restful import Resource
from models import db,Pizza,Restaurant,RestaurantPizza
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app,db)
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
        response = make_response(jsonify(pizzas_list),200)
        return response
    
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
        response = make_response(jsonify(restaurants_list),200)
        return response
    
api.add_resource(RestaurantResource, '/restaurants')

class RestaurantById(Resource):
    def get(self,id):
        restaurant_found = Restaurant.query.filter_by(id=id).first()
        if restaurant_found:
            pizzas_destructure = [{
                "id": pizza.id,
                "name":pizza.name,
                "ingredients": pizza.ingredients

            }
            for pizza in restaurant_found.pizzas
            ]
            response = make_response({
                "id": restaurant_found.id,
                "name": restaurant_found.name,
                "address": restaurant_found.address,
                "pizzas": pizzas_destructure
            }, 200)
            return response
        else:
            return make_response(jsonify({"error":"Entered Restaurant is not available"}),404)


    def delete(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id= id).delete()
            db.session.delete(restaurant)
            db.session.commit()

            return "Restaurant deleted!!!!" 
        else:
            return make_response(jsonify({"error": "Cannot Delete non-existent restaurant"}),404)
        

api.add_resource(RestaurantById, '/restaurants/<int:id>')



class RestaurantPizzaRelationship(Resource):
    def get(self):
        restaurants_pizzas = RestaurantPizza.query.all()
        restaurants_pizzas_list = [
            {
                "id":restpiz.id,
                "price":restpiz.price,
                "restaurant_id": restpiz.restaurant_id,
                "pizza_id":restpiz.pizza_id
            }
            for restpiz in restaurants_pizzas
        ]
        response  = make_response(jsonify(restaurants_pizzas_list),200)
        return response
    
    def post(self):
        
        data = request.get_json()
        restpiz = RestaurantPizza(
            price = data["price"],
            pizza_id =data["pizza_id"],
            restaurant_id = data["restaurant_id"],
        )
        db.session.add(restpiz)
        db.session.commit()

        pizza_posted = Pizza.query.filter_by(id=data["pizza_id"]).first()
        pizza_posted_to_show=[
            {
                "id": pizza_posted.id,
                "name":pizza_posted.name,
                "ingredients": pizza_posted.ingredients

            }
        ]
        response  = make_response(jsonify(pizza_posted_to_show),200)
        return response

api.add_resource(RestaurantPizzaRelationship, '/restaurant_pizzas')


if __name__ == "__main__":
    app.run(port=5555)

