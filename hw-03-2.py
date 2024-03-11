import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    for _ in range(quantity):
        numbers = list(random.sample(range(min, max), quantity))
    return sorted(numbers)

result = get_numbers_ticket(1, 31, 5)
print(f"Ваші лотерейні числа: {result}")
