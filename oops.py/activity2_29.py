class computer:
    def __init__(self):
        self.__maxPrice=900
    def sell(self):
        print("Selling price: {}".format(self.__maxPrize))
    def setMaxPrice(self, price):
        self.__maxPrice= price

obj= computer()
obj.sell()

obj.__maxPrice= 1000
obj.sell()

obj.setMaxPrice(1000)
obj.sell()