from flask import Flask, render_template, request, json, redirect


app=Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return(render_template('home.html'))

@app.route('/projects')
def projectsPage():
    return(render_template('projects.html'))

@app.route('/blog')
def blogHome():
    return(render_template('blogHome.html'))

@app.route('/blog/<post>')
def blogPost(post):
    return(render_template('blogPost.html', post=post))

@app.route('/about')
def aboutPage():
    return(render_template('about.html'))

@app.route('/contact')
def contactPage():
    return(render_template('contact.html'))

@app.route('/graph')
def make_graph():
    return('<html>'++'</html>')

'''
#most of that could be summarized as:
@app.route('/<page>')
def renderPage():
    return(render_template(str(page)+'.html'))

'''


if(__name__=='__main__'):
    app.run(debug=True)

