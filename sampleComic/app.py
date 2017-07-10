from flask import Flask, render_template, request, json, redirect


app=Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return(render_template('home.html'))

@app.route('/read/<string:page_details>')
def read(page_details):
    return (render_template('page.html', page_details=page_details))

@app.route('/blog')
def blogHome():
    return(render_template('blogHome.html'))

@app.route('/blog/<post>')
def blogPost(post):
    return(render_template('blogPost.html', post=post))

if(__name__=='__main__'):
    app.run(debug=True)

