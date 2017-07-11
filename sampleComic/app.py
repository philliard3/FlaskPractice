from flask import Flask, render_template, request, json, redirect
import pymongo

app=Flask(__name__)
client = pymongo.MongoClient()
pages = client.comicdata.pages
comicglobals = client.comicdata.globals
blogposts = client.blogdata.posts

@app.errorhandler(404)
def page_not_found(e):
    return('Looks like you wanted a page that doesn\'t exist.', 404)

@app.route('/')
@app.route('/home')
def homepage():
    return(render_template('home.html'))

@app.route('/read/<string:page_details>')
def read(page_details):
    imagepath = ''
    # retrieve image path
    for page in pages:
        if(page['id']==page_details):
            imagepath = page['imagepath']
            last_id=page['last']
    if(imagepath==''):
        return(render_template('pageNotFound.html'))
    else:
        return(render_template('page.html', imagepath=imagepath))

@app.route('/blog')
def blogHome():
    return(render_template('blogHome.html'))

@app.route('/blog/<post>')
def blogPost(post):
    posttext = ''
    # retrieve image path
    for blogpost in blogposts:
        if(blogpost['id']==post):
            posttext = blogpost['posttext']
    if(posttext==''):
        return(render_template('blogPostNotFound.html'))
    else:
        return(render_template('blogPost.html', posttext=posttext))

if(__name__=='__main__'):
    app.run(debug=True)
