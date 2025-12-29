class Parent:
    def fun1(self):
        print('hello')

class Child(Parent):
    def fun2(self):
        print('welcome')

    def fun1(self):   # method overiding
        print('Hiii')

myObj = Child()

myObj.fun2()
myObj.fun1()