class Item (object):
    def __init__(self, logBy, date, time, catg, brand, color, location, desc, contact, inSafe, Id):
        self.__id = Id
        self.__logBy = logBy
        self.__date = date
        self.__time = time
        self.__catg = catg
        self.__brand = brand
        self.__color = color
        self.__location = location
        self.__desc = desc
        self.__contact = contact
        self.__inSafe = inSafe

    def getId(self):
        return self.__id

    def getLogBy(self):
        return self.__LogBy

    def getDt(self):
        y, m, d = self.__date.split("-")
        return m + "/" + d + "/" + y

    def getTm(self):
        h, m, s = self.__time.split(":")
        hour = int(h)

        if hour < 12:
            ampm = "AM"
        else:
            ampm = "PM"

        if hour is 0:
            hour = 12
        elif hour > 12:
            hour = hour - 12

        return str(hour) + ":" + m + " " + ampm

    def getCat(self):
        catMap = {
            "Clothing" : "Clothing",
            "JewelAccess" : "Jewelry/Accessories",
            "Tech" : "Technology",
            "BookSchool" : "Books/School",
            "BottleUmbrella" : "Water Bottles/Umbrellas",
            "CreditCardID" : "Credit Card/ID",
            "WalletPurse" : "Wallet/Purse",
            "Misc" : "Miscellaneous"
        }

        cats = self.__catg.split()

        r = ""
        for c in cats:
            r = r + catMap[c] + ", "

        return r[:-2]
    
    def getBrd(self):
        return self.__brand

    def getClr(self):
        return self.__color

    def getLoc(self):
        return self.__location

    def getDesc(self):
        return self.__desc
    
    def getCont(self):
        return self.__contact

    def getInSafe(self):

        if self.__inSafe == 'True':
            return "Yes"
        else:
            return "No"