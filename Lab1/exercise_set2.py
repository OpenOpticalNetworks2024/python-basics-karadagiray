"""Exercise Set 2: Data Structures"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    def pick_elements(list_one, list_two):
    odd_index_elements = list_one[1::2]  # Odd-index elements from the first list
    even_index_elements = list_two[0::2]  # Even-index elements from the second list
    result = odd_index_elements + even_index_elements  # Combine both lists
    return result
list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]
print(pick_elements(list_one, list_two))

# ex2
def exercise2():
def modify_list(sample_list):
    element = sample_list.pop(4)
    sample_list.insert(2, element)
    sample_list.append(element)
    return sample_list

sample_list = [34, 54, 67, 89, 11, 43, 94]
print(modify_list(sample_list))  


# ex3
def exercise3():
    def slice_and_reverse(sample_list):
    chunk_size = len(sample_list) // 3
    chunks = [sample_list[i:i + chunk_size] for i in range(0, len(sample_list), chunk_size)]
    return [chunk[::-1] for chunk in chunks]

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(slice_and_reverse(sample_list))  

# ex4
def exercise4():
    from collections import Counter

def count_occurrences(sample_list):
    return dict(Counter(sample_list))

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(count_occurrences(sample_list))  

# ex5
def exercise5():
def pair_elements(first_list, second_list):
    return set(zip(first_list, second_list))

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
print(pair_elements(first_list, second_list))  


# ex6
def exercise6():
    def remove_intersection(first_set, second_set):
    intersection = first_set.intersection(second_set)
    first_set.difference_update(intersection)
    return first_set
    
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print(remove_intersection(first_set, second_set))  



# ex7
def exercise7():
def check_subset_and_remove(first_set, second_set):
    if first_set.issubset(second_set):
        first_set.clear()
    elif second_set.issubset(first_set):
        second_set.clear()
    return first_set, second_set

first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print(check_subset_and_remove(first_set, second_set))  


# ex8
def exercise8():
    def filter_roll_numbers(roll_numbers, sample_dict):
    valid_values = set(sample_dict.values())
    roll_numbers = [num for num in roll_numbers if num in valid_values]
    return roll_numbers

roll_numbers = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
print(filter_roll_numbers(roll_numbers, sample_dict))  



# ex9
def exercise9():
def get_unique_values(speed_dict):
    return list(set(speed_dict.values()))

speed = {'Jan': 47, 'Feb': 52, 'March': 47, 'April': 44, 'May': 52, 'June': 53, 'July': 54, 'Aug': 44, 'Sept': 54}
print(get_unique_values(speed))  


# ex10
def exercise10():
    def remove_duplicates_and_find_min_max(sample_list):
    unique_elements = tuple(set(sample_list))
    return unique_elements, min(unique_elements), max(unique_elements)

sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
unique_tuple, min_value, max_value = remove_duplicates_and_find_min_max(sample_list)
print(unique_tuple, min_value, max_value)  



if __name__ == "__main__":
    print("EXERCISE SET 2: Data Structures")
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
