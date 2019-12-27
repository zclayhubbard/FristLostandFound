from sys import argv, exit, stderr
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from database import *
from item import Item

app = Flask(__name__, template_folder='.')

@app.route('/')
@app.route('/index')
def index():
    html = render_template('index.html')
    response = make_response(html)
    return response

# def search:
    # triggered when you submit the search box on the landing page
    # takes cookies from search, queries database, gets rows of results
    # makes them into Item objects, renders the template with them and sends it back

@app.route('/makeRequest')
def loadRequestPage():
    html = render_template('makeRequest.html')
    response = make_response(html)
    return response

@app.route('/submitRequest')
def submitRequest():
    # triggered when submitting request form
    # first takes key terms and searches lostitems table for any pings
        # this is gonna be the trickiest part, because we don't want it to return every item ykno
        # i think the key is gonna be only searching within a certain range of dates
    # if it gets any good results from table, render a page that says okay are you sure it isn't any of these?
        # this could probably be a separate page that's set up just like fullLog but with a button to continue at the bottom
        # would need to also handle how you get out of that page, that's another two events but we'll come back to that
    # if we don't get any good results, then we just update the requests table and keep it moving

    # [LoggedBy, Date, PatronName, PatronContact, DateLost, LocationLost, Category, Brand, Color, Description, ID],


    # first round (Basic insertion):
    # get args
    loggedby = request.args.get("wdName")
    date = request.args.get("date")
    patronname = request.args.get("patronName")
    patroncontact = request.args.get("patronContact")
    datelost = request.args.get("dateLost")
    locationlost = request.args.get("locationLost")
    category = request.args.get("category")
    brand = request.args.get("brand")
    color = request.args.get("color") # if empty set to None (?)
    desc = request.args.get("descriprion")

    # clean info

    args = [loggedby, date, patronname, patroncontact, datelost, locationlost, category, brand, color, desc]
    errorsuccess = addRequest(args)

    html = render_template('requestErrorSuccess.html', errorsuccess=errorsuccess)
    response = make_response(html)
    return response


@app.route('/logItem')
def loadLogPage():
    html = render_template('logItem.html')
    response = make_response(html)
    return response

@app.route('/submitItem')
def submitItem():
    # triggered when submitting item form
    # first takes key terms and searches requests table for any pings
        # this is gonna be the trickiest part, because we don't want it to return every request ykno
        # i think the key is gonna be only searching within a certain range of dates
    # if it gets any good results from table, render a page that says okay are you sure it isn't any of these?
        # this could probably be a separate page that's set up just like fullLog but with a button to continue at the bottom
        # would need to also handle how you get out of that page, that's another two events but we'll come back to that
    # if we don't get any good results, then we just update the lostitems table and keep it moving 

    # WDAttendant, Date, Time, Category, Color, Brand, Location, Description, Contact, inSafe, ID 

    # first round (Basic insertion):
    # get args
    loggedby = request.args.get("wdName")
    date = request.args.get("date")
    time = request.args.get("time")
    category = request.args.get("category")
    brand = request.args.get("brand")
    color = request.args.get("color")
    location = request.args.get("locationFound")
    desc = request.args.get("description")
    contact = request.args.get("contactInfo") # if empty set to None (?)
    insafe = request.args.get("safe")

    # clean info

    args = [loggedby, date, time, category, color, brand, location, desc, contact, insafe]
    errorsuccess = addItem(args)

    html = render_template('itemErrorSuccess.html', errorsuccess=errorsuccess)
    response = make_response(html)
    return response

@app.route('/fullLog')
def loadFullLog():
    items = getItems()
    html = render_template('log.html', items=items)
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
