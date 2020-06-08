from car import Car
from utils import *
from motor import Motor

if __name__ == '__main__':

    licenceNumber = int(input("First Please provide us with your licence number"))

    type = input('give me the type of vehicle you want')

    car_mercedes = Car(type,'red',265,'mercedes',2000,4,40000,licenceNumber)
    car_mercedes.printCarAttributes()

    licenceNumber = int(input("First Please provide us with your licence number"))
    type= input('give me the type of vehicle you want')
    car_audi = Car(type,'black',300,'audi',2500,4,35000,licenceNumber)
    car_audi.printCarAttributes()

    if IsValidLicence(car_mercedes.licenceNumber):
        print('it is valid')
    else:
        print('not valid')

    if IsValidLicence(car_audi.licenceNumber):
        print('it is valid')
    else:
        print('not valid')

    while True:
        tax= input('give me the % of tax')
        tax=int(tax)
        if tax>1 and tax<100:
            car_tax_mercedes = car_mercedes.getPriceAfterTax(tax)
            print(car_tax_mercedes)
            car_tax_audi = car_audi.getPriceAfterTax(tax)
            print(car_tax_audi)
            break
        else:
            print('give me a number between 1 and 100')
            break









