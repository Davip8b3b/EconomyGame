from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
  coin = 320;
  return render_template("home.html", coin = coin)
  
if __name__ == "__main__":
  app.run(debug=True)