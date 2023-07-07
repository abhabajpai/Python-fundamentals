class Employyee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return self.name
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves =newleaves
        # classs methods as alternative constructor
    @classmethod
    def from_str(cls, string):
        #params=string.split("-")
        #print (params)
        #return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print ("this is good"+ string)


harry=Employyee("Harry", 255,"sde")
#harry.change_leaves(34)
#rint (harry.no_of_leaves)
karan=Employyee.from_str("Karan-48-student")
#print (karan.name)
karan.printgood("abha")