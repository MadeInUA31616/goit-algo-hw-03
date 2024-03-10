import random

def get_numbers_ticket(min, max, quantity):
    for _ in range(quantity):
        numbers = list(random.sample(range(min, max), 5))

    return numbers

result = get_numbers_ticket(1, 31, 5)
print(f"Ваші лотерейні числа: {result}")
