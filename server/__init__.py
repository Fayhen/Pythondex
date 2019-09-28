from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config["SECRET_KEY"] = 'changeme' # Change this in production
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///pythondex.db'
cors = CORS(app, resources={r'/*': {'origins': '*'}}) # Restrict on production
db = SQLAlchemy(app)
ma = Marshmallow(app)

from server import routes

# Swagger configuration
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
swagger_blueprint = get_swaggerui_blueprint(
  SWAGGER_URL,
  API_URL,
  config={
    "app_name": "Pythondex"
  }
)

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)
