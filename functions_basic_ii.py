# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
print('1. Countdown:')

def countdown(num):
    new_list = []
    for i in range(num, -1, -1):
        new_list.append(i)
    return new_list
# Example: countdown(5) should return [5,4,3,2,1,0]
print(countdown(5))
print(' \n')


# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
print('2. Print and Return:')

def print_and_return(list):
    print(list[0])
    return(list[1])
# Example: print_and_return([1,2]) should print 1 and return 2
return_val_1 = print_and_return([1,2])
print(return_val_1)
print(' \n')


# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
print('3. First Plus Length:')

def first_plus_length(list):
    sum = list[0] + len(list)
    return sum
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
return_val_2 = first_plus_length([1,2,3,4,5])
print(return_val_2)
print(' \n')


# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
print('4. Values Greater than Second:')

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    second = list[1]
    for num in list:
        if num > second:
            new_list.append(num)
    print(len(new_list))
    if len(new_list) < 2:
        return False
    else:
        return new_list
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
return_val_3 = values_greater_than_second([5,2,3,2,1,4])
print(return_val_3)
# Example: values_greater_than_second([3]) should return False
return_val_4 = values_greater_than_second([3])
print(return_val_4)
print(' \n')


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
print('5. This Length, That Value:')

def this_length_that_value(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
# Example: length_and_value(4,7) should return [7,7,7,7]
return_val_5 = this_length_that_value(4,7)
print(return_val_5)
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
return_val_6 = this_length_that_value(6,2)
print(return_val_6)