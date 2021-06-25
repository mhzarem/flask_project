from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_package.config import Config

db=SQLAlchemy()



def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from flask_package.main.route import main
    from flask_package.add.routes import add
    app.register_blueprint(add)
    app.register_blueprint(main)

    return app