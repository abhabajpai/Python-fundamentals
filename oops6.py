class Abha:
    def __init__(self,name=None):
        self.__name=name
       
    def setName(self,x):
        self.__name=x
    def getName(self):
        return (self.__name)
    
Rahul=Abha('rahul')
print("before setting", Rahul.getName())
Rahul.setName('rahul2')
print("after setting", Rahul.getName())