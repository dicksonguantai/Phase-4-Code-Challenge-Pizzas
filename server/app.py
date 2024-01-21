from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app)
db.init_app(app)