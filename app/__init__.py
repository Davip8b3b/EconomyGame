from flask import Flask
from flask.cli import FlaskGroup, with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

cli = FlaskGroup(app)

@with_appcontext
@cli.command()
def create_db(): 
  db.create_db()
  print("Banco de dados criado com sucesso!")
  
from app.controllers import default
