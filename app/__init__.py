from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#rodar a página home 
@app.route("/")
def index():
  coin = 320;
  return render_template("home.html", coin = coin)
  
