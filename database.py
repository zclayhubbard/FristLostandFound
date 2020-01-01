import psycopg2
from sys import argv
from item import Item
from request import Request

credentials = "dbname=d6a3d0upkftvfu host=ec2-107-21-108-37.compute-1.amazonaws.com port=5432 user=edzebzygddyifx password=30f2dfe5104845e3756749993abf4a5afd49c116c76956f3ecda9b30cbd0f31f sslmode=require"

def prepare(value):
    index = value.find('_')
    index2 = value.find('%')
    prepared = value
    if (index >= 0):
        prepared = prepared[:index] + '\'' + prepared[index:]
    if (index2 >= 0):
        prepared = prepared[:index2] + '\'' + prepared[index:]

    prepared = '%' + prepared + '%'
    return prepared

def getItems(fullLog=True, category=None, query=None):
    conn = psycopg2.connect(credentials)
    cursor = conn.cursor()

    items = []

    # return full log of items
    if fullLog:
        s = "SELECT * FROM lostitems"
        cursor.execute(s)
        rows = cursor.fetchall()

        for r in rows:
            i = Item(str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(r[4]), str(r[5]), str(r[6]), str(r[7]), str(r[8]), str(r[9]), str(r[10]))
            items.append(i)

    elif query is not None and len(query.split()) is 0:
        s = "SELECT * FROM lostitems WHERE category LIKE %s"
        cursor.execute(s, ["%"+category+"%"])
        rows = cursor.fetchall()

        for r in rows:
            i = Item(str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(r[4]), str(r[5]), str(r[6]), str(r[7]), str(r[8]), str(r[9]), str(r[10]))
            items.append(i)

    else:
        # stmt = "SELECT * FROM lostitems WHERE category = %s AND (LOWER(color) LIKE %s OR LOWER(brand) LIKE %s OR LOWER(location) LIKE %s OR LOWER(description) LIKE %s OR LOWER(contact) LIKE %s)
        # stmt = "SELECT * FROM lostitems WHERE category = %s AND (POSITION(%s in LOWER(color)) > 0 OR POSITION(%s in LOWER(brand)) > 0  OR POSITION(%s in LOWER(location)) > 0 OR POSITION(%s in LOWER(description)) > 0 OR POSITION(%s in LOWER(contact)) > 0)"   
        q = query.split()
        params = []

        s = "SELECT * FROM lostitems WHERE "

        # if category != "":
        s += "category LIKE %s AND "
        params.append("%"+category+"%")

        s += "((POSITION(%s in LOWER(color)) > 0) OR (POSITION(%s in LOWER(brand)) > 0)  OR (POSITION(%s in LOWER(location)) > 0) OR (POSITION(%s in LOWER(description)) > 0) OR (POSITION(%s in LOWER(contact)) > 0))"

        for word in q:
            for i in range(5):
                params.append(word)
            cursor.execute(s, params)

            rows = cursor.fetchall()

            for r in rows:
                i = Item(str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(r[4]), str(r[5]), str(r[6]), str(r[7]), str(r[8]), str(r[9]), str(r[10]))
                items.append(i)

            for i in range(5):
                params.pop()

    
    cursor.close()
    conn.close()

    return items

def addItem(args):
    # prepare statements as needed
    s = "INSERT INTO lostitems VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT)"

    # insert into lostitems table
    conn = psycopg2.connect(credentials)
    cursor = conn.cursor()
    
    try:
        cursor.execute(s, args)
        conn.commit()
    except Exception as e:
        return str(e)

    cursor.close()
    conn.close()

    return "Item logged successfully!"

def addRequest(args):
    # prepare statements as needed
    s = "INSERT INTO requests VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT)"

    # insert into lostitems table
    conn = psycopg2.connect(credentials)
    cursor = conn.cursor()
    
    try:
        cursor.execute(s, args)
        conn.commit()
    except Exception as e:
        return str(e)

    cursor.close()
    conn.close()

    return "Request logged successfully!"    

def crossCheck(table, column, date):
    s = "SELECT * FROM "

    if table == "lostitems":
        s += "lostitems WHERE date "
    elif table == "requests":
        s += "requests WHERE datelost "
    else:
        raise ValueError("invalid table name")

    s += "BETWEEN date %s - interval '3 day' AND date %s + interval '3 day'"

    conn = psycopg2.connect(credentials)
    cursor = conn.cursor()

    args = [date, date]
    items = []
    reqs = []
    
    cursor.execute(s, args)
    rows = cursor.fetchall()

    if table == "lostitems":
        for r in rows:
            i = Item(str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(r[4]), str(r[5]), str(r[6]), str(r[7]), str(r[8]), str(r[9]), str(r[10]))
            items.append(i)    

        cursor.close()
        conn.close()
        return items

    elif table == "requests":
        for r in rows:
            #logBy, date, patronName, patronCont, dateLost, locLost, catg, brand, color, desc, Id
            q = Request(str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(r[4]), str(r[5]), str(r[6]), str(r[7]), str(r[8]), str(r[9]), str(r[10]))
            reqs.append(q)

        cursor.close()
        conn.close()
        return reqs


