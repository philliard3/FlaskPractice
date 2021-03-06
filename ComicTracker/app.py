from flask import Flask, render_template, request, session, json, redirect, url_for, Response
import pymongo
import tapaspy
import webtoonpy

client = pymongo.MongoClient()
# database of user accounts
userdb = client.accounttesting.users
'''
I need to come up with how to collect and store the comics. If I keep separate copies, then it'll take more space but will provide records.
'''
# database of comics from external sources
externalcomicdb = client.accounttesting.externalcomics
# database of comics that have been fused from multiple sources
aggregatecomicdb = client.accounttesting.aggregatecomics

# database of all tags
tagdb = client.accounttesting.tags

app = Flask(__name__)
app.secret_key = "change this string"

@app.route("/")
def homepage():
    return(render_template("index.html"))

# this is how you can send or receive stuff
@app.route("/api", methods=["POST", "GET"])
def api_test():
    if request.method == "POST":
        if "greeting" in request.form.keys():
            return(json.jsonify(message="valid!"))
        response = json.jsonify({"message":"invalid"})
        response.status_code = 400
        return(response)
    elif request.method == "GET":
        return(json.jsonify(message="gotten"))

@app.route("/register")
def register(failed=False):
    return(render_template("register.html", failed=failed))

@app.route("/login")
def login(failed=False):
    if "name" in session:
        return (redirect(url_for("dashboard", name=session["name"])))
    return(render_template("login.html", failed=failed))

@app.route("/registerattempt", methods=["POST"])
def register_attempt():
    if "name" in request.form.keys():
        if not(request.form["name"] in [i for i in userdb.find()]):
            # names.append(request.form["name"])
            userdb.insert({"name": request.form["name"]})
            return(redirect(url_for("login", failed=False)))
    return(redirect(url_for("register", failed=True)))

@app.route("/loginattempt", methods=["POST"])
def login_attempt():
    if "name" in request.form.keys():
        print([i for i in userdb.find()])
        if request.form["name"] in ([i["name"] for i in userdb.find()]):
            print("moving on")
            session["name"] = request.form["name"]
            return(redirect(url_for("dashboard", name=request.form["name"])))
    return(redirect(url_for("login", failed=True)))

@app.route("/logout")
def logout():
    session.pop("name", None)
    return(redirect(url_for("login")))

@app.route("/dashboard/")
@app.route("/dashboard")
def dashboard_no_name():
    if "name" in session:
        return(redirect(url_for("dashboard", name=session["name"])))
    return(redirect((url_for("login", failed=True))))

@app.route("/dashboard/<name>")
def dashboard(name=""):
    if name!="":
        return("<html><h1>Hello, "+name+".</h1></html>")
    return(redirect(url_for("login", failed=True)))

@app.route("/search")# , methods=["POST"])
def search():
    # tapas_titles = tapaspy.search_comic(comic_name=request.form["comic_name"])
    # webtoon_titles = webtoonpy.search_comic(comic_name=request.form["comic_name"])
    tapas_titles = tapaspy.search_comic("dragnarok")
    webtoon_titles = webtoonpy.search_comic("dragnarok")
    return(render_template("search.html", tapas_titles=tapas_titles, webtoon_titles=webtoon_titles))

def search_results():
    return

if(__name__=="__main__"):
    # userdb.remove()
    app.run(debug=True)


