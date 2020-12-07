from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
import json
import os

app = Flask(__name__)

# To allow accessing application data from outside its domain
# for external apps
CORS(app)

# Change it for a better security key
# This is required for the login session
app.config['SECRET_KEY'] = 'secret-key-goes-here'

#login manager to authenticate agents
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(agent_id):
    # check of agent exists in database
    return Agent.query.get(int(agent_id))

#database configuration
DATABASE_USER = "Jonathan"   #Add your database username here
DATABASE_PASSWORD = "Jonathan"   #Add your database password here
DATABASE_PORT = 5432
DATABASE_NAME="loancompany"
print("MY_HOME:", os.environ['DATABASE_URL'])
DATABASE_URI = os.environ['DATABASE_URL'] + "?sslmode=require" or f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost:5432/loancompany"
# DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost:{DATABASE_PORT}/{DATABASE_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
PORT = os.environ['PORT']

db = SQLAlchemy(app)

api = Api(app)


#Customer data
class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    contact = db.Column(db.String())
    loan_amount = db.Column(db.Integer())
    loan_repaid = db.Column(db.Integer())
    prepayment = db.Column(db.Integer())
    arrears = db.Column(db.Integer())
    city = db.Column(db.String())
    region = db.Column(db.String())
    location = db.Column(db.String())
    coordinates = db.Column(db.String())

    def __init__(self, name, contact="", loan_amount=0, loan_repaid=0, prepayment=0, arrears=0, city="", region="", location="", coordinates=""):
        self.name = name
        self.contact = contact
        self.loan_amount = loan_amount
        self.loan_repaid = loan_repaid
        self.prepayment = prepayment
        self.arrears = arrears
        self.city = city
        self.region = region
        self.location = location
        self.coordinates = coordinates


    def __repr__(self):
        return f'<id {self.id}>'

    # to serialize its objects to json
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact':self.contact,
            'loan_amount':self.loan_amount,
            'loan_repaid':self.loan_repaid,
            'prepayment':self.prepayment,
            'arrears':self.arrears,
            'city':self.city,
            'region':self.region,
            'location':self.location,
            'coordinates':self.coordinates
        }

# Agent data
class Agent(UserMixin, db.Model):

    __tablename__ = 'agent'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def __repr__(self):
        return f'<id {self.id}>'

    #to serialized its objects to json
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password':self.password
        }

class Login(Resource):
    #login agent by sending post request with json to http://localhost:5000/login
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        agent = Agent.query.filter(Agent.email==email).first()
        if agent and check_password_hash(agent.password, password):
            login_user(agent)
            return jsonify({"message":"Agent logged in successfully"})
        else:
            return jsonify({"error":"Agent not registered or invalid data entered"})


class Logout(Resource):
    def get(self):
        logout_user()
        return jsonify({"message":"Agent logged out"})


class CustomerList(Resource):

    #decorator to check if agent is logged in to view data
    @login_required
    def get(self):
        customers = Customer.query.all()
        for i in range(len(customers)):
            customers[i] = customers[i].serialize()
        if customers:
            return jsonify({"data":customers})
        else:
            return jsonify({"data":"Empty dataset"})

class CustomerDetails(Resource):

    #decorator to check if agent is logged in to view data
    @login_required
    def get(self, customer_name):
        customer = Customer.query.filter(Customer.name==customer_name).first()
        if customer:
            customer = customer.serialize()
            return jsonify({"data":customer})
        return jsonify({"error":"No customer exist with this name"})

api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CustomerList, '/')
api.add_resource(CustomerDetails, '/customers/<customer_name>')

if __name__ == "__main__":
    app.run(debug=True,port=PORT)
