from models import db,api
from flask import jsonify,request
from flask_restful import Resource 
from .models import Restaurant,Pizza, RestaurantPizza


class Index(Resource):
    def get(self):
        return "Tumetoboa!!!!"
    
api.add_resource(Index, '/')


