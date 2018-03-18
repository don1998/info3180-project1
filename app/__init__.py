from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a super secure key"  # you should make this more random and unique
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/project1"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pgezgjwaizhwyt:a63c6da35a37acf1143984c4e9aff02c0da00259c9de7756193d01d5e6048c39@ec2-54-204-44-140.compute-1.amazonaws.com:5432/dd7s809ja5aln8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning

db = SQLAlchemy(app)

UPLOAD_FOLDER ='./app/static/uploads'


# Flask-Login login manager
login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page
login_manager.login_message_category = "info"  # customize the flash message category

app.config.from_object(__name__)
from app import views
