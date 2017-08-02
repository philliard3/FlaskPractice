from flask import Flask, render_template, request, json, redirect, url_for, Response


app=Flask(__name__)

@app.route('/')
def homepage():
    return(render_template('index.html'))



# this is how you can send or receive stuff
@app.route('/api', methods=['POST', 'GET'])
def api_test():
    if request.method=='POST':
        if 'greeting' in request.form.keys():
            return(json.jsonify(message="valid!"))
        response = json.jsonify({'message':'invalid'})
        response.status_code = 400
        return(response)
    elif request.method=='GET':
        return(json.jsonify(message="gotten"))



@app.route('/login')
def login(failed=False):
    return(render_template('login', failed=failed))

@app.route('/loginattempt', methods=['POST'])
def login_attempt():
    if 'name' in request.form.keys():
        return(redirect(url_for('dashboard', name=request.form['name'])))
    else:
        return(redirect(url_for('login')))

@app.route('/dashboard')
def dashboard(name=''):
    if name=='':
        return(redirect(url_for('login', failed=True)))
    else:
        return('<html><h1>Hello,'+name+'.</h1></html>')

if(__name__=='__main__'):
    app.run(debug=True)


