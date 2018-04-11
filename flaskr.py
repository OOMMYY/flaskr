#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask, url_for
from flask import render_template
from flask import send_from_directory
from flask import Markup
import markdown

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name = ""):
    print "func body helle_word"
    if name != "":
        return render_template('hello.html', name = name)
    else:
        return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/url_for')
def fun_url_for():
    print url_for('hello_world')
    print url_for('static', filename = 'style.css')
    return "url_for"

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    pass

@app.route('/user/<username>')
def profile(username):
    pass

@app.route('/')
def index():
    return 'Index Page'

#返回html
@app.route('/baidu')
def baidu():
    return send_from_directory('html', 'baidu.html')

#download
@app.route('/download')
def down_load():
    return send_from_directory('markdown', 'hello.md')

#返回markdown
@app.route('/markdown')
def markdown_fun():
    with open('markdown/hello.md') as f:
        content = f.read().decode('utf8')
	content = Markup(markdown.markdown(content, ['extra']))
    return content	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000)
