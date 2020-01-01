class Request (object):
    def __init__(self, logBy, date, patronName, patronCont, dateLost, locLost, catg, brand, color, desc, Id):
        self.__id = Id
        self.__logBy = logBy
        self.__date = date
        self.__patronName = patronName
        self.__patronCont = patronCont
        self.__dateLost = dateLost        
        self.__locLost = locLost
        self.__catg = catg
        self.__brand = brand
        self.__color = color        
        self.__desc = desc
    
    def getId(self):
        return self.__id

    def getLogBy(self):
        return self.__logBy

    def getDt(self):
        y, m, d = self.__date.split("-")
        return m + "/" + d + "/" + y

    def getPatName(self):
        return self.__patronName
    
    def getPatCont(self):
        return self.__patronCont

    def getDtLost(self):
        y, m, d = self.__dateLost.split("-")
        return m + "/" + d + "/" + y
    
    def getLocLost(self):
        return self.__locLost

    def getCat(self):
        catMap = {
            "null" : None,
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

    def getDesc(self):
        return self.__desc        