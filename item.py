class Item (object):
    def __init__(self, Id, wdAtt, date, time, catg, brand, color, location, desc, contact):
        self.__id = Id
        self.__wdAtt = wdAtt
        self.__date = date
        self.__time = time
        self.__catg = catg
        self.__brand = brand
        self.__color = color
        self.__location = location
        self.__desc = desc
        self.__contact = contact

    def getId(self):
        return self.__id

    def getWd(self):
        return self.__wdAtt

    def getDt(self):
        return self.__date

    def getTm(self):
        return self.__time

    def getCat(self):
        return self.__catg
    
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
