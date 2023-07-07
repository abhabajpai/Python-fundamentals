class Employee:
    no_of_leaves=9
    pass
abha=Employee()
abhi=Employee()
abha.name="abha bajpai"
abha.salary=444
abha.role="SDE"
abhi.name="abhi bajpai"
abhi.salary=467
abhi.role="SDE"
print(abha.__dict__)
print(Employee.no_of_leaves)
abha.no_of_leaves=8
print(abha.__dict__)