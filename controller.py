from sys import argv, exit, stderr
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
# from database import Database
from item import Item

app = Flask(__name__, template_folder='.')

@app.route('/')
@app.route('/index')
def index():
    html = render_template('index.html')
    response = make_response(html)
    return response

@app.route('/makeRequest')
def loadRequestPage():
    html = render_template('makeRequest.html')
    response = make_response(html)
    return response

@app.route('/logItem')
def loadLogPage():
    html = render_template('logItem.html')
    response = make_response(html)
    return response
    
@app.route('/fullLog')
def loadFullLog():
    html = render_template('fullLog.html')
    response = make_response(html)
    return response

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port', file=stderr)
        exit(1)
    try:
        app.run(host='0.0.0.0', port=int(argv[1]))
    except ValueError as e:
        print("ValueError: port must be an integer", file=stderr)
