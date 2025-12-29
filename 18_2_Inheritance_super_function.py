class Parent:
    def fun1(self):
        print('hello')

class Child(Parent):
    def fun2(self):
        super().fun1()  #super function
        print('welcome')

myObj = Child()

myObj.fun2()