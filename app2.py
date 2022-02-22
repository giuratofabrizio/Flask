from flask import Flask, request, render_template
import Datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getTime", methods=['GET'])
def getTime():
   ora = Datetime.time 