import datetime
from flask import Flask,render_template,request,session
from flask_session import Session
#from flask import redirect,url_for

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/",methods=["POST","GET"])
def index():
    # headline = "This is CS50"
    # return render_template("index.html",headl = headline)
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("notes.html",notes=session["notes"])



# @app.route("/<string:name>")
# def personal(name):
#     name = name.capitalize()
#     return "<h1>Welcome to CS50 "+name+"!</h1>"
#


@app.route("/isitchristmas")
def isChristmas():
    now = datetime.datetime.now()
    christmas = now.month == 12 and now.day == 25
    return render_template("christmas.html",christmas = christmas)



@app.route("/form")
def form():
    return render_template("form.html")



@app.route("/welcome",methods=["POST","GET"])
def welcome():
    if request.method == "GET":
        #return redirect(url_for("form"))
        return "<h4>please submit the form instead</h4>"+render_template("form.html")
    name = request.form.get("input1")
    return "<h1>Welcome to CS50 " + name + "!</h1>"



if __name__ == "__main__":
    app.run()
