class Abha:
    def __init__(self,favcolor,name,age):
        self.favcolor=favcolor
        self.name=name
        self.age=age
    def printdetails(self):
        print("favorite color is",self.favcolor)
        print(" name is",self.name)
        print("age is",self.name)
class rohit(Abha):
    def __init__(self,favcolor,name,age,sex):
        Abha.__init__(self,favcolor,name,age)
        self.sex=sex
    def printrohitdetails(self):
        self.printdetails()
        print("age:",self.age)

obj1=rohit('yellow','abha',23,'female')
obj1.printrohitdetails()
