from app import app

#rodar a página home 
@app.route("/")
def index():
  coin = 320;
  return render_template("home.html", coin = coin)
