from flask import Flask, render_template, request, json, redirect, url_for, Response

names = []
app=Flask(__name__)

@app.route("/")
def homepage():
    print("names="+str(names))
    return(render_template("index.html"))



# this is how you can send or receive stuff
@app.route("/api", methods=["POST", "GET"])
def api_test():
    if request.method=="POST":
        if "greeting" in request.form.keys():
            return(json.jsonify(message="valid!"))
        response = json.jsonify({"message":"invalid"})
        response.status_code = 400
        return(response)
    elif request.method=="GET":
        return(json.jsonify(message="gotten"))


@app.route("/register")
def register(failed=False):
    return(render_template("register.html", failed=failed))

@app.route("/login")
def login(failed=False):
    return(render_template("login.html", failed=failed))

@app.route("/registerattempt", methods=["POST"])
def register_attempt():
    if "name" in request.form.keys():
        if not(request.form['name'] in names):
            names.append(request.form['name'])
            return(redirect(url_for("login", failed=False)))

    return(redirect(url_for("register", failed=True)))


@app.route("/loginattempt", methods=["POST"])
def login_attempt():
    if "name" in request.form.keys():
        print(names)
        if request.form["name"] in names:
            return(redirect(url_for("dashboard", name=request.form["name"])))

    return(redirect(url_for("login", failed=True)))

@app.route("/dashboard/<name>")
def dashboard(name=""):
    if name!="":
        return("<html><h1>Hello, "+name+".</h1></html>")
    return(redirect(url_for("login", failed=True)))
if(__name__=="__main__"):
    app.run(debug=True)


