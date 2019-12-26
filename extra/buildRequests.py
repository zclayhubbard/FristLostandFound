#
# Meant to be run just one time to initialize database with some test data 
#

import psycopg2
credentials = "dbname=d6a3d0upkftvfu host=ec2-107-21-108-37.compute-1.amazonaws.com port=5432 user=edzebzygddyifx password=30f2dfe5104845e3756749993abf4a5afd49c116c76956f3ecda9b30cbd0f31f sslmode=require"
conn = psycopg2.connect(credentials)
cursor = conn.cursor()

# data = [
#     ["Kadence", "", "Menelik Graham", "menelikg@princeton.edu", "2019/12/4", "", "Tech", "Apple", "white", "airpods (case and buds)"],
#     ["Toni", "", "Lindsay Li", "lindsayl@princeton.edu", "2019/12/5", "Guyot Hall", "Tech", "Dell", "gray", "gray computer bag with Dell laptop"],
#     ["Alex", "", "Christopher Lugo", "clugo@princeton.edu", "2019/12/6", "A level", "JewelAccess", "Head", "Black", "black gloves"],
#     ["Serena", "", "Jacqueline Xu", "jx5@princeton.edu", "2019/12/9", "Einstein Room", "Tech", "Apple", "white", "apple pencil"],
#     ["Zyanne", "", "Fwata", "2034828719", "2019/12/10", "west tv lounge, on the couches", "Tech", "Apple", "", "student from debate tournament left behind macbook pro, in a black case"],
#     ["Krystal", "", "Nancy Coffin", "ncoffin@princeton.edu", "2019/12/13", "Misc", "", "Silver, Red, and Green", "University Keys, painted green and red"],
#     ["Yolore", "", "Shivani", "203-491-7979 203-219-4192", "2019/12/10", "TV couches", "Tech", "Apple", "Black", "black case on a macbook pro"],
#     ["Krystal", "", "Matheus Martins", "609-627-9300 math.martins@icloud.com", "2019/12/12", "CreditCardID", "", "Blue-ish", "Brazilian Passport Stars on the front page"],
#     ["", "", "Yurian Quinones", "ybq@princeton.edu (949)-973-0483", "2019/12/6", "Anywhere on the path from rocky to cottage", "WalletPurse", "", "Dark brown", "Dark brown leather wallet"],
#     ["malachi", "", "Elaine Pagels", "6092030795", "2019/12/24", "Area near Frist", "BooksSchool", "", "Black", "Black flat appt book 8.5/5"],
#     ]	


# [LoggedBy, Date, PatronName, PatronContact, DateLost, LocationLost, Category, Brand, Color, Description, ID],

stmt = "INSERT INTO requests VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT)"

for i in range(len(data)):
    #print(i)
    currRow = data[i],
    print(currRow)
#     cursor.execute(stmt, currRow)

# conn.commit()

# test = "SELECT * FROM lostitems"
# cursor.execute(test)
# rows = cursor.fetchall()

# for r in rows:
#     print(r)
#     print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# cursor.close()
# conn.close()


