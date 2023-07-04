def abha_bajpai():
    print("abha")
abha_bajpai()
#min function

def minimum(min1,min2):
    if( min1<min2):
        print(min1)
    if (min1>min2):
        print(min2)
num1=98
num2=87
minimum(num1,num2)
#return statement
def miniret(a,b):
    if (a<b):
        return a
    return b
mv=miniret(num1,num2)
print(mv)
#altering data
num_list = [10, 20, 30, 40]
print(num_list)
def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10

multiply_by_10(num_list)
print(num_list)  # The contents of the list have been changed

#recursion
def fib(n):
    # The base cases
    if n <= 1:  # First number in the sequence
        return 0
    elif n == 2:  # Second number in the sequence
        return 1
    else:
        # Recursive call
        return fib(n - 1) + fib(n - 2)


print(fib(6))








