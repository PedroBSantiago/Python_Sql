# from flask import Flask, render_template, request, redirect
# import _mysql_connector;

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("html.html")

from flask import Flask, render_template, request, redirect
import mysql.connector 

app = Flask(__name__, template_folder= "templates")

@app.route("/")
def index():
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)