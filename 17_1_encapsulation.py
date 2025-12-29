class myclass:

    x = 10  # public variable

    __y = 20  #private variable
    def disp(self):  #want to create function to access private variables
        return self.__y

    def meth1(self):  # public method
        print("Hello")
        self.__meth2() # access private method using public method

    def __meth2(self):   # private method
        print("Welcome")
    

myObj = myclass()
print(myObj.x)  #access public variable 
print(myObj.disp())  # acce private variable using method



myObj.meth1() # call public method
#myObj.meth2()  # can not direct call private method,so we want to call private method inside public method and,
               # when call public both private and public methods are access