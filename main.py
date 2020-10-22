import projects #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("travel.html", projects=projects.setup())


@app.route("/spain/")
def greece_route():
    return "<h1 style='background-color:blue;color:white'>Greece!</h1>"

@app.route("/italy/")
def italy_route():
    return "<h1 style='background-color:blue;color:white'>Italy!</h1>"

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)