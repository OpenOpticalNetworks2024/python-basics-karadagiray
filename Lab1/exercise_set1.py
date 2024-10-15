"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    def product_or_sum(a, b):
    product = a * b
    if product > 1000:
        return a + b
    else:
        return product
        
    print(product_or_sum(a, b))

# ex2
def exercise2():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    sum_current_previous(start, end)
    
    def sum_current_previous(start, end):
    previous = 0
    for i in range(start, end + 1):
        current_sum = previous + i
        print(f"Current Number: {i}, Previous Number: {previous}, Sum: {current_sum}")
        previous = i
# ex3
def exercise3():
    def first_last_same(nums):
    return nums[0] == nums[-1]

    nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print(first_last_same(nums))

# ex4
def divisible_by_5(nums):
    for num in nums:
        if num % 5 == 0:
            print(num)

nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
divisible_by_5(nums)



# ex5
def exercise5():
    def count_emma(string):
    return string.count("Emma")

string = "I have a girlfriend and her name is Emma, I love Emma and Emma is from USA"
print(count_emma(string))

# ex6
def exercise6():
def create_third_list(list1, list2):
    result = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
    return result  # it checks if the number is odd or even

list1 = [int(x) for x in input("Enter numbers for first list: ").split()]
list2 = [int(x) for x in input("Enter numbers for second list: ").split()]
print(create_third_list(list1, list2))

# ex7
def exercise7():
    def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    return s1[:middle_index] + s2 + s1[middle_index:]
    
s1 = "giray"    #my name
s2 = "karadag"  #my last name  
print(append_in_middle(s1, s2)) 

# ex8
def exercise8():
    def first_middle_last(s1, s2):
    def get_middle(s):
        return s[len(s)//2] if len(s) % 2 != 0 else s[len(s)//2 - 1]
    
    new_string = s1[0] + get_middle(s1) + s1[-1] + s2[0] + get_middle(s2) + s2[-1]
    return new_string

s1 = "giray"  #my name
s2 = "karadag"  #my last name
print(first_middle_last(s1, s2))  


# ex9
def exercise9():
def count_characters(s):
    lowercase_count = sum(1 for c in s if c.islower())
    uppercase_count = sum(1 for c in s if c.isupper())
    digit_count = sum(1 for c in s if c.isdigit())
    special_count = sum(1 for c in s if not c.isalnum())
    
    return {
        'lowercase': lowercase_count,
        'uppercase': uppercase_count,
        'digits': digit_count,
        'special symbols': special_count
    }

s = "Giray Karadag!$ s323260"
print(count_characters(s))  

# ex10
def exercise10():
    def find_usa_occurrences(s):
    return s.lower().count("usa")

s = "USA is ignorant. usa is imperialist. U.S.A ."
print(find_usa_occurrences(s))  

# ex11
def exercise11():
def sum_and_average_of_digits(s):
    digits = [int(c) for c in s if c.isdigit()]
    total_sum = sum(digits)
    average = total_sum / len(digits) if digits else 0
    return total_sum, average

s = "giray323260karadag"
print(sum_and_average_of_digits(s)) 


# ex12
def exercise12():
    from collections import Counter

def count_all_characters(s):
    return dict(Counter(s))

s = "giray karadag"
print(count_all_characters(s))


if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()
