import projects #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("travel.html", projects=projects.setup())


@app.route("/greece/")
def greece_route():
    return render_template("greece.html", projects=projects.setup())

@app.route("/italy/")
def italy_route():
    return render_template("italy.html", projects=projects.setup())

@app.route("/spain/")
def spain_route():
    return render_template("spain.html", projects=projects.setup())

@app.route("/france/")
def france_route():
    return render_template("france.html", projects=projects.setup())

@app.route("/germany/")
def germany_route():
    return render_template("germany.html", projects=projects.setup())

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)