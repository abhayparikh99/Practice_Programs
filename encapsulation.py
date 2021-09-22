class Sample:
    def __init__(self):
        self.price = 50
        self.__newprice = 50
        print("Encapsulation")
    def display(self):
        print("Price =",self.price)
        print("New Price =",self.__newprice)
    def setNewPrice(self,newpricevalue):
        self.__newprice = newpricevalue

obj = Sample()
obj.display()
obj.price = 150
obj.__newprice = 150
print("---> After change 1 :")
obj.display()
print("---> After method change :")
obj.setNewPrice(500)
obj.display()