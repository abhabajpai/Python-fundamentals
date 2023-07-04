#break statement
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 != n2):
            if(n1 + n2 == n):
                found = True  # Set found to True
                break  # Break inner loop if a pair is found
    if found:
        print(n1, n2) # Print the pair
        break  # Break outer loop if a pair is found
#continue statement
num_list = list(range(5,15))
for i in num_list:
    if i==6 or i==8 or i==10:
        continue
    print(i)

