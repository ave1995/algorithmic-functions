#   WEEKLY CHALLENGE

#   This week’s challenge: Write a function to solve the Two Sum problem, a popular interview question. Given an array of integers and a target sum, return the indices of the two numbers that add up to the target.
#   For example, given the array [2, 7, 11, 15] and the target sum 9, the function should return [0, 1] because 2 + 7 = 9.

from array import array

numbers = array('i', [2, 7, 11, 15]) 
target = 9

def two_sum(numbers: array, target: int) -> array:
    checked = set()

    for number in numbers:
        possible_number = target - number
        if possible_number in checked:
            return [possible_number, number]
        checked.add(number)

    return []

result = two_sum(numbers, target)

if result:
    print(f"Pair found: {result}")
else:
    print("No pair found for the target!")