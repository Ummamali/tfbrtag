# app/__init__.py

import os

from flask import Flask

from flask_cors import CORS

def create_app():

	app = Flask(__name__)
	CORS(app)

	# Import the routes to register them with the app
	from app.routes.root_route import root_bp

	# Register the blueprints
	app.register_blueprint(root_bp)

	return app
