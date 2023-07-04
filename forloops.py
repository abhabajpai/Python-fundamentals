for i in range(8):
    print(i)
name='Abhishek'
for i in name:
    print(i)
#list example
colour=["red","green","yellow","blue"]
for i in colour:
    print(i)
for i in range(1,9):
    print(i)
for k in range(1,12,3):
    print(k)
new_list=[35,68,70,90]
print(new_list)
for i in range(0, len(new_list)):
    new_list[i]=new_list[i]*2
print(new_list)
#nestedforloop
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
    for n2 in num_list:  # Now we have two iterators
        if(n1 != n2):
            if(n1 + n2 == n):
                print(n1, n2)
