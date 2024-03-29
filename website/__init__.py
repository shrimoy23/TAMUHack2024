from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "random ass key" # We need to add a secret key to run our server for some reason
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Creates key with database as value
    db.init_app(app) 

    from .chat import chat
    from .chat import plan
    from .auth import auth
    from .planner import my_plan
    from .home import homepage
    from .about import about

    app.register_blueprint(chat, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    app.register_blueprint(plan, url_prefix = '/')
    app.register_blueprint(homepage, url_prefix = '/')
    app.register_blueprint(about, url_prefix = '/')
    app.register_blueprint(my_plan, url_prefix ='/')

    from .db_objs import User, Note
    
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # Shows the page
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # .get method looks for primary key, so we dont have to use id='' as a parameter

    return app