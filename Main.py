# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home():
  return render_template("mainwebsite.html")

@app.route("/g")
def git():
	return render_template("menu.html")

@app.route("/spain")
def spain():
	return render_template("spain.html")

@app.route("/italy")
def italy():
	return render_template("italy.html")

#@app.route("/germany")
#def germany():
	#return render_template("germany.html")

#@app.route("/greece")
#def greece():
	#return render_template("greece.html")

if __name__ == "__main__":
  #runs the application on the repl development server
  app.run(debug = True)