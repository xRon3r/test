from vehicle import Vehicle

class Motor(Vehicle):
    def __init__(self,type,color,speed,brand,cc,wheels,price):
        Vehicle.__init__(self,color,speed,brand,cc,wheels,price)
        self.type