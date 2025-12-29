class phone1:   # parent class/super class
    def feature1(self):
        print('camera')

class phone3:    # parent class/super class
    def feature3(self):
        print('blutooth')
        
class phone2(phone1,phone3):  # child class/sub class
    def feature2(self):
        print('internet')



myObj = phone2()
myObj.feature1()
myObj.feature2()
myObj.feature3()