#Challenge 1
from traceback import print_tb


def sum_to(n):
    return n * (n + 1) // 2

# print(sum_to(6)) # returns 21
# print(sum_to(10)) # returns 55

#Challenge 2

def largest(list):
    current = 0
    largest_num = 0 
    for num in list:
        if current < num:
            current = num
            largest_num = current
    return largest_num
            

# print(largest([1, 2, 3, 4, 0])) # returns 4
# print(largest([10, 4, 2, 231, 91, 54]))  # returns 231

#Challenge 3

def occurrences(str1, str2):
    return str1.count(str2)

# print(occurrences('fleep floop', 'p'))

#Challenge 4

def product(*args):
    num = 1
    for arg in args:
        num *= arg
    return num

# print((product(-1, 5)))