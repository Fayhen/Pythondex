from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config["SECRET_KEY"] = 'changeme' # Change this in production
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///pythondex.db'
cors = CORS(app, resources={r'/*': {'origins': '*'}}) # Restrict on production
db = SQLAlchemy(app)

print("Hello World")
