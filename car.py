from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,type,color,speed,brand,cc,wheels,price,licenceNumber):
        Vehicle.__init__(self,color,speed,brand,cc,wheels,price,licenceNumber)
        self.type=type
        print('you succesfully created a car!')

    def printCarAttributes(self):
        print('default attributes for {} are: color {}, speed {}, brand {}, cc {}, wheels {}, price {}£,'.format(self.type,
                                                                                                                 self.color,
                                                                                                                 self.speed,
                                                                                                                 self.brand,
                                                                                                                 self.cc,
                                                                                                                 self.wheels,
                                                                                                                 self.price))




