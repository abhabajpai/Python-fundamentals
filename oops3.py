#self and init
class Employee:
    def __init__(self, salary, id, job):
        self.salary=salary
        self.id=id
        self.job=job
    
#abhishek=Employee()
rahul=Employee(20000,4,"sde")
#print(abhishek)
print(rahul)
print(rahul.salary)
print(rahul.id)
#decorators
def dec1(func1):
    def nowexec():
        print("exacuting now")
        func1 ()
        print("executed")
    return nowexec
def abha():
    print("abha is a good girl")
abha=dec1(abha)
abha()
        