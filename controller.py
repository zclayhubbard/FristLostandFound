#---------------------------------------
# controller.py
# Author: Zyanne Clay-Hubbard
#---------------------------------------
from sys import argv, exit, stderr
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    response = make_response("index.html")
    return response


# -----------------------------------------------------------------------
if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)

    app.run(host='0.0.0.0', port=int(argv[1]), debug=True) 