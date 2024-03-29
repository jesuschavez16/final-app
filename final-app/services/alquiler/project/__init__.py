# services/alquiler/project/__init__.py


import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



#instanciando la db
db = SQLAlchemy() 


def create_app(script_info=None):

    #instanciar la app
    app = Flask(__name__)


    #establecer configuracion
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
   
    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.alquiler import alquiler_blueprint
    app.register_blueprint(alquiler_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
	    return {'app': app, 'db': db}

    return app

