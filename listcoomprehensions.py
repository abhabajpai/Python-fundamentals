nums=[10,30,54,58,68]
nums_double=[n*2 for n in nums]
print(nums)
print(nums_double)
#Using Multiple Lists
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)
