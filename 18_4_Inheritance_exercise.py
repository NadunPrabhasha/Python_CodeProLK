class Fruit:
    num_of_items = None
    unit_price = None

    def set_value(self,x,y):
        self.num_of_items = x
        self.unit_price = y


class Apple(Fruit):
    def price(self):
        print('For apple',self.num_of_items*self.unit_price)


class Orange(Fruit):
    def price(self):
        print('For orange',self.num_of_items*self.unit_price)


class Mango(Fruit):
    def price(self):
        print('For mango',self.num_of_items*self.unit_price)


myObj1 = Apple()
myObj2 = Orange()
myObj3 = Mango()

myObj1.set_value(12,40)
myObj2.set_value(8,30)
myObj3.set_value(40,3)

myObj1.price()
myObj2.price()
myObj3.price()


