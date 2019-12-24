#
# Meant to be run just one time to initialize database with some test data 
#

import psycopg2
credentials = "dbname=d6a3d0upkftvfu host=ec2-107-21-108-37.compute-1.amazonaws.com port=5432 user=edzebzygddyifx password=30f2dfe5104845e3756749993abf4a5afd49c116c76956f3ecda9b30cbd0f31f sslmode=require"
conn = psycopg2.connect(credentials)
cursor = conn.cursor()

# just take the last ten-fifteen rows of the google sheet and add them to the database manually
    # put all the stuff in a 2d array and then loop w a standard statement
# it'll take for fucking ever but there's no other way tbh
# run it, make sure u commit
# then go to terminal, have it just print what's in it to test
# and then we can move on to getting it to display that info on the fullLog page correctly!


#[Date, Time, WD Attendant, Color, Brand, Where Found, Item Description, Contact info, In the safe?]

data = [
    ["Caton", "2019/12/2", "8:06", "CreditCardID", "orange", "Prox", "Outside front of frist", "Audrey Spensley Prox", "spensley@", False],
    ["Arianne","2019/12/2", "13:14", "Tech","white","Apple","Woolworth","Air pod", "", False],
    ["Anecia", "2019/12/2","3:29", "BottleUmbrella" ,"Rose Gold","","West TV Lounge","Rose Gold Umbrella", "", False],
    ["MJ","2019/12/3", "1:49","Clothing WalletPurse","blue","J Crew","Brought to desk by BSUP","Dark wash J crew jeans with a wallet in the front pocket belonging to Cameron Levy", "crlevy@", False],
    ["Anecia","2019/12/3","17:23", "JewelAccess", "Brown","Ralph Lauren","","Brown Ralph Lauren Glasses", "", False],
    ["Anecia", "2019/12/8","10:07","CreditCardID","Gold","Vanilla Visa", "Outside near prospect gardens", "Golf $50 Visa Gift Card", "", False],
    ["Faith","2019/12/8","16:43", "CreditCardID" , "orange", "prox", "200 level bathroom", "Prox (Sean-Wyn NG)", "seanwynn@", True],
    ["Yolore","2019/12/10","1:51","Tech" , "black", "lenovo", "A level table", "laptop charger","", False],
    ["Anecia","2019/12/10", "4:14","Tech","Rose Gold", "Apple", "found in one of the couches in a TV Lounge", "White face rosegold iPhone w/no case",	"", False],
    ["Runako","2019/12/11","8:04","CreditCardID","orange","","by spelman","prox", "", True],
    ["Grace","2019/12/11","18:23", "Tech","silver","Apple","Turned in by TA","Macbook with old charging port", "", False],
    ["Atarah","2019/12/11","20:36","CreditCardID","Red","Bank of America", "","Visa Debit Card (Temporary)","", True],
    ["Faith","2019/12/12", "9:49", "Clothing","blue","","bench by women's bathroom 100 level","blue denim looking coat.. not denim tho", "", False],
    ["Faith", "2019/12/12", "11:00", "Tech","blue","BOSE","McCosh 10","black and grey headphones", "", False],
    ["Zyanne","2019/12/12", "16:21","BookSchool","black", "Princeton","welcome desk","black folder, gold writing, princeton university, belongs to Daniel Leung", "dl13@", False],
    ["Atarah","2019/12/17","7:00","WalletPurse","Brown","","Lot21","Leather wallet belonging to Amir Dehghani", "", True],
    ["Edwin", "2019/12/17","5:55","Misc","green","toyota","west tv","key chain w toyota key and 2 extra keys w green rubber protectors", "", True],
    ["Atarah","2019/12/18","8:48","Clothing","Black","Princeton","","Princeton Votes 100 Baseball hat", "", False],
    ["Atarah","2019/12/18", "8:49","BottleUmbrella", "Blue","Contigo", "", "Blue (teal) waterbottle", "", False],	
    ["Faith","2019/12/23","9:00","Clothing","blue","ZT","women's center","blue fleece sweater", "", False]
    ]

# WDAttendant, Date, Time, Category, Brand, Color, Location, Description, Contact, inSafe, ID
stmt = "INSERT INTO lostitems VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT)"

for i in range(len(data)):
    currRow = data[i]
    #print(len(currRow))
    cursor.execute(stmt, currRow)

conn.commit()

test = "SELECT * FROM lostitems"
cursor.execute(test)
rows = cursor.fetchall()

for r in rows:
    print(r)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

cursor.close()
conn.close()


