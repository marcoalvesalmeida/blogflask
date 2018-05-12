from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login  import LoginManager

blog = Flask(__name__)
blog.config.from_object('config')
db = SQLAlchemy(blog)
migrate = Migrate(blog, db)

manager = Manager(blog)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(blog)

from blog.models import tables, forms
from blog.controllers import default
