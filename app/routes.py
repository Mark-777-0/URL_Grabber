from flask import render_template, jsonify, Request
import flask
from app import app
import httplib2
from bs4 import BeautifulSoup, SoupStrainer


@app.route('/grab',methods=['POST','GET'])
def grabLinks():
    
    website=list(flask.request.form.keys())[0]

    http = httplib2.Http()
    status, response = http.request(website)

    webLinks=[]

    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            webLinks.append(link['href'])

    return jsonify({'website':webLinks})



@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')