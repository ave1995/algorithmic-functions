import random

def random_number_order_simple(count):
    numbers = random.sample(range(1, count + 1), count)
    print(numbers)
    return numbers

def random_number_order(count):
    numbers = []
    for i in range(1, count + 1):
        numbers.append(i)
    
    for number in numbers:
        randomIndex = random.randint(0, count - 1)
        temp = numbers[randomIndex]
        numbers[randomIndex] = number
        numbers[numbers.index(number)] = temp
        
    print(numbers)
    return numbers
        

if __name__ == "__main__":
    random_number_order_simple(10)
    random_number_order(10)