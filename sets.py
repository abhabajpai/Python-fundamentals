#creating a set
random_set = {"Educative", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))  # Length of the set
#set()constructor
empty_set=set()
print(empty_set)
#adding element
empty_set.add(2)
empty_set.update([2,3,4,5,7])
print(empty_set)
#deleting element
empty_set.remove(4)
print(empty_set)
#iterating a set
odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

print(unordered_set)

for num in unordered_set:
    if(not num % 2 == 0):
        odd_list.append(num)

print(odd_list)

