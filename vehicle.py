class Vehicle():
    def __init__(self,color,speed,brand,cc,wheels,price,licenceNumber):
        self.color = color
        self.speed = speed
        self.brand = brand
        self.cc = cc
        self.wheels = wheels
        self.price = price
        self.licenceNumber=licenceNumber


    def changeColor(self,color):
        self.color = color

    def getMaxSpeed(self):
        return self.speed

    def getPriceAfterTax(self,tax):
        return self.price*tax*0.01 + self.price

    def getBrand(self):
        return self.brand