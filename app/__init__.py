from flask import Flask, render_template

#teste
app = Flask(__name__)
@app.route("/")
def index():
  coin = 320;
  return render_template("home.html", coin = coin)
  
