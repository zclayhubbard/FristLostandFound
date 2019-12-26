import psycopg2
from sys import argv
from item import Item

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

def getItems(fullLog=True, category=None, searchTerm=None):
    conn = psycopg2.connect(credentials)
    cursor = conn.cursor()

    # return full log of items
    if fullLog:
        s = "SELECT * FROM lostitems"
        cursor.execute(s)
        rows = cursor.fetchall()
        items = []

        for r in rows:
            i = Item(str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(r[4]), str(r[5]), str(r[6]), str(r[7]), str(r[8]), str(r[9]), str(r[10]))
            items.append(i)
        
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